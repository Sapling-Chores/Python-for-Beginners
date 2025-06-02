# Conditional Statements (if, elif, else) and Logic

# Basic if statement
number = 10
if number > 6:
    print(f"{number} is greater than 6")  # 10 is greater than 6

# if-else statement
value = 7
if value > 10:
    print(f"{value} is greater than 10")
else:
    print(f"{value} is smaller than 10")  # 7 is smaller than 10

# if-elif-else ladder
score = 78
if score <= 50:
    print(f"{score} is smaller than or equal to 50")
elif 100 > score > 50:
    print(f"{score} is between 50 and 100")  # 78 is between 50 and 100
else:
    print(f"{score} is greater than 100")

# Simple user input comparison
animal_guess = input("Which is the national animal of India? ").strip().lower()
if animal_guess == "tiger":
    print(True)
else:
    print(False)

# Using 'pass' (placeholder)
test_value = 10
if test_value >= 10:
    pass  # does nothing

# Logical Operators: and, or, not
age = 19
citizenship = "american"
if age >= 18 and citizenship == "indian":
    print("You are allowed to vote")
else:
    print("You are not allowed to vote")  # You are not allowed to vote

humidity = int(input("Humidity: ").strip())
temperature = int(input("Temperature: ").strip())

if humidity >= 45 or temperature > 37:
    print("Today is very 'hot'\nGet into light clothes")
elif humidity < 35 and temperature < 30:
    print("Today is cold\nWear warm clothes")
else:
    print("The weather is perfect today\nEnjoy your day")

# Combined logical expression
user_input = int(input("Enter a valid number: "))
if (user_input > 10 and user_input < 20) or user_input == 100:
    print("Great, that's a valid number")
else:
    print("Oops, that's not a valid number")

# Truthy and Falsy Checks
non_empty_list = ["item"]
if non_empty_list:
    print("The list is not empty")  # The list is not empty
else:
    print("The list is empty")

outer_box = [non_empty_list]
if not outer_box:
    print("Outer box is empty")
else:
    print("Outer box is not empty")  # Outer box is not empty

empty_list = []
if empty_list:
    print("List is not empty")
else:
    print("List is empty")  # List is empty

# Logical behavior of 'and' / 'or'
print(9 and 0)            # 0
print(9 or 0)             # 9
print(9 and 8)            # 8
print(0 and 9)            # 0
print(0 and 9 and 2 and 10)  # 0
print(None and 0 and False and 9)  # None
print(0 and None and 9 and False)  # 0
print(False or None or 6)         # 6
print(0 and None or 9)            # 9

# Comparing Lists/Tuples
print([1, 2, 3] == [1, 2, 3])      # True
print([1, 2] > [1, 3])             # False
print([1, 2] > [1, 1, 3])          # True
print([1, 2, 3] < [1, 1, 4])       # False
print([1, 2, 3] > [1, 3, 2])       # False
print([1, 2, 3] == [1, 2, 9])      # False
print([1, 2, 3] != [1, 2, 3])      # False

