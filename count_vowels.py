s="Hello World"
vowels="aeiouAEIOU"
v=0 #vowels count
c=0 #consonant count
for ch in s:
    if ch.isalpha():
      if ch in vowels:
        v+=1
      else:
        c+=1
result={"Vowels": v,"consonants" :c}
print(result)        
