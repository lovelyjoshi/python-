#creation of sets
my_set={1,2,3,4,5}
print(my_set)

#using constructor(change list into set)
my_set1=set([2,4,6,8])
print(my_set1)

#empty set
empty_set=set()
print(empty_set)

#set operations(only two operations are performrd on set add or remove)
my_set.add(6)#add()
print(my_set)
my_set.remove(6)#remove()
print(my_set)
my_set.discard(7)#discard
print(my_set)

#set methods
#union(combines elements from two sets)(set_a|set_b)
set_a={2,4,6,8}
set_b={2,3,4,5}
union_set=set_a .union( set_b)
print(union_set)

#difference(element presnt in first set but not in second)(set_a-set_b)
difference_set=set_a.difference(set_b)
print(difference_set)

#symmetric difference(do not give common elements)(set_a^set_b)
sym_diff = set_a.symmetric_difference(set_b)
print(sym_diff)

#intersection(common element)(set_a&set_b)
intersection_set = set_a.intersection(set_b)
print(intersection_set)

#for loop
for i in set_a:
    print(i)

#set comphenrension
square={x**2 for x in range(1,6)}
print(square)