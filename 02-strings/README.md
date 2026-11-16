# Lesson 2 · Strings

**Time:** ~40 minutes (the longest lesson; take a break halfway)

## The idea

A **string** is text: a **sequence** of characters in quotes. Because it's a sequence, every character has a position, and Python gives you tools to slice it, clean it and fill it in.

### 1. Escape sequences: characters you can't type directly

| Write | Prints |
|---|---|
| `\'` or `\"` | a quote inside a string |
| `\\` | one backslash |
| `\n` | a new line |
| `\t` | a tab |

```py
print("She said \"hi\"\nThen left.")
```

### 2. Indexing & slicing: positions start at 0

```py
course = "Python Programming"

print(len(course))    # 18 — number of characters
print(course[0])      # P — first character
print(course[-1])     # g — last character (negative counts from the end)
print(course[0:6])    # Python — start at 0, stop BEFORE 6
print(course[7:])     # Programming — from 7 to the end
```

**Why "stop before"?** Because then `course[0:6]` has exactly `6 - 0 = 6` characters. Sanity check: `"Python"` has 6 letters.

### 3. Functions vs. methods

- A **function** stands on its own: `print()`, `len()`, `input()`, `type()`.
- A **method** belongs to an object and is called with **dot notation**: `course.upper()`.
- `input()` shows a prompt and waits for the user. **It always returns a string**, even if they type a number. Lesson 4 deals with that.

### 4. String methods

```py
course = "  Python Programming  "

print(course.upper())                    # all uppercase
print(course.lower())                    # all lowercase
print(course.title())                    # First Letter Of Each Word
print(course.strip())                    # remove whitespace from both ends
print(course.lstrip())                   # remove leading whitespace
print(course.rstrip())                   # remove trailing whitespace
print(course.find("Python"))             # index of first match, or -1 if not found
print(course.replace("Python", "Java"))  # replace every match
print(course.split())                    # ['Python', 'Programming']
print("Pro" in course)                   # True
print("Pro" not in course)               # False
```

Strings are **immutable**: methods hand you back a *new* string, and `course` itself never changes. To keep the result, store it: `course = course.strip()`.

### 5. f-strings: fill values into text

Put `f` before the quotes, then drop variables or expressions inside `{ }`. You don't need `+` to join pieces together.

```py
name = "Sam"
score = 95.5

print(f"Hello {name}")              # Hello Sam
print(f"Next year: {score + 5}")    # Next year: 100.5
print(f"Rounded: {score:.0f}")      # Rounded: 96
```

## Exercise: name tidier

Ask the user for their full name. Assume they type it messily, like `   ada   LOVELACE  `. Then print:
1. the name cleaned up in Title Case
2. their initials
3. how many characters the cleaned name has
4. a greeting built with an f-string

**Expected output** (for the input above)
```
Clean: Ada Lovelace
Initials: A.L.
Length: 12
Welcome to Python, Ada!
```

Hint: `.split()` turns the name into a list of words; `[0]` gets the first one.

## Check yourself

<details>
<summary>What does <code>"Python"[1:4]</code> give?</summary>

`"yth"`: it starts at index 1 (`y`) and stops *before* index 4. That's 4 − 1 = 3 characters.
</details>

<details>
<summary>After <code>s = " hi "</code> and then <code>s.strip()</code>, what is <code>s</code>?</summary>

Still `" hi "`. Strings are immutable, and `.strip()` returned a new string that you didn't store. You need `s = s.strip()`.
</details>

## Go deeper

OpenStax, [*Introduction to Python Programming*](https://openstax.org/details/books/introduction-python-programming): §1.4 String basics.
