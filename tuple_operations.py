#concatenation (join two or more tuples)
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple3=print(tuple1+tuple2) 

#repeatation(using * operator)
a=(tuple2)*3
print(a)

#checking for an item
print(2 in tuple1)

#using loops in tuple
#for loop
for i in tuple1:
    print(i)
#while loop in python
numbers=(1,3,6,8)
i=0
while i<len(numbers): 
    print(numbers[i])
    i+=1   

#built in methods
#count()
print(numbers.count(3))
#index()
print(numbers.index(3))

#tuple functions
number=(9,8,7,6,5,4)
print(len(number))
print(max(number))
print(min(number))
print(sum(number))
sorted_num=sorted(numbers)
print(sorted_num) #change in list
a= sorted(numbers)
numbers_sorted=tuple(a)
print(numbers_sorted)

#modifying tuple(first we change tuple into list then perform operation(modify) and then again change into tuple)
tuple_numbers=(44,55,77)
list_numbers=list(tuple_numbers)
print(list_numbers)
list_numbers[0]=100
print(list_numbers)
new_tuple1=tuple(list_numbers)
print(new_tuple1)

#packing and unpacking tuple
x="riya"
y="doctor"
z=32
pack_tuple=x,y,z 
print(pack_tuple)

#unpacking tuple
person = ("name","profession",45)
name,profession,age=person
print(name)
print(profession)
print(age)