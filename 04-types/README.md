# Lesson 4 · Types, conversions & truthiness

**Time:** ~25 minutes

## The idea

Every value has a **type**: `str` (text), `int` (whole number), `float` (decimal), `bool` (True/False), and more. Python won't mix types for you, so you have to convert them yourself.

```py
x = input("x: ")       # always a string, e.g. "4"
# y = x + 1            → TypeError: can't add a str and an int
y = int(x) + 1         # convert first
print(f"x: {x}, y: {y}")

int("4")     # 4
float("4")   # 4.0
str(4)       # "4"
bool("")     # False
print(type(x))   # <class 'str'>
```

**Why the error?** `"4" + 1` is ambiguous. Should it be `5`, or the text `"41"`? Python refuses to guess, so you say which you mean with `int()` or `str()`.

### Truthiness

Every value counts as `True` or `False` when it's used in an `if`.

- **Falsy:** `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, and any other empty collection
- **Truthy:** everything else

**Gotcha:** `bool("False")` and `bool("0")` are both **True**. They're non-empty strings, and Python looks at whether a string is empty, not at what it says.

## Exercise: part 1, predict first

**Before running anything**, write down what you think each line prints. Then run it and check.

```py
print(bool(0))
print(bool("0"))
print(bool(" "))
print(bool([]))
print(int(3.9))
print(int("3.9"))
```

<details>
<summary>Answers</summary>

`False`, `True`, `True` (a space is a character), `False`, `3` (`int()` chops off the decimal, it doesn't round), and then a **ValueError**: `int()` can't read a decimal string directly. Use `int(float("3.9"))`.
</details>

## Exercise: part 2, adder

Ask the user for two numbers and print their sum. It should work for decimals like `2.5` too.

**Expected output**
```
First number: 2.5
Second number: 4
2.5 + 4.0 = 6.5
```

## Check yourself

<details>
<summary>What does <code>type(input("age: "))</code> return if the user types 17?</summary>

`<class 'str'>`. `input()` always returns a string.
</details>

## Go deeper

OpenStax, [*Introduction to Python Programming*](https://openstax.org/details/books/introduction-python-programming): §2.2 Type conversion, §2.3 Mixed data types.
