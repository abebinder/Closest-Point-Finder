import random, math
import matplotlib.pyplot as plt

random.seed(10)

def solveClosestPoints(l):
    random.shuffle(l)
    delta=distance(l[0],l[1])
    top_pair=(0,1)
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
                        top_pair=(i,j)
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
    for i in range(n):
        a=random.random()
        b=random.random()
        items_list.append((a,b))
    return (items_list)

def visualize(items_list):
    N = len(items_list)
    datax = [item[0] for item in items_list]
    datay = [item[1] for item in items_list]

    #print data[:, 0]
    #print data
    labels = ['{0}'.format(i) for i in range(N)]

    plt.subplots_adjust(bottom = 0.1)
    plt.scatter(
        datax, datay, #data[:, 0], data[:, 1],
        cmap=plt.get_cmap('Spectral'))

    for label, x, y in zip(labels, datax, datay):
        plt.annotate(
            label,
            xy=(x, y), xytext=(-10, 20),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0')
        )

    plt.show()

if __name__ == '__main__':
    l=randominputgenerator(12)
    print(solveClosestPoints(l))
    visualize(l)
