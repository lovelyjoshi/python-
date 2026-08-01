fruits=["apple","banana","orange","cherry"]
print(fruits)

#appends(adds a single element to the end of list)
fruits.append("grapes")
print(fruits)

#extend(adds multiple elements to the end of list)
fruits.extend(["lichi","peach"])
print(fruits)

#insert(insert element on a specified position)
fruits.insert(1,"guava")
print(fruits)

#remove(remove first occurance of specified element)
fruits.remove("apple")
print(fruits)

#pop(remove and return an element )
removed= fruits.pop(3)
print(fruits)
print(removed)

#index(used to find the position of the first occurance of specified element)
x= fruits.index("banana")
print(x)

#count(returns the no of occurance of specified element)
y= fruits.count("orange")
print(y)

#sort(arrange the elements of a list in ascending (default)or decending method)
fruits.sort()
print(fruits)
#sort in decending order
fruits.sort(reverse = True)
print(fruits)

#copy(used to create a copy of list)
new_list=fruits.copy()
print(new_list)

#clear(remove all elements from list)
fruits.clear()
print(fruits)

#flatten_list
numbers1=[[1,2,3],[4,5]]
flat_list=[item for sublist in numbers1 for item in sublist]
print(flat_list)