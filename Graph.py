""" This module represents a graph."""


class Graph:
    """ Graph class. """
    def __init__(self):
        pass


class Vertex:
    """ Class which represents a vertex of a graph."""
    def __init__(self):
        self.neighbors = {}

    def _sort_neighbors_by_cost(self):
        return sorted(self.neighbors(), key=lambda kv: kv[1])
