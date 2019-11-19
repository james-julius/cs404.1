from python.src.util.linkedlist import LinkedList
from python.src.graph.edge import Edge


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = 0
        self.adjacency_list = [LinkedList()] * vertices

        for i in range(len(self.adjacency_list)):
            self.adjacency_list[i] = LinkedList()

    def num_edges(self):
        return self.edges

    def num_vertices(self):
        return self.vertices

    def validate_vertex(self, v):
        if v < 0 or v >= self.vertices:
            raise Exception("vertex %d is not between 0 and %d" %
                            (v, self.vertices - 1))

    def add_edge(self, source, dest, weight=0):
        self.validate_vertex(source)
        self.validate_vertex(dest)

        self.edges += 1
        self.adjacency_list[source].insert_end(Edge(source, dest, weight))
        self.adjacency_list[dest].insert_end(Edge(dest, source, weight))

    def edges(self):
        edge_list = LinkedList()

        for i in range(self.vertices):
            for edge in self.adjacent_vertices(i):
                edge_list.insert_end(edge)

        return edge_list

    def adjacent_vertices(self, v):
        self.validate_vertex(v)
        return self.adjacency_list[v]

    def degree(self, v):
        self.validate_vertex(v)
        return self.adjacency_list[v].size()
