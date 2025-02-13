import datetime
import random

birthday=[]

i=0
while(i<50):
    year=random.randint(1875,2017)
    month=random.randint(1,12)
    if(year%4==0 and year%100!=0 or year%400==0):
        leap=1
    else:
        leap=0
    if(month==2 and leap==1):
        day=random.randint(1,29)
    elif(month==2 and leap==0):
        day=random.randint(1,28)
    elif(month%2==0 and month>8):
        day=random.randint(1,31)
    elif(month==7 or month==8):
        day=random.randint(1,31)
    elif(month%2!=0 and month<7):
        day=random.randint(1,31)
    else:
        day=random.randint(1,30)
    i=i+1

    dd=datetime.date(year,month,day)
    day_of_year=dd.timetuple().tm_yday
    birthday.append(day_of_year)

birthday.sort()
    
i=0
while(i<50):
    print(birthday[i])
    i=i+1
