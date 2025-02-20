#Finding an anagram by using ASCII values

str1=input("Enter the string1: ")
str2=input("Enter the string2: ")
count1=0
i=0
while(i<len(str1)):
    count1+=ord(str1[i])
    i+=1
count2=0
i=0
print("Sum of ascii value of str1: ",count1)
while(i<len(str2)):
    count2+=ord(str2[i])
    i+=1
print("Sum of ascii value of str2: ",count2)

if(count1==count2):
    print("Provided two strings are satisfy an anagram")
else:
    print("Not an anagram")
