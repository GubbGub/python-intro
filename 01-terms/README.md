# Lesson 1 · Terms

**Time:** ~15 minutes

## The idea

A handful of words come up constantly. Learn them once and the docs and error messages start to make sense.

| Term | Meaning |
|---|---|
| **Python interpreter** | The program that runs Python code. |
| **Expression** | A piece of code that **produces a value**, such as `2 + 3` or `len(name)`. |
| **Module** | A `.py` file of code you can `import` and reuse instead of rewriting it. |
| **Library** | A collection of modules grouped together to solve bigger problems, like math, data analysis or games. |
| **PEP** | *Python Enhancement Proposal*, a design document for the language. **PEP 8** is the standard style guide for Python code. |
| **Linter** | A tool that checks your code for likely errors and style problems before you run it. |

The key habit: **you don't write everything yourself.** Python ships with modules for common jobs. `import` one, then use **dot notation** to reach what's inside it.

## The example

```py
import math              # import a built-in module

print(math.sqrt(16))     # dot notation looks inside the module → 4.0
print(math.pi)           # modules hold values too → 3.141592653589793
```

Why does `math.sqrt(16)` print `4.0` and not `4`? Square roots are usually not whole numbers, so `sqrt` always gives back a decimal (a *float*). Lesson 3 covers this.

## Exercise

Using the `math` module, find:
1. the area of a circle with radius 5 (area = π r²)
2. the hypotenuse of a right triangle with legs 3 and 4

**Expected output**
```
78.53981633974483
5.0
```

## Check yourself

<details>
<summary>Is <code>print</code> an expression?</summary>

`print("hi")` is a call that *does* something (it shows text). It does technically produce a value, `None`, but we call it for its effect, not its value. `2 + 3` is an expression you'd use for its value, `5`.
</details>

<details>
<summary>Module or library: what's <code>math</code>?</summary>

A **module**: it's a single unit you import. A library like NumPy is a whole collection of modules.
</details>

## Go deeper

OpenStax, [*Introduction to Python Programming*](https://openstax.org/details/books/introduction-python-programming): §2.1 The Python shell, §2.6 The math module, §2.7 Formatting code.
