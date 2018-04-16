import matplotlib.pyplot as plt
import closest_points
import time
import random
random.seed(1)



ns = []
times = []
min_i  = 45
max_i  = 87
n_base = 1.15

for i in range( min_i, max_i ):
    n = int( n_base ** i )
    ns.append( n )

    sum = 0
    for j in range(10):
        points = closest_point.generate_points( n )
        t1 = time.time()
        ( distance, pair ) = closest_points.solve( points )
        t2 = time.time()
        td = t2 - t1
        print( "%d %d %s" % ( i, n, td ) )
        sum += td
    times.append( sum/10 )

plt.plot( ns, times )



plt.xlabel('input size')
plt.ylabel('time (s)')
plt.title( 'Closest Points solver' )
plt.grid(True)
# plt.legend()
plt.savefig( "closest_points.png")
plt.show()
