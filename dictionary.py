# Create dictionary
d = {"name": "Ram", "age": 20, "course": "BCA"}
print("Original Dictionary:", d)

# Access elements
print("Name:", d["name"])

# Add element
d["city"] = "Delhi"
print("After adding city:", d)

# Update element
d["age"] = 21
print("After updating age:", d)

# Delete element
del d["course"]
print("After deleting course:", d)

# Pop element
d.pop("city")
print("After pop city:", d)

# Length of dictionary
print("Length:", len(d))

# Keys, Values, Items
print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())

# Check key existence
print("Is 'name' present?", "name" in d)

# Traverse dictionary
print("Dictionary elements:")
for key, value in d.items():
    print(key, ":", value)

# Copy dictionary
d2 = d.copy()
print("Copied Dictionary:", d2)

# Merge dictionaries
d3 = {"marks": 90}
d.update(d3)
print("After merging:", d)

# Clear dictionary
d.clear()
print("After clear:", d)