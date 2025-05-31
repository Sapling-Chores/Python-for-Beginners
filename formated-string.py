from datetime import datetime

name = "Alex"
age = 18
grade = "11th"
pi = 3.141596253

print(f"My name is {name} , I am {age} years old and I am in {grade} grade ")
print(f"My name is {name} , I will be {age + 1} years old next year")
print(f"{pi:.3f}")  # Upto 3 digit of decimal
print(f"{pi:.5f}")
print(f"{pi:10.3f}") #      3.14(10 characters)

user = {'name': 'Sara', 'id': 12}
print(f"User: {user['name']} , ID: {user['id']}")

data = {"username": ["saplingg","z3nx","Not domst","NotSarfaraz"],"number":[86,89,90,91]}
print(f"{data["username"]} , {data["number"]}")
print(f"{data["username"]}")

dog_name = "kutta"
print(f"{dog_name:>10}") # left align
print(f'{dog_name:<10}') #right align
print(f"{dog_name:^10}") #centered same as center in string

bigNumber = 1234567890
print(f"{bigNumber:,}") # Thousands seperater
print(f"{pi:.2%}") # creates it as percentage

#Extrass

now = datetime.now()
print(f"Today is {now:%A, %B %d, %Y}")  # e.g., Monday, May 29, 2025
