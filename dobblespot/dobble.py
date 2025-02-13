import random
import string

symbols=[]
symbols=list(string.ascii_letters)
cards1=[0]*5
cards2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
samesymbols=random.choice(symbols)
symbols.remove(samesymbols)

if(pos1==pos2):
    cards1[pos1]=samesymbols
    cards2[pos2]=samesymbols
else:
    cards1[pos1]=samesymbols
    cards2[pos2]=samesymbols
    cards1[pos2]=random.choice(symbols)
    symbols.remove(cards1[pos2])
    cards2[pos1]=random.choice(symbols)
    symbols.remove(cards2[pos1])

i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        alphabet=random.choice(symbols)
        cards1[i]=alphabet
        symbols.remove(alphabet)
        alphabet1=random.choice(symbols)
        cards2[i]=alphabet1
        symbols.remove(alphabet1)
        i=i+1
print(cards1)
print(cards2)
