import random, math
random.seed(2)

def solveClosestPoints(l):
    random.shuffle(l)
    delta=distance(l[0],l[1])
    top_pair=(l[0],l[1])
    if(delta==0.0):
        return(delta,top_pair)

    dict=MakeDictionary(l,delta,0)
    for i in range(0,len(l)):
        cell=whatCellAmIIn(l[i],delta)
        for s in range(cell[0]-2, cell[0]+3):
            for t in range(cell[1]-2, cell[1]+3):
                j_list=dict.get((s,t))
                if(j_list==None):
                    continue
                changed=False
                for j in j_list:
                    dist=distance(l[i],l[j])
                    if(dist<delta):
                        changed=True
                        delta=dist
                        top_pair=(l[i],l[j])
                        if(delta==0.0):
                            return(delta,top_pair)
                if(changed):
                    dict=MakeDictionary(l,delta,i)
                    cell=whatCellAmIIn(l[i], delta)


        if(cell in dict):
            dict[cell].append(i)
        else:
            dict[cell]=[i]
    return (delta,top_pair)


def MakeDictionary(l, delta, i):
    dict={}
    for j in range(0,i):
        p=l[j]
        a=whatCellAmIIn(p,delta)
        if(a in dict):
            dict[a].append(j)
        else:
            dict[a]=[j]
    return dict


def whatCellAmIIn(p,delta):
    x=int(math.floor(p[0]/(delta/2)))
    y=int(math.floor(p[1]/(delta/2)))
    return (x,y)



def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)



def randominputgenerator(n):
    items_list=[]
    for i in range(1,n+1):
        a=random.randint(1,n**2)
        b=random.randint(1,n**2)
        items_list.append((a,b))
    return (items_list)

l=[(4,3),(1,1),(2,2),(4,4),(4,4)]
for i in range(0,5):
    l=randominputgenerator(4)
    print(l)
    print(solveClosestPoints(l))
