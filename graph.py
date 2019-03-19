class Vertex:
    def __init__(self):
        self.prev = None
        self.links_to = []
        self.cost = 100000000000

    def compute_cost(self, u, v):
        """ Computes the cost for going from u to v."""
        pass


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def populate_graph(self, graph):
        pass

    def add_vertex(self, vertex):
        pass

    def run_dijkstra(self, G, v):
        pass
