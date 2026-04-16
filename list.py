# Create list
lst = [10, 20, 30, 40]
print("Original List:", lst)

# Accessing elements
print("First element:", lst[0])
print("Last element:", lst[-1])

# Slicing
print("Sliced (1:3):", lst[1:3])
print("Reversed list:", lst[::-1])

# Adding elements
lst.append(50)
print("After append:", lst)

lst.extend([60, 70])
print("After extend:", lst)

lst.insert(1, 15)
print("After insert at index 1:", lst)

# Removing elements
lst.remove(15)
print("After remove 15:", lst)

lst.pop()
print("After pop:", lst)

lst.pop(2)
print("After pop index 2:", lst)

# Searching
print("Index of 30:", lst.index(30))
print("Count of 20:", lst.count(20))
print("Is 40 present?", 40 in lst)

# Sorting & reversing
lst.sort()
print("Sorted list:", lst)

lst.sort(reverse=True)
print("Descending order:", lst)

lst.reverse()
print("Reversed again:", lst)

# Copy list
new_lst = lst.copy()
print("Copied list:", new_lst)

# Length
print("Length of list:", len(lst))

# Looping
print("Elements using loop:")
for i in lst:
    print(i, end=" ")

print()

# List concatenation
lst2 = [100, 200]
print("Concatenated list:", lst + lst2)

# Repetition
print("Repeated list:", lst * 2)

# List comprehension
squares = [x*x for x in range(5)]
print("Squares using comprehension:", squares)