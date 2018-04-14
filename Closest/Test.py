import Closest
import time
import random
random.seed(1)
import matplotlib.pyplot as plt



def randominputgenerator(n):
    items_list=[]
    for i in range(1,n+1):
        a=random.randint(1,n**2)
        b=random.randint(1,n**2)
        items_list.append((a,b))
    return (items_list)




min_i  = 10 #33, 70
max_i  = 3000 #50, 90
n_base = 1.05
randomns=[]
randomtimes=[]
minn=4000
maxn=120000


for i in range( min_i, max_i ):
    n = int( n_base ** i )
    if(n>minn and n<maxn):
        randomns.append(n)
        items=randominputgenerator(n)
        t1=time.time()
        Closest.solveClosestPoints(items)
        t2=time.time()
        randomtimes.append(t2-t1)
        print(n)






plt.plot( randomns, randomtimes )
plt.xlabel('input size')
plt.ylabel('time (s)')
plt.title('Random Case Blue \n All Item weights> Knapsack Weight Green')
plt.grid(True)
plt.show()
