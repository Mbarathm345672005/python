import random

doors=[0]*3
goatdoors=[0]*2
swap=0
dont_swap=0
j=0

while(j<10):
    x=random.randint(0,2)
    doors[x]="bmw"
    for i in range(0,3):
        if (i==x):
            continue
        else:
            doors[i]="goat"
            goatdoors.append(i)
    inp=int(input("Enter ur choice:"))
    goat=random.choice(goatdoors)
    while(inp==goat):
        goat=random.choice(goatdoors)
    ch=input("do u want to swap('Y') or not")
    if (ch=='Y'):
        if (doors[inp]=="goat"):
            print("your correct")
            swap=swap+1
        else:
            print("Your wrong")
    else:
        if(doors[inp]=="bmw"):
            print("Your right")
            dont_swap+=1
        else:
            print("your wrong")
    j+=1

print("swap:", swap)
print("dont swapt:", dont_swap)
        
