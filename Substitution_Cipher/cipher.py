import string

dict={}
data=""
file=open('demo1.txt','w')
file2=open('demo.txt')

for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
str=file2.read()
print("Original text in the file: ",str)

with open('demo.txt') as f:
    while True:
        d=f.read(1)
        if not d:
            print("cipher text: ",data)
            print("End of file")
            break
        if d in dict:
            data+=dict[d]
        else:
            data+=d
    file.write(data)
    
file.close()
    
        
