def tickets(people):
    #to determine if clerk can sell tickets to entire queue, given each costs 25
    #he has no change in the begining
    n25 = n50 = 0
    for e in people:
        if   e==25            : n25+=1
        elif e==50            : n25-=1; n50+=1
        elif e==100 and n50>0 : n25-=1; n50-=1
        elif e==100 and n50==0: n25-=3
        if n25<0 or n50<0:
            return 'NO'
    return 'YES'