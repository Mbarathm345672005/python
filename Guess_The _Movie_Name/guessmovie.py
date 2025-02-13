import random

movies=['goat','vikram vedha','leo','avengers','captain america','iron man','spider man','mission','f9','hulk','thor']

def create_qn(movie):
    l=len(movie)
    mov=list(movie)
    temp=[]
    for i in range(l):
        if ( mov[i]==' '):
            temp.append(' ')
        else:
            temp.append("*")
    m="".join(str(x) for x in temp)
    return m

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True

def unlock(modified,picked,letter):
    modlist=list(modified)
    picklist=list(picked)
    temp=[]
    l=len(picked)
    for i in range(l):
        if (picklist[i]==' ' or picklist[i]==letter):
            temp.append(picklist[i])
        else:
            if (modlist[i]=="*"):
                temp.append(modlist[i])
            else:
                temp.append(modlist[i])
    mod_new=''.join(str(x) for x in temp)
    return mod_new
    
def play():
    pname1=input("Enter your name player1")
    pname2=input("Enter your name player2")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            picked=random.choice(movies)
            qn=create_qn(picked)
            modified_qn=qn
            print(qn)
            not_said=True
            while not_said:
                letter=input("Enter ur letter player1")
                if( is_present(letter,picked)):
                    modified_qn=unlock(modified_qn,picked,letter)
                    print(modified_qn)
                    d=int(input("player1, do u know full answer then enter 1 or enter 0 for unlock the letters"))
                    if(d==1):
                        ans=input("Enter ur answer:")
                        if( ans==picked):
                            print("Your right")
                            pp1=pp1+1
                            print(pname1, ", point is ",pp1)
                            not_said=False
                        else:
                            print("Wrong answer ",pname1,"try again")
                else:
                    print(letter,"not found")
            c=int(input("press 1 to contine or press 0 to exit:"))
            if c==0:
                print(pname1, "your score is", pp1)
                print(pname2, "your score is", pp2)
                print("Thanks for playing \n have a nice day")
                willing=False
        if turn%2!=0:
            picked=random.choice(movies)
            qn=create_qn(picked)
            modified_qn=qn
            print(qn)
            not_said=True
            while not_said:
                letter=input("Enter ur letter player2")
                if( is_present(letter,picked)):
                    modified_qn=unlock(modified_qn,picked,letter)
                    print(modified_qn)
                    d=int(input("player2, do u know full answer then enter 1 or enter 0 for unlock the letters"))
                    if(d==1):
                        ans=input("Enter ur answer:")
                        if( ans==picked):
                            print("Your right")
                            pp2=pp2+1
                            print(pname2, ", point is ",pp2)
                            not_said=False
                        else:
                            print("Wrong answer ",pname2,"try again")
                else:
                    print(letter,"not found")
            c=int(input("press 1 to contine or press 0 to exit:"))
            if c==0:
                print(pname1, "your score is", pp1)
                print(pname2, "your score is", pp2)
                print("Thanks for playing \n have a nice day")
                willing=False
        turn=turn+1

play()
