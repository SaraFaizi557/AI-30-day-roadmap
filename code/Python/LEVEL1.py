# LEVEL 1 Loops & Strings
# Goal: Control flow + text handling.

# 1. Reverse a string.

s = "hello"
reverse_s = s[::-1]
print(reverse_s)

# 2. Count vowels in a string.

s = input("Enter a string: ").lower()
vowels = "aeiou"

count = sum(1 for ch in s if ch in vowels)
print(count)

# 3. Check if a string is a palindrome.

def is_pelindrome(s):
    return s == s[::-1]

print(is_pelindrome(input("Enter a word: ")))

# 4. Print Fibonacci series up to n.

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)

# 5. Count digits in a number.

def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

    
print(count_digits(154))

# 6. Sum of digits of a number.

n = int(input("Enter number: "))
n = abs(n)
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print("Sum of digits:", total)

# 7. Print a right-angle triangle pattern using *.

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print("*" * i)

# 8. Find the largest number in a list.

nums = [3, 5, 23, 9, 4, 15, 34]

print(max(nums))

# 9. Remove spaces from a string.

str = input("Enter a word: ")

result = str.replace(" ", "")
print(result)

# 10. Count how many times a character appears.

s = input("Enter a word: ")
ch = input("Enter a char: ")

count = s.count(ch)
print(count)