#---------------------------
# weighted graph algorithms
# all points shortest path
#---------------------------

import sys
import re
import time

graphRE = re.compile("(\\d+)\\s(\\d+)")
edgeRE = re.compile("(\\d+)\\s(\\d+)\\s(-?\\d+)")

vertices = []
edges = []
#-----------------------------------------------------------------------------------------------

# The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]

def fancyPrint(p):
    j = 0
    n = len(vertices)
    for i in p:
    	print(i)
    	if j == n-1:
    		print('')
    		j = 0
    		continue
    	j += 1
#------------------------------------------------------------------------------------------------

# all points
def BellmanFord(G):

    pathPairs = []
    temp = []  
    n = len(vertices)
   
    for i in range(n):
        for j in range(n):
            temp = BelmanFord_SS(G,i)
            pathPairs.append( ( (i,j) , float(temp[j]) ) )

    # fancyPrint(pathPairs)
    print(pathPairs)

    return pathPairs
#-------------------------------------------------------------------------------------------------

# single source
def BelmanFord_SS(G,s):

    d = []
    n = len(vertices)

    # Step 1: initialize graph
    for i in range(n):
        d.append(float('inf'))
   
    d[s] = 0  

    # Step 2: relax edges repeatedly
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if (float(d[u]) + float(edges[u][v])) < float(d[v]):
                    d[v] = float(d[u]) + float(edges[u][v])

   # Step 3: check for negative-weight cycles
    for u in range(n):
        for v in range(n):
            if float(d[u]) + float(edges[u][v]) < float(d[v]):
            	print("Error: negative cycle")
                return false

    return d
#-------------------------------------------------------------------------------------------------

def FloydWarshall(G):

    pathPairs = []
    n = len(vertices)
    
    # set vertex to self = 0
    for i in range(n):
        edges[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if float(edges[i][k]) == float('inf') or float(edges[k][j]) == float('inf'):
                    continue
                if float(edges[i][j]) > float(edges[i][k]) + float(edges[k][j]):
                    edges[i][j] = float(edges[i][k]) + float(edges[k][j])

    for i in range(n):
        for j in range(n):
            pathPairs.append( ( (i,j) , float(edges[i][j]) ) )

    # fancyPrint(pathPairs)
    print(pathPairs)

    return pathPairs
#-------------------------------------------------------------------------------------------------

def readFile(filename):
    global vertices
    global edges
    # File format:
    # <# vertices> <# edges>
    # <s> <t> <weight>
    # ...
    inFile = open(filename,'r')
    line1 = inFile.readline()
    graphMatch = graphRE.match(line1)
    if not graphMatch:
        print(line1 + " not properly formatted")
        quit(1)
    vertices = list(range(int(graphMatch.group(1))))
    edges = []
    for i in range(len(vertices)):
        row = []
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch = edgeRE.match(line)
        if edgeMatch:
            source = edgeMatch.group(1)
            sink = edgeMatch.group(2)
            if int(source) > len(vertices) or int(sink) > len(vertices):
                print("Attempting to insert an edge between " + source + " and " + sink + " in a graph with " + vertices + " vertices")
                quit(1)
            weight = edgeMatch.group(3)
            edges[int(source)][int(sink)] = weight
    #Debugging
    #for i in G:
        #print(i)
    return (vertices,edges)
#-------------------------------------------------------------------------------------------------

def main(filename,algorithm):
    algorithm = algorithm[1:]
    G = readFile(filename)
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)
    if algorithm == 'b' or algorithm == 'B':
        BellmanFord(G)
    if algorithm == 'f' or algorithm == 'F':
        FloydWarshall(G)
    if algorithm == "both":
        start = time.clock()
        BellmanFord(G)
        end = time.clock()
        BFTime = end - start
        start = time.clock()
        FloydWarshall(G)
        end = time.clock()
        FWTime = end - start
        print("Bellman-Ford timing: " + str(BFTime))
        print("Floyd-Warshall timing: " + str(FWTime))
#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>") # remember to rename the file later
        quit(1)
    main(sys.argv[2],sys.argv[1])
#-------------------------------------------------------------------------------------------------

