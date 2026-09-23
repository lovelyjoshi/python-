#find smallest element in list
numbers = [10, 25, 7, 45, 18]

smallest = numbers[0]

for x in numbers:
    if x < smallest:
        smallest = x

print(smallest)