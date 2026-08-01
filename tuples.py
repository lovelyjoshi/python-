#creating tuple(tuple is immutable)
#using parenthesis
colors=("red","green","blue")
numbers=(1,2,3,4)
mixed=(1,"red",3.14,True)
nested=(1,[1,2],(1,2,3))
print(colors)
print(numbers)
print(mixed)
print(nested)

#without parenthesis
my_tuple=1,2,3
print(my_tuple)

#using the tuple constructor
new_tuple=tuple((1,2,3,4))
print(new_tuple)

#creating a tuple from list
list_items=[1,3,4,5]
tuple_items=tuple(list_items)
print(tuple_items)

#accessing tuple elements(using index)
fruits=("apple","banana","orange")
print(fruits[0])
print(fruits[-1])

#slicing in tuple
#tuple_name[start:stop:step]
print(fruits[1:4])
print(fruits[::2])
print(fruits[::-1])
print(fruits[-4:-1])