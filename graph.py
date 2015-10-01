"""Python graph class, demonstrating
essential facts and functionalities of graphs
"""

class Graph(object):
  def __init__(self, graph_dict={}):
    """initializes a graph object """
    self.__graph_dict = graph_dict

  def vertices(self):
    """returns vertices of a graph"""
    return self.__graph_dict.keys()

  def edges(self):
    """returns edges of graph"""
    return self.__generate_edges()

  def add_vertex(self, vertex):
    """If vertex is not in self.__graph_dict, a key "vertex" with empty
    list added to dictionary. 
    Otherwise do nothing
    """
    if vertex not in self.__graph_dict:
      self.__graph_dict[vertex] = []

  def add_edge(self, edge):
    """assumes edge is of type set, tuple of list;
    between 2 vertices can have multiple edges
    """
    vertex_x, vertex_y = tuple(edge)
    if vertex_x in self.__graph_dict:
      self.__graph_dict[vertex_x].append(vertex_y)
    else:
      self.__graph_dict[vertex_x] = [vertex_y]
  
  def __generate_edges(self):
    """static method to generate edges of the graph.
    Edges are represented as sets with one (a loop back to the vertex) or two 
    vertices
    sets use  {} syntax
    """
    edges = []
    for vertex in self.__graph_dict:
      for neighbor in self.__graph_dict[vertex]:
        if {neighbor, vertex} not in edges:
          edges.append({vertex, neighbor})
    return edges
 
  def __str__(self):
    res = "vertices: " 
    for k in self.__graph_dict:
      res += str(k) + " "
    res += "\nedges: "
    for edge in self.__generate_edges():
      res += str(edge) + " "
    return res 

if __name__ == "__main__":
  g = { "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
        "f" : []
  }
  graph = Graph(g)

  print("Vertices of graph: ")
  print(graph.vertices())

  print("Edges of graph: ")
  print(graph.edges())

  print("Add vertex:")
  graph.add_vertex("z")

  print("Vertices of graph: ")
  print(graph.vertices())

  print("Add an edge")
  graph.add_edge({"a", "z"})

  print("Vertices of graph: ")
  print(graph.vertices())

  print("Edges of graph: ")
  print(graph.edges())

  print('Adding an edge {"x", "y"} with new vertices:')
  graph.add_edge({"x", "y"})
  print("Vertices of graph: ")
  print(graph.vertices())

  print("Edges of graph: ")
  print(graph.edges())


  

