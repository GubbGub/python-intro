# Escape sequences
print("She said \"hi\"\nThen left.")

# Indexing & slicing
course = "Python Programming"
print(len(course))    # 18
print(course[0])      # P
print(course[-1])     # g
print(course[0:6])    # Python
print(course[7:])     # Programming

# Methods return NEW strings
messy = "  Python Programming  "
print(messy.strip().upper())
print(messy.replace("Python", "Java"))
print(messy.split())
print("Pro" in messy)

# f-strings
name = "Sam"
score = 95.5
print(f"Hello {name}")
print(f"Next year: {score + 5}")
print(f"Rounded: {score:.0f}")
