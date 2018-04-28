import matplotlib.pyplot as plt
import closest_points
import time
import random
random.seed(4)


# test for correctness
P = closest_points.generate_points(12)
print( closest_points.solve(P) )
closest_points.visualize(P)

exit() # remove this if you wanna see time complexity graph

# test time complexity

ns = []
times = []
min_i  = 45
max_i  = 87
n_base = 1.15

for i in range( min_i, max_i ):
    n = int( n_base ** i )
    ns.append( n )

    points = closest_points.generate_points( n )
    t1 = time.time()
    ( distance, pair ) = closest_points.solve( points )
    t2 = time.time()
    td = t2 - t1
    print( "%d %d %s" % ( i, n, td ) )
    times.append( td )

plt.plot( ns, times )



plt.xlabel('input size')
plt.ylabel('time (s)')
plt.title( 'Closest Points solver' )
plt.grid(True)
plt.savefig( "closest_points.png")
plt.show()
