player1={0:'Rock',1:'Paper',2:'Scissor'}
player2={0:'Paper',1:'Scissor',2:'Rock'}
pp1=0
pp2=0

def rock_paper_scissor(num1,num2,bit1,bit2):
    global pp1,pp2
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if (player1[p1]==player2[p2]):
        print("Draw")
    elif(player1[p1]=="Rock" and player2[p2]=="Paper"):
        print("player 2 won")
        pp2=pp2+1
    elif(player1[p1]=="Rock" and player2[p2]=="Scissor"):
        print("Player 1 won")
        pp1+=1
    elif(player1[p1]=="Paper" and player2[p2]=="Scissor"):
        print("Player 2 won")
        pp2+=1
    elif(player1[p1]=="Paper" and player2[p2]=="Rock"):
        print("Player 1 won")
        pp1+=1
    elif(player1[p1]=="Scissor" and player2[p2]=="Rock"):
        print("Player 2 won")
        pp2+=1
    elif(player1[p1]=="Scissor" and player2[p2]=="Paper"):
        print("Player 1 won")
        pp1+=1

while(1):
    num1=input("Player one,Enter ur choice:")
    num2=input("Player two,Enter ur choice:")
    bit1=int(input("Player one, Enter ur secret code:"))
    bit2=int(input("Player two, Enter ur secret code:"))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do u want to continue (y/n)?")
    if(ch=="n"):
        print("player one point",pp1)
        print("player two point",pp2)
        if(pp1>pp2):
            print("player one won")
        else:
            print("player two won")
        break
    
