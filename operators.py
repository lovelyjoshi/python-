a = 10
b = 5

# Arithmetic Operators
print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

# Comparison Operators
print("\nComparison Operators:")
print("a > b =", a > b)
print("a < b =", a < b)
print("a == b =", a == b)

# Logical Operators
print("\nLogical Operators:")
print("(a > b and b > 0) =", (a > b and b > 0))
print("(a < b or b > 0) =", (a < b or b > 0))
print("not(a > b) =", not(a > b))

# Assignment Operators
print("\nAssignment Operators:")
c = a
c += b
print("c += b =", c)

# Membership Operators
lst = [1, 2, 3]
print("\nMembership Operators:")
print("2 in list =", 2 in lst)

# Identity Operators
x = [1, 2]
y = x
print("\nIdentity Operators:")
print("x is y =", x is y)