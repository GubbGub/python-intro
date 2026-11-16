raw = input("Full name: ")

clean = " ".join(raw.split()).title()   # split() also removes the extra spaces between words
first, last = clean.split()[0], clean.split()[-1]

print(f"Clean: {clean}")
print(f"Initials: {first[0]}.{last[0]}.")
print(f"Length: {len(clean)}")
print(f"Welcome to Python, {first}!")
