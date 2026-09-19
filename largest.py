#find largest element in list
numbers = [10, 25, 7, 45, 18]

largest = numbers[0]

for x in numbers:
    if x > largest:
        largest = x

print(largest)