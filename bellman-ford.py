# BELLMAN-FORD ALGORITHM
# jakubmanczak

nodes = [
  "S","A","B","C","D","E","F","G","H","I"
] # list of nodes because i'm too lazy to write...
# ...code that extracts them from the edges
startnode = "S" # the node from which we start
dist = {} # object holding distances to nodes
edges = [ # list of edges of the graph
  ["S","A",7],["S","C",6],["S","F",5],["S","E",6],
  ["A","B",4],["A","C",-2],
  ["B","G",-2],["B","H",-4],
  ["C","D",2],["C","F",1],
  ["E","F",-2],["E","H",3],
  ["F","D",3],
  ["G","I",-1],
  ["H","G",1],
  ["I","H",1]
]

for i in nodes: # we set all distances to infinity to start
  dist[i] = float("inf") 
dist[startnode] = 0 # distance of starting node is always 0

for i in range(len(nodes) - 1): # we iterate V (amount of vertices) minus 1 times
  for start, destination, weight in edges: 
    if dist[start] != float("inf") and dist[start] + weight < dist[destination]: 
      dist[destination] = dist[start] + weight # we "perform the relaxation" if conditions met

for start, destination, weight in edges: # detect if there are negative cycles
  if dist[start] != float("inf") and dist[start] + weight < dist[destination]:
    print("bad graph, friend") # if there are, warn the user
    print("results ahead are misleading and false :(")

print(dist)