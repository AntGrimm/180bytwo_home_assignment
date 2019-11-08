# Functions are commented out at the bottom, remove comment to run each function

import itertools


# Removing a character in a loop and checking word against dictionary
def check_super_word(check_str, dictionary):
    for i in range(0, len(check_str)):  # Removing each character in loop
        new_str = ''.join([check_str[j] for j in range(len(check_str)) if j != i])

        if new_str in dictionary:  # Checking if each iteration of word is in the dictionary
            return True
        else:
            print(check_str + " is not a super word")


# Combining integers and interlacing strings
def combine_integers(a, b):
    c = ''.join(map(''.join, itertools.zip_longest(str(a), str(b), fillvalue="")))
    return int(c)


# Python program for implementation of MergeSort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left = arr[:mid]  # Dividing the array elements
        right = arr[mid:]  # into 2 halves

        merge_sort(left)  # Sorting the first half
        merge_sort(right)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# Remove below comment to run function
# print(check_super_word("print", ["pint", "pit", "hat"]))
# print(combine_integers(123, 456))
print(merge_sort([1, 2, 6, 5, 4, 7, 8]))