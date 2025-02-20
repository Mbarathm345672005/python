#Finding whether two strings are an anagram by using sorted()

str1=input("Enter the string1: ")
str2=input("Enter the string2: ")
a=sorted(str1)
b=sorted(str2)
print(a)
print(b)
if(a==b):
    print("Provided two strings are satisfy an anagram")
else:
    print("Not an anagram")
    
