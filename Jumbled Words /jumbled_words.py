import random
def choose():
    words=['rainbow','car','aeroplane','rocket','apple','lamborghini','flower','man','alpha','emperor','science','python']
    pick=random.choice(words)
    return pick
def jumble(word):
    jumb="".join(random.sample(word,len(word)))
    return jumb
def thank(pp1,pp2):
    print("result")
    print ("Player 1 point is :", pp1)
    print("Player 2 point is", pp2)
    if(pp1>pp2):
        print("so player 1 won")
    else:
        print("so player 2 won")
    
def play():
    pn1=input("Enter the player 1 name:")
    pn2=input("Enter the player 2 name:");
    pp1=0
    pp2=0
    turn=0
    while(1):
        
        c=1
        if(turn%2==0):
            pick=choose()
            qn=jumble(pick)
            print("player 1 Question is '",qn,"'")
            ans=input ("player1 answer :")
            if(pick==ans):
                print ("Your correct")
                pp1=pp1+1
                print ("p1 point is",pp1)
            else:
                print("sorry ur wrong and the correct answer '", pick,"'")
        else:
            pick=choose()
            qn=jumble(pick)
            print("player 2 Question is '",qn,"'")
            ans=input ("player2 answer :")
            if(pick==ans):
                print ("Your correct")
                pp2=pp2+1
                print ("p2 point is",pp2)
                print("you want to end the game means enter 0 or enter any keys")
                c=int(input("Enter key:"))
                if(c==0):
                    thank(pp1,pp2)
                    break
            else:
                print("sorry ur wrong and the correct answer '", pick,"'")
                print("you want to end the game means enter 0 or enter any keys")
                c=int(input("Enter key:"))
                if(c==0):
                    thank(pp1,pp2)
                    break 
        turn+=1
        
play()
