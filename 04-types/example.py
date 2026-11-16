x = input("x: ")       # always a string
y = int(x) + 1         # convert before doing math
print(f"x: {x}, y: {y}")
print(type(x), type(y))

print(int("4"), float("4"), str(4), bool(""))

# truthiness
for value in [None, 0, 0.0, "", [], {}, "False", "0", " "]:
    print(repr(value), "->", bool(value))
