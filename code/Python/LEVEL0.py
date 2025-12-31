# LEVEL 0 Absolute Beginner (Syntax & Thinking)
# Goal: Get comfortable with Python syntax and basic logic.

# 1. Take input: name, age. Print: Hi Name, you’ll be age next year (age+1)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

agePlus = age + 1

print(f"Print: Hi {name}, you’ll be {agePlus} next year")

# 2. Take two numbers as input and print their sum.

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

sum = num1 + num2
print(sum)

# 3. Check whether a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("It's positive")
elif num < 0:
    print("It's negative")
elif num == 0:
    print("Number is equal to zero")

# 4. Convert Celsius to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 5. Find whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("It's Even")
elif num % 2 == 1:
    print("It's Odd")

# 6. Print numbers from 1 to 100.

# Using for loop

for i in range(1 ,101):
    print(i)

# Using while loop

i = 1

while i <= 100:
    print(i)
    i += 1

# 7. Print only even numbers between 1 and 50.

for i in range(0, 51):
    if i % 2 == 0:
        print(i)

# 8. Calculate the square and cube of a number.

n = float(input("Enter a number: "))

square = n ** 2
cube = n ** 3

print("Square:", square)
print("Cube:", cube)

# 9. Take a character and check if it’s a vowel.

vowels = {"a", "e", "i", "o", "u"}
ch = input("Enter a character: ").strip().lower()

if len(ch) == 1 and ch in vowels:
    print("It's a vowel")
else:
    print("It's not a vowel")

# 10. Simple calculator using if/elif.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
