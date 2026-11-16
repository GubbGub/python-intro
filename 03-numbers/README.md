# Lesson 3 · Numbers & math

**Time:** ~25 minutes

## The idea

Python is a calculator with a few extra operators that turn out to be very useful in real programs.

```py
print(10 + 3)    # 13     addition
print(10 - 3)    # 7      subtraction
print(10 * 3)    # 30     multiplication
print(10 / 3)    # 3.333… division (always gives a float)
print(10 // 3)   # 3      floor division: drops the decimal, rounds down
print(10 % 3)    # 1      modulus: the remainder
print(10 ** 3)   # 1000   exponent
```

**Why `//` and `%` matter:** together they split a number into "how many whole groups" and "what's left over". 10 ÷ 3 is **3** groups with **1** left over. Sanity check: `3 * 3 + 1 == 10`. That one idea converts minutes to hours, cents to dollars, and seconds to clock time.

**Augmented assignment** is shorthand for updating a variable:

```py
x = 10
x = x + 3   # long way
x += 3      # same thing; also -=, *=, /=, //=, %=, **=
```

**Complex numbers** use `j` for the imaginary unit (√−1):

```py
x = 1 + 2j
print(x.real)    # 1.0
print(x.imag)    # 2.0
```

**Helpful functions:**

```py
import math

print(round(3.14159, 2))   # 3.14
print(abs(-5))             # 5
print(math.ceil(4.2))      # 5 — round up
print(math.floor(4.8))     # 4 — round down
```

More in the [Python math docs](https://docs.python.org/3/library/math.html).

## Exercise: time converter

A movie is `135` minutes long. Use `//` and `%` to print it as hours and minutes. Then do the same for a 1,000,000-second countdown, in days, hours, minutes and seconds.

**Expected output**
```
135 minutes = 2 h 15 min
1000000 seconds = 11 days, 13 h, 46 min, 40 s
```

## Check yourself

<details>
<summary>What is <code>-7 // 2</code>?</summary>

`-4`, not `-3`. Floor division rounds **down**, toward negative infinity, not toward zero. −3.5 rounded down is −4.
</details>

<details>
<summary>How can you tell if a number <code>n</code> is even?</summary>

`n % 2 == 0`: even numbers leave no remainder when you divide by 2.
</details>
