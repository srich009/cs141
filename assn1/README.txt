Nearest Points Program:
-------------------------

to run can use either python OR python3

$ python nearest_neighbor.py -<dc|bf|both|time> <input_file>

flag options:
-dc == run divide and conquer algorithm
-bf == run brute force algorithm
-both == run divide and conquer THEN brute force algorithms
-time == run and time both the divide and conquer THEN brute force algorithms

input file:
a text file, should contain a list of n points.
format:
x1 y1
x2 y2
...
xn yn

output:
an output file will be generated, it will contain the distance calculated by the nearest neighbor algorithm