# Python String Methods - Beginner's Showcase
# This script demonstrates various string methods, slicing, indexing, and escape characters.
# It includes both basic usage and slightly more advanced experiments.

# ---------------------------------------
# Sample Strings
# ---------------------------------------
text = "   Hello, my name is Alex, I am 18 and I am learning Python   " # Added space in the beginning and end.
text_simple = "hello my name is alex" # All in lower case.
text_upper = "HELLO MY NAME IS ALEX, HOW ARE YOU" # All in upper case
single_char = "h"
word = "hi"
word_start = "start"
space_str = " "
numeric_str = "12345"
bye_words = "Good", "Bye", "My", "Friend"

# ---------------------------------------
# Boolean String Checks
# ---------------------------------------
print("Boolean Checks:")
print(word_start.isalpha())   # True - only letters
print(numeric_str.isdigit())  # True - only digits
print(word_start.isalnum())   # True - letters and numbers only
print(space_str.isspace())    # True - only whitespace
print()

# ---------------------------------------
# Searching and Replacing
# ---------------------------------------
print("Searching & Replacing:")
print(text.find("Python"))    # returns index
print(text.find("Java"))      # -1 if not found
print(text.index("Python"))   # returns index
# print(text.index("Java"))   # Uncomment to see ValueError

print(text.replace("Alex", "Jamie"))  # replace substring
print()

# ---------------------------------------
# Case Modifiers
# ---------------------------------------
print("Case Modifiers:")
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())
print(text.swapcase())
print()

# ---------------------------------------
# Stripping and Centering
# ---------------------------------------
print("Whitespace & Centering:")
print(text.strip())                     # Removes outer whitespace
print(text.lstrip())                    # Left strip
print(text.rstrip())                    # Right strip
print(word.center(10, "!"))             # Center with padding
print(single_char.center(8, "|"))
print()

# ---------------------------------------
# Startswith & Endswith
# ---------------------------------------
print("Start/End Checks:")
print(word_start.startswith("s"))      # True
print(word_start.endswith("t"))        # True
print(word_start.endswith("r"))        # False
print()

# ---------------------------------------
# Split and Join
# ---------------------------------------
print("Splitting & Joining:")
print("a,b,c".split(","))              # Split into list
print("|".join(["good", "bye", "my friend"]))  # Join with separator
print(" ".join(bye_words))             # Join tuple of words
print()

# ---------------------------------------
# Count, zfill, and others
# ---------------------------------------
print("Count, zfill & Formatting:")
print("banana".count("a"))             # Count occurrences
print("42".zfill(5))                   # Pad with zeros: '00042'
print("ok".center(10, "-"))            # Centered with fill
print()

# ---------------------------------------
# Slicing & Indexing
# ---------------------------------------
print("Slicing & Indexing:")
sample = "Python is powerful"
print(sample[0])           # First char
print(sample[:])           # Full string
print(sample[-1])          # Last char
print(sample[1:4])         # Index 1 to 3
print(sample[::2])         # Every second char
print(sample[1::2])        # Every second char from index 1
print(sample[0:4:2])       # Index 0 to 3, step 2
print()

# ---------------------------------------
# Immutability
# ---------------------------------------
print("Immutability Demo:")
s = "hello"
print(s[0:])
s = "Hello"               # New string assigned (old string unchanged)
print(s[0:])
print()

# ---------------------------------------
# Escape Characters
# ---------------------------------------
print("Escape Characters:")
print("He said \"yes\".")      # Escaped double quote
print("Line1\nLine2")          # Newline
print("Tab\tSpace")            # Tab character
print("Backslash: \\")         # Backslash
print()

# ---------------------------------------
# Raw String
# ---------------------------------------
print("Raw Strings:")
print(r"C:\new\folder")        # Backslashes are not treated as escape characters


# Multiline String

print('''This is multi 
string and you can use's'
or "s" inverted comma like this one .       
      ''')


# Using in / not in operation

print("py" in "python")       # True
print("java" not in "python") # True

# Looping through string

for ch in "abc":
    print(ch)
