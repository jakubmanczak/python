# DIJKSTRA ALGORITHM
# jakubmanczak

startNode = 'A' # vertex from which we start
destinationNode = 'H' # vertex which we want to reach
pathCost = {} # object holding cost of different paths
previous = {} # object holding previous nodes
queue = []
graph = {
  'A': {'B': 1, 'F': 8, 'E': 4},
  'B': {'F': 6, 'G': 2, 'C':2},
  'C': {'G': 2, 'D': 1},
  'D': {'G': 1, 'H': 4},
  'E': {'F': 5, },
  'F': {},
  'G': {'F': 1, 'H': 1},
  'H': {},
}

for n in graph: # n for node, so for each node in our graph
  queue.append(n) # add to queue
  previous[n] = None # initialise position in adjacency object
  pathCost[n] = float("inf") # set path cost to infinite
pathCost[startNode] = 0 # override initial node's infinite cost to 0

while queue: # iterate as long as there's stuff in the queue
  smallestNode = queue[0] # set smallestNode as first item in queue
  smallestValue = pathCost[smallestNode] # set its value
  for i in range(1, len(queue)): # find the actual smallest node & replace prev from queue start
    if pathCost[queue[i]] < smallestValue:
      smallestNode = queue[i]
      smallestValue = pathCost[smallestNode]
  currentNode = smallestNode # set current iteration node as smallestNode
  queue.remove(currentNode) # remove it from queue
  for i in graph[currentNode]: # for every node adjacent to the currentNode
    alternateNode = graph[currentNode][i] + pathCost[currentNode] # evaluate the adjacent nodes and compare them
    if pathCost[i] > alternateNode: # if any paths are more efficient, use them instead
      pathCost[i] = alternateNode
      previous[i] = currentNode

print(destinationNode) # print destination
while 1: # loop until we find initial
  destinationNode = previous[destinationNode] # set new destination as the previous node for the currentNode destination
  if destinationNode == None: break # if node is the starting one, stop
  print(destinationNode) # print next destination