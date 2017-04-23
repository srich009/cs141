import sys
from math import sqrt
import re
from operator import itemgetter

pointRE = re.compile("(-?\\d+.?\\d*)\\s(-?\\d+.?\\d*)")

def dist(p1, p2):
    return sqrt(pow((p1[0]-p2[0]),2) + pow((p1[1]-p2[1]),2))
#----------------------------------------------------------------------

#Brute force version of the nearest neighbor algorithm, O(n**2)
def brute_force_nearest_neighbor(points):
    min_distance = 0
    if len(points) < 2:
        return min_distance

    # initial distance of p1 and p2 
    min_distance = dist(points[0],points[1]) 
    
    # nested loops
    # point p, where p[0] = x, p[1] = y
    # i = p1, j = p2
    for i in range(0, len(points)-1):
        cur_i = points[i]
        for j in range(i+1, len(points)):
            cur_j = points[j] 
            cur_dist = dist(cur_i, cur_j)
            if cur_dist < min_distance:
                min_distance = cur_dist
    return min_distance
#----------------------------------------------------------------------

#Run the divide-and-conquor nearest neighbor 
def nearest_neighbor(points):
    x_pnt = sorted(points, key=itemgetter(0)) # points sorted by x
    y_pnt = sorted(points, key=itemgetter(1)) # points sorted by y
    # print x_pnt
    # print y_pnt
    return nearest_neighbor_recursion(x_pnt, y_pnt)
#----------------------------------------------------------------------

#Divide and conquer recurse part
def nearest_neighbor_recursion(x_pnt, y_pnt):
    min_distance = 0
    num_p = len(x_pnt)

    if num_p <= 3:
    	return brute_force_nearest_neighbor(x_pnt)
    else:
    	half = num_p/2			# half way
    	xpl = x_pnt[:half]		# x points left half
    	xpr = x_pnt[half:]		# x points right half

        med = xpl[-1]           # median point
        ypl, ypr = [], []       # y left half, y right half

        # sort points by y
        for pnt in y_pnt:
            if pnt[0] <= med[0]: 
                ypl.append(pnt) # add pnt y left half
            else:
                ypr.append(pnt) # add pnt y right half

        # print xpl
        # print xpr
        # print ypl
        # print ypr
        # print disr_l
        # print dist_r

        dist_l = nearest_neighbor_recursion(xpl, ypl)
        dist_r = nearest_neighbor_recursion(xpr, ypr)

        if dist_l < dist_r:
            dist_m = dist_l
        else: 
            dist_m = dist_r

        stp = [] # strip of points in the middle

        for pnt in y_pnt:
            if abs(pnt[0] - med[0]) < dist_m:
                stp.append(pnt)

        num_stp = len(stp)
        min_distance = dist_m

        if num_stp > 1:
            for i in range(num_stp-1):
                for j in range(i+1, min(i+8, num_stp)):
                    if dist(stp[i],stp[j]) < min_distance:
                        min_distance = dist(stp[i],stp[j])

    return min_distance
#----------------------------------------------------------------------

def read_file(filename):
    points=[]
    # File format
    # x1 y1
    # x2 y2
    # ...
    in_file=open(filename,'r')
    for line in in_file.readlines():
        line = line.strip()
        point_match=pointRE.match(line)
        if point_match:
            x = float(point_match.group(1)) # cast float
            y = float(point_match.group(2)) # cast float
            points.append((x,y))
    print(points)
    return points
#----------------------------------------------------------------------

def main(filename,algorithm):
    algorithm=algorithm[1:]
    print algorithm
    points = read_file(filename)
    if algorithm == 'dc':
        print("Divide and Conquer: ", nearest_neighbor(points))
    if algorithm == 'bf':
        print("Brute Force: ", brute_force_nearest_neighbor(points))
    if algorithm == 'both':
        print("Divide and Conquer: ", nearest_neighbor(points))
        print("Brute Force: ", brute_force_nearest_neighbor(points))
#----------------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python assignment1.py -<dc|bf|both> <input_file>")
        quit(1)
    if len(sys.argv[1]) < 2:
        print("python assignment1.py -<dc|bf|both> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])
