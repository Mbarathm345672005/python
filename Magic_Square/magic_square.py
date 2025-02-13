def magicSquare(n):
    magic=[]
    magic=[[0 for i in range(n)] for j in range(n)]
    i=n//2
    j=n-1
    count =1
    num=n*n
    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(i==-1):
                i=n-1
            if(j==n):
                j=0
        if ( magic[i][j]!=0):
            i=i+1
            j=j-2
            continue
        else:
            magic[i][j]=count
            count=count+1
        i=i-1
        j=j+1
    for i in range(n):
        for j in range(n):
            print( magic[i][j], end=" ")
        print()
    print("sum of the rows/ columns/ diagonal is: " ,(n*(n**2+1)/2))
n=int(input("Enter N:"))
magicSquare(n)
    
