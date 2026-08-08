# Motion 32 Native Mode USB/Event Stream Follow-Up

This follow-up targets two questions:

1. Where does USB-MIDI receive dispatch enter the firmware, especially around the native-entry command `8F 00 7F`?
2. What does the internal event stream at `0x20004084` do with opcodes `0x14`, `0x15`, `0x16`, and `0x36`?

Evidence comes from:

- `Motion32UsbDispatchTraceProbe.java` -> `usb_dispatch_trace_probe.md`
- `Motion32EventStreamConsumerProbe.java` -> `event_stream_consumer_probe.md`
- `Motion32NativeEventFollowupProbe.java` -> `native_event_followup_probe.md`

## USB-MIDI Dispatch

### Corrected Address Map

In the payload import, the active endpoint setup routine is:

- `FUN_00002a14(int param_1)`: initializes the inbound framed-byte queue at `0x200040a0`, marks the USB send-ready flag `DAT_20005b60 = 1`, then configures one of two USB endpoint contexts.
- `FUN_00004854(context, descriptor)`: generic USB endpoint/config setup.
- `FUN_00002a60(buffer, length, port_id)`: sends bytes through endpoint context `0x20005cd4` when `port_id == 1`, otherwise through `0x20005d24`.

Startup calls `FUN_00002a14(9)`, so the main path uses:

- context `0x20005d24`
- descriptor/config struct at `0x00009874`
- send port argument `9`

Earlier forced-function output around `0x97e4` / `0x9874` was misleading. These addresses are descriptor/config data, not executable callback code.

### Descriptor Data

The descriptor at `0x9874` contains:

```text
00009874: 09 02 00 00 02 04 02 05 02 06 02 07 00 00 00 00
00009884: a8 98 00 00 c5 2a 00 00 00 00 00 00 94 98 00 00
00009894: 00 01 00 00 dc 40 00 20 0f 00 ff ff ...
```

The important word is `c5 2a 00 00`, a Thumb pointer to `0x00002ac4`.

### Confirmed Receive Feeder

`0x00002ac4` decodes as a tiny USB event callback:

```c
void USB_event_feeder(int event)
{
  if (*(char *)(event + 4) == 2) {
    DAT_20005b60 = 1;
  }
  else if (*(char *)(event + 4) == 4) {
    FUN_00000d6c(0x200040a0, *(undefined1 *)(event + 8));
  }
}
```

Implication:

- Event type `2` is a send-ready/completion event.
- Event type `4` feeds one byte from `event + 8` into `0x200040a0`.
- `0x200040a0` is the inbound Fender SysEx/framed-byte queue consumed by `FUN_000010a4` / old `FUN_000020a4`, which waits for `F0`, matches the Fender prefix, buffers payload, and ends on `F7`.

This does not explain `8F 00 7F`. The current concrete path around `0x02ac4` is byte-stream/SysEx-oriented, not a full USB-MIDI packet decoder. If `8F 00 7F` changes native mode, its parser is likely upstream of this feeder or in a separate MIDI/channel-voice receive path, not in the `0x200040a0` framed queue consumer.

## Internal Event Stream `0x20004084`

### Queue Writers

`0x20004084` is an outbound queue for firmware-generated host messages.

The ring helpers are:

- `FUN_00000d6c(queue, byte)`: enqueue one byte.
- `FUN_00000d54(queue)`: compute available byte count.
- `FUN_00000dc0(queue, dest, limit)`: dequeue/copy bytes.

The encoder functions are:

```c
FUN_00000f6c(control_id, value)
  optional selector: (control_id - 0x50) & 0xff
  0x14
  value

FUN_00000fb0(control_id, delta)
  optional selector: (control_id - 0x50) & 0xff
  0x15
  delta + 0x40

FUN_00000eec(control_id, value14)
  optional selector: (control_id - 0x50) & 0xff
  0x16
  high 7 bits
  0x36
  low 7 bits
```

`DAT_20004081` caches the last selector, so repeated events on the same logical control omit the selector byte.

### Queue Consumer

`FUN_00000ff4()` drains the event queue:

```c
void FUN_00000ff4(void)
{
  int n = FUN_00000d54(0x20004084);
  if (n != 0) {
    FUN_00000dc0(0x20004084, 0x20004324, n);
    FUN_00002a60(0x20004324, n, 9);
  }
}
```

So the event stream is sent to the host through the main endpoint/context `0x20005d24`.

### Hardware Scan Producers

`FUN_00008944()` is a main scan/service loop. In the relevant path it calls:

- `FUN_0000140c()`: compares relative accumulators and emits `0x15` delta events.
- `FUN_00001618(&DAT_200064c0)`: prepares/scales current scan values.
- `FUN_00001288(&DAT_200064c0)`: compares absolute values and emits `0x16` / `0x36` 14-bit events.

`FUN_00001288()` sends 14-bit absolute values for `DAT_200045ca` controls:

- mode/protocol 0: `DAT_200045ca = 2`
- mode/protocol 1: `DAT_200045ca = 1`

`FUN_0000140c()` sends relative deltas for `DAT_200045cc` controls:

- mode/protocol 0: `DAT_200045cc = 8`
- mode/protocol 1: `DAT_200045cc = 9`

The per-mode relative control-id table starts at `0x9664`:

```text
mode/protocol 0: 00 03 05 07 01 02 04 06 08
mode/protocol 1: 02 08 06 05 01 00 07 04 03
```

Because the encoder writes `(control_id - 0x50) & 0xff`, these map to selector bytes:

```text
mode/protocol 0: B0 B3 B5 B7 B1 B2 B4 B6 B8
mode/protocol 1: B2 B8 B6 B5 B1 B0 B7 B4 B3
```

This looks very much like the firmware's native CC/channel-style stream for knobs/wheel/touch controls.

### Framed Message Builder

`FUN_00001030(payload, len)` builds outgoing Fender-framed messages into the same queue:

- mode/protocol 0 prefix: `F0 08 26 05`
- mode/protocol 1 prefix: `F0 08 24 05`
- skips payload bytes whose signed value is negative
- appends `F7`

This confirms `0x20004084` carries both native continuous-control events and Fender SysEx/framed responses.

## Useful Conclusions

1. `0x20004084` is a real outbound host queue.
2. `0x14`, `0x15`, `0x16`, and `0x36` are firmware-authored MIDI-like event bytes, not arbitrary internal enum values.
3. The consumer path is concrete: hardware scan -> encoder -> queue `0x20004084` -> copy to `0x20004324` -> send via `FUN_00002a60(..., 9)` -> endpoint context `0x20005d24`.
4. The active receive callback embedded in the endpoint descriptor is `0x02ac4`, and it feeds only the inbound framed-byte queue `0x200040a0`.
5. The `8F 00 7F` native-entry parser was not found in this path. The strongest current hypothesis is that native-entry is handled in lower USB-MIDI/channel-voice receive dispatch before bytes reach the Fender SysEx queue, or in a separate endpoint/service routine called by the USB stack.

## Best Next Pulls

1. Follow `FUN_000047f0()` and the callbacks/config words in the `0x9874` descriptor struct. That is where endpoint packet send/receive mechanics may expose the missing channel-voice dispatch.
2. Force-create/decompile the label block around `0x011f4`, because it calls `FUN_00000ff4()` and likely tells us the event-queue drain cadence.
3. Decode the setup pairs at `0x95fc`; they are used by `FUN_000016f4()` to configure the scanned controls and may identify which physical inputs correspond to the absolute controls.
4. Trace `FUN_00000e50()`. It selects all the important table variants: SysEx prefix, absolute-control count, relative-control count, and relative-control id order.
