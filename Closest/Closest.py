import random, math
random.seed(1)
def solveClosestPoints(l):
    random.shuffle(l)
    print(l)
    delta=distance(l[0],l[1])
    print(delta)
    top_pair=(l[0],l[1])
    dict=MakeDictionary(l,delta,0)
    for i in range(0,len(l)):
        cell=whatCellAmIIn(l[i],delta)
        for s in range(cell[0]-2, cell[0]+3):
            if(s<0):
                continue
            for t in range(cell[1]-2, cell[1]+3):
                if(t<0):
                    continue
                try:
                    j_list=dict.get((s,t))
                    if(j_list==None):
                        raise(ZeroDivisionError)
                    for j in j_list:
                        dist=distance(l[i],l[j])
                        if(dist<delta):
                            delta=dist
                            top_pair=(l[i],l[j])
                            dict=MakeDictionary(l,delta,i)
                except:
                    pass

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


l=[(.2,.2),(.2,.3),(.5,.5),(.7,1),(1,5),(4,3)]

print(solveClosestPoints(l))
