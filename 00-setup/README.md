# Lesson 0 · Setup

**Time:** ~20 minutes

## The idea

To run Python you need two things:
- the **Python interpreter**, the program that reads your code and runs it
- an **editor** to write the code in

We'll use **VS Code** as the editor, and run everything from its built-in terminal.

## Install

1. **Python.** Download it from [python.org/downloads](https://www.python.org/downloads/). On Windows, tick **"Add python.exe to PATH"** on the first screen of the installer.
2. **VS Code.** Download it from [code.visualstudio.com](https://code.visualstudio.com/).
3. In VS Code, open the **Extensions** panel and install **Python** (the one published by Microsoft).

Check that it worked by opening a terminal (**Ctrl + \`**) and typing:

```bash
python --version     # Windows also accepts: py --version
```

You should see something like `Python 3.13.1`.

## The example

Make a file called `hello.py`, type this in, save it, and run `python hello.py` in the terminal:

```py
print("Hello, world!")
```

## Shortcuts worth learning now

| What | Windows | Mac |
|---|---|---|
| Open / close the terminal | Ctrl + \` | Ctrl + \` |
| Save | Ctrl + S | Cmd + S |
| Clear the terminal | type `cls` | Cmd + K (click the terminal first) |
| Problems panel (every error and warning) | Ctrl + Shift + M | Shift + Cmd + M |
| Command Palette (run any command) | Ctrl + Shift + P | Shift + Cmd + P |

## Exercise

In `exercise.py`, print three lines: your name, the city you live in, and one thing you want to build with Python.

## Check yourself

<details>
<summary>What's the difference between VS Code and the Python interpreter?</summary>

VS Code is where you **write** code. The interpreter is the program that **runs** it. You could write Python in Notepad and it would still run, because the interpreter is what matters.
</details>

## Go deeper

OpenStax, [*Introduction to Python Programming*](https://openstax.org/details/books/introduction-python-programming): §1.1 Background, §1.8 Why Python?
