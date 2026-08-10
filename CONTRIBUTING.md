# Working on Motion32

## Setting up the test environment

The offline suite runs without Ableton or hardware, but four of its guards decompile Live's own
framework to check control names and skin namespaces against the real thing. Those four need two
pieces that are **not** in this repository:

**1. Live's control-surface framework.** Copy `ableton/v3/control_surface/` out of your own Live 12
installation into `Resources/control_surface/`. That path is gitignored because the `.pyc` is
Ableton's proprietary code and is not ours to redistribute. Searching your Live install directory
for `control_surface` finds it faster than following a path from memory.

**2. `xdis`**, which reads the `.pyc`:

```
pip3 install xdis --break-system-packages
```

Then:

```
bash run-tests.sh
```

A full green run is **4,147 assertions across 170 groups, zero failures**. Without the two pieces
above you get roughly 66 fewer assertions and 4 failures, and those failures are correct — a guard
that cannot run is reported as a failure rather than skipped. See §6b-13 in the implementation
notes for why: an earlier version reported "0 failures" while silently checking nothing.

The count is expected to rise as guards are added. If it *drops*, something stopped running.

## Making a change

One branch per issue, merged through a pull request.

```
git checkout main
git pull
git checkout -b fix/sends-label-helper
```

Branch naming: `fix/…` for bugs, `feat/…` for new behaviour, `refactor/…` for structural work.

Then edit, and before touching hardware:

```
bash run-tests.sh
```

Green means it is safe to try on the device. Red means it is not — the suite exists precisely
because several of these bugs would look like "nothing happened" on hardware rather than like an
error.

## Committing

```
git add -A
git commit -m "Sends: single send_label helper, A-L with numeric fallback

Fixes #1"
```

Putting `Fixes #N` in the commit or PR body closes the issue automatically when the branch merges,
which keeps the issue list honest without extra bookkeeping.

## Opening the pull request

```
git push -u origin fix/sends-label-helper
gh pr create --fill
```

Read the diff on GitHub before merging. This is the review checkpoint — the point of the branch is
that you see the change as a whole, in one place, before it becomes `main`. Then:

```
gh pr merge --squash --delete-branch
git checkout main
git pull
```

Squash keeps one commit per fix on `main`, so the history reads as a list of resolved issues rather
than a stream of work-in-progress saves.

## Hardware testing

The offline suite cannot see the device. These need a real Motion 32 and are called out in the
issues that touch them:

- held-pad and stuck-note behaviour across layout changes
- meter cost at 10 Hz under load
- teardown and reconnect behaviour
- anything that changes what goes on the wire

After a hardware run, check `Log.txt` against the list in the README.

## Editing on GitHub

If you edit a file in the GitHub web UI — a README typo, say — that commit lands on `main` and your
local clone is immediately behind. Run `git pull` before you start local work, or the next commit
diverges and has to be untangled by hand.
