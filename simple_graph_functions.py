
graph = {
	"a": ["c"],
	"b": ["c", "e"],
	"c": ["a", "b", "d", "e"],
	"d" : ["c"],
        "e" : ["c", "b"],
        "f" : []
}

#generate lists of edges
#edge: 2-tuple with nodes as elements. (a, e), (a, b), etc
def generate_edges(graph):
  edges = []
  for node in graph:
    for neighbor in graph[node]:
      edges.append((node, neighbor))
  return edges

#find isolated nodes in a graph (does not have any incoming or outgoing edges)
def find_isolated(graph):
  isolated = []
  for node in graph:
    if not graph[node]:
       isolated.append(node)
  return isolated

def main():
  edges = generate_edges(graph)
  print "edges: ",
  print edges
  isolated = find_isolated(graph)
  print "isolated: ",
  print isolated

if __name__ == '__main__':
  main()
