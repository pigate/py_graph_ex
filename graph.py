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

  def find_path(self, start_vertex, end_vertex, path=[]):
    """find path from start_vertex to end_vertex in graph """
    graph = self.__graph_dict
    path = path + [start_vertex]
    if start_vertex == end_vertex:
      return path
    if start_vertex not in graph:
      return None
    for vertex in graph[start_vertex]:
      if vertex not in path:
        extended_path = self.find_path(vertex, end_vertex, path)
        if extended_path:
          return extended_path
    return None

  def find_all_paths(self, start_vertex, end_vertex, path=[]):
    """find all paths from start_vertex to end_vertex in graph"""
    graph = self.__graph_dict
    path = path + [start_vertex]
    paths = [path]
    if start_vertex == end_vertex:
      return paths
    if start_vertex not in graph:
      return []
    for vertex in graph[start_vertex]:
      #check for cycle
      if vertex not in path: 
        extended_paths = self.find_all_paths(vertex, end_vertex, path)
        for p in extended_paths:
          paths.append(p)
    return paths

  def find_first_cycle(self, start_vertex, path=[]):
    """find first cycle in graph"""
    graph = self.__graph_dict
    if start_vertex not in graph:
      return None
    #update acc
    if start_vertex in path:
      return path + [start_vertex]
    path = path + [start_vertex]
    for vertex in graph[start_vertex]:
      extended_path_cycle = self.find_first_cycle(vertex, path)
      if extended_path_cycle:
        return extended_path_cycle
    return None


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

  path_a_b = graph.find_path("a", "b", [])
  print "Path from a to b: ",
  print path_a_b

  path_a_f = graph.find_path("a", "f", [])
  print "Path from a to f: ",
  print path_a_f
  
  all_paths_a_b = graph.find_all_paths("a", "b", [])
  print "All paths from a to b: ",
  print all_paths_a_b

  all_paths_a_f = graph.find_all_paths("a", "f", [])
  print "All paths from a to f: ",
  print all_paths_a_f

  cycle_a = graph.find_first_cycle("a", [])
  print "Cycle from a: ",
  print cycle_a

  cycle_b = graph.find_first_cycle("b", [])
  print "Cycle from b: ",
  print cycle_b
 
  cycle_c = graph.find_first_cycle("c", [])
  print "Cycle from c: ",
  print cycle_c

  cycle_f = graph.find_first_cycle("f", [])
  print "Cycle from f: ",
  print cycle_f
