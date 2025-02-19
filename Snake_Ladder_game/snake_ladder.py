import random
from PIL import Image

def show_image():
    img=Image.open('sl.png')
    img.show()

def check_ladder(points):
    if (points==2):
        print("ladder")
        return 38
    elif (points==9):
        print("ladder")
        return 14
    elif (points ==15):
        print("ladder")
        return 82
    elif (points ==16):
        print("ladder")
        return 54
    elif (points ==50):
        print("ladder")
        return 91
    elif (points==74):
        print("ladder")
        return 87
    else:
        return points

def check_snake(points):
    if (points==18):
        print("snake")
        return 6
    elif(points==29):
        print("snake")
        return 7
    elif(points==61):
        print("snake")
        return 16
    elif(points==72):
        print("snake")
        return 47
    elif(points==96):
        print("snake")
        return 76
    else:
        return points

def is_reached(points):
    if points==100:
        return True
    else:
        return False
   
def play():
    p1=input("Enter the player 1 name: ")
    p2=input("Enter the player 2 name: ")
    pp1=0
    pp2=0
    turn=0
    end=100

    while(1):
        if turn%2==0:
            print("player 1 ",p1," turn")
            c=int(input("Continue game enter 1 or for exit enter 0: "))
            if c==0:
                print("player 1:",pp1)
                print("player 2:",pp2)
                print("Thank u for playing...")
                break
            dice=random.randint(1,6)
            print("dice rolled and gives: ",dice)
            pp1+=dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1>end:
                pp1=100
            print("point is",pp1)    

            if is_reached(pp1):
                print("Player one ",p1," ,won")
                break

        else:
            print("player 2 ",p2," turn")
            c=int(input("Continue game enter 1 or for exit enter 0: " ))
            if c==0:
                print("player 1:",pp1)
                print("player 2:",pp2)
                print("Thank u for playing...")
                break
            dice=random.randint(1,6)
            print("dice rolled and gives: ",dice)
            pp2+=dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2>end:
                pp2=100
            print("point is",pp2)
            if is_reached(pp2):
                print("Player two ",p2," ,won")
                break
        turn+=1

show_image()
play()
        
