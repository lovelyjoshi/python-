text=input("enter a string")
if text ==text[::-1]:
    print("palindrome")
else:
    print("not a palindrome")    
    
#integer program to calculate palindrome
num=int(input("enter a number:"))
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev+10+digit
    temp=temp//10

if num==rev:
    print("palindrome number")
else:
    print("not a palindrome number")            