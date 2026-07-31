#find second largest number in list
list1=[10,20,34,56,77,99]
num=max(list1)
print(num)
list2 =[]
for i in list1:
    if (i< num):
       list2.append(i)
       print(list2)
print("second largest element is:" ,max(list2))