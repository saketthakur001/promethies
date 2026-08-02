# promethies

A small personal habit/task-tracking experiment. It's an early-stage, work-in-progress project — parts of it are exploratory notebook scratch work rather than a finished tool.

## What it does

The core idea is a `TaskForge` class (in `main.py`, also duplicated/explored in `main.ipynb`) that tracks a few personal habit categories — Books, Movies, Music, Meditation — each with a priority score, a tasks file, and a history log:

- `TaskForge.__init__` creates `TaskForge.md` (a priorities index) if it doesn't already exist.
- `update_tasks(task, tasks_list, priority)` writes a `<task>_tasks.md` file listing the given tasks under a priority header.
- `update_history(task, history_list)` appends timestamped entries to a `<task>_history.md` file.
- `check_meditation()` reads `meditation_history.md` and returns the timestamp of the last logged meditation entry (used to see how long it's been since the last session).

Running `main.py` directly logs a "Completed: 30 minutes meditation" entry to `meditation_history.md` and prints the last meditation timestamp.

## Key files

- `main.py` — the `TaskForge` class and a small example/demo run at the bottom.
- `main.ipynb` — notebook version of the same ideas, with extra scratch cells (an Obsidian-vault-writing experiment, half-written helper functions, a `reminder()` message prompt, and other in-progress snippets). Treat this as a dev notebook, not a finished module.
- `TaskForge.md` — the generated priorities file for Books/Movies/Music/Meditation.
- `prototype.py` — a standalone, unrelated script: a password-gated console prompt that prints a personal motivational note and saves the user's rating/thoughts to markdown files (`me_ratings.md`, `thinkeyMode.md`, `ThinkeyThoughts`). It's a personal-use script, not a reusable tool.
- `loop.py` / `loop_test.ipynb` — currently empty placeholders for future work.

## Running it

No external dependencies are required for `main.py` (standard library only). From the repo root:

```bash
python main.py
```

This will create `TaskForge.md` and `meditation_history.md` (if missing) in the current directory and print the timestamp of the last meditation entry.

`prototype.py` can be run the same way, but it's interactive and personal in nature (it asks for a password and writes to markdown files named after the author's own notes system):

```bash
python prototype.py
```

## Limitations

- This is a personal experiment, not a packaged application — there's no CLI, config file, or install step beyond running the scripts directly.
- `main.ipynb` contains dead/commented-out code and half-finished functions (e.g. an empty `thoughts_to_store()`); it documents the evolution of `main.py` more than it provides working functionality on its own.
- `loop.py` and `loop_test.ipynb` are empty — whatever they were meant to hold hasn't been written yet.
- `check_meditation()` has an unreachable `print` statement after a `return` in the "no history" branch.
- File paths (e.g. the Obsidian vault path in `main.ipynb`) are hardcoded to the original author's machine and won't work elsewhere.
