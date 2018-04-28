import math
import random
import matplotlib.pyplot as plt
# random.seed(100)


def solve(P):
    closest_pair = (0, 1)
    delta = get_distance(P[0], P[1])
    if(delta == 0.0):
        return ( delta, closest_pair )
    subsquare_to_points_mapping = {}
    subsquare_to_points_mapping[ get_subsquare_of_point( P[0], delta ) ] = 0
    subsquare_to_points_mapping[ get_subsquare_of_point( P[1], delta ) ] = 1

    for i in range( 2, len(P) ):
        subsquare = get_subsquare_of_point( P[i], delta )

        new_closest_pair_found = False
        for s in range( subsquare[0]-2, subsquare[0]+3 ):

            for t in range( subsquare[1]-2, subsquare[1]+3 ):

                point_in_subsquare = subsquare_to_points_mapping.get( ( s, t ) )
                if( point_in_subsquare == None ): continue

                distance = get_distance( P[i], P[point_in_subsquare] )
                if( distance < delta ):
                    new_closest_pair_found = True
                    delta = distance
                    closest_pair = ( i,point_in_subsquare )
                    if(delta == 0.0):
                        return( delta, closest_pair )

        if new_closest_pair_found:
            subsquare_to_points_mapping = make_dictionairy( P, delta, i )
            subsquare = get_subsquare_of_point( P[i], delta )

        subsquare_to_points_mapping[subsquare] = i

    return ( delta, closest_pair )


def make_dictionairy(P, delta, max_point_index):
    subsquare_to_points_mapping = {}

    for i in range(0, max_point_index):
        subsquare = get_subsquare_of_point( P[i], delta)
        subsquare_to_points_mapping[subsquare] = i

    return subsquare_to_points_mapping


def get_subsquare_of_point( point, delta ):
    s = int( math.floor( point[0]/(delta/2) ) )
    t = int( math.floor( point[1]/(delta/2) ) )
    return ( s, t )


def get_distance(p0, p1):
    return math.sqrt( (p0[0] - p1[0])**2 + (p0[1] - p1[1])**2 )


def visualize(items_list):
    N = len(items_list)
    datax = [item[0] for item in items_list]
    datay = [item[1] for item in items_list]
    labels = ['{0}'.format(i) for i in range(N)]

    plt.subplots_adjust(bottom = 0.1)
    plt.scatter(
        datax, datay,
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

def generate_points( n ):
    points = []
    for i in range(n):
        x = random.random()
        y = random.random()
        points.append( ( x, y ) )
    return points
