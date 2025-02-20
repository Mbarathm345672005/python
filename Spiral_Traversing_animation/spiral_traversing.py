import turtle
import random

turtle.bgcolor("black")
tur=turtle.Turtle()
wid=5
h=7
dist=25
tur.setpos(-250,250)
tur.penup()   
list_col=["blue","green","red","pink","White"]

def spiral(m,n):
    k=0
    l=0
    f=0
    tur.color("white")

    while(k<m and l<n):
        if(f==1):
            tur.right(90)
        for i in range(l,n):
            tur.dot()
            tur.forward(dist)

        k+=1
        f=1
        tur.right(90)
        col=random.randint(0,3)
        tur.color(list_col[col])

        for i in range(k,m):
            tur.dot()
            tur.forward(dist)

        n-=1
        tur.right(90)
        col=random.randint(0,3)
        tur.color(list_col[col])
        
        if(k<m):

            for i in range(n-1,l-1,-1):
                tur.dot()
                tur.forward(25)

            m-=1
        tur.right(90)
        col=random.randint(0,3)
        tur.color(list_col[col])

        if(l<n):

            for i in range(m-1,k-1,-1):
                tur.dot()
                tur.forward(25)

            l+=1
        
spiral(20,20)
