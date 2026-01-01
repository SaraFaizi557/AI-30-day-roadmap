# LEVEL 2 Lists, Tuples, Sets, Dictionaries
# Goal: Work with collections properly.

# 1. Find max and min in a list (without built-ins).

# nums = [10, 25, 3, 99, 45]

# max_val = nums[0]
# min_val = nums[0]

# for num in nums:
#     if num > max_val:
#         max_val = num
#     elif num < min_val:
#         min_val = num

# print("Max_Value: ", max_val)
# print("Min_Value: ", min_val)

# 2. Remove duplicates from a list.

# nums = [23, 12, 4, 12, 34, 4, 23, 54]
# unique = list(set(nums))
# print(unique)

# 3. Sort a list manually (bubble sort).

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         swapped = False

#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True

#         if not swapped:
#             break

#     return arr

# arr = [4, 6, 2, 1, 3, 7, 9, 8 ]    
# print(bubble_sort(arr))

# 4. Merge two lists.

# a = [1, 2, 3]
# b = [4, 5, 6]

# merged = a + b
# print(merged)

# 5. Find common elements in two lists.

# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]

# common = list(set(a) & set(b))
# print(common)

# 6. Count frequency of elements using a dictionary.

nums = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for x in nums:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)
