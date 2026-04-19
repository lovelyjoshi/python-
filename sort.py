numbers = list(map(int, input("Enter numbers: ").split()))

asc = sorted(numbers)
desc = sorted(numbers, reverse=True)

print("Ascending:", asc)
print("Descending:", desc)