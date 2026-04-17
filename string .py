# Create string
s = "Hello World"
print("Original String:", s)

# Accessing characters
print("First character:", s[0])
print("Last character:", s[-1])

# Slicing
print("Sliced (0:5):", s[0:5])
print("Reversed string:", s[::-1])

# Length
print("Length of string:", len(s))

# Case conversion
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title case:", s.title())

# Searching
print("Index of 'World':", s.find("World"))
print("Count of 'l':", s.count('l'))

# Replace
print("Replace 'World' with 'Python':", s.replace("World", "Python"))

# Checking functions
print("Is alphabetic:", s.isalpha())
print("Is digit:", s.isdigit())
print("Is alphanumeric:", s.isalnum())

# Remove spaces
s2 = "  Hello  "
print("Strip spaces:", s2.strip())

# Split and Join
words = s.split()
print("Split string:", words)

joined = "-".join(words)
print("Joined string:", joined)

# Concatenation
s3 = "Python"
print("Concatenation:", s + " " + s3)

# Repetition
print("Repetition:", s3 * 3)

# Loop through string
print("Characters in string:")
for ch in s:
    print(ch, end=" ")

print()

# Check substring
print("Is 'Hello' in string?", "Hello" in s)

# String comparison
s4 = "hello world"
print("Compare s and s4:", s == s4)

# Formatting
name = "Joshi"
age = 20
print("Formatted string: Name is {} and age is {}".format(name, age))