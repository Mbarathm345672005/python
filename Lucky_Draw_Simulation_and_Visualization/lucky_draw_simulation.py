import random
import matplotlib.pyplot as plt

account=0
x=[]
y=[]
for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    if bet==lucky_draw:
        account=account+900-100
    else:
        account-=100
    y.append(account)

print("The amount has after the duration: ",account)
plt.plot(x,y)
plt.xlabel("days of the year")
plt.ylabel("amount has according to the each bet per day")
plt.show()
