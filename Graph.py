""" This module implements a graph and algorithms which operate on it.
"""


class Graph:
    def __init__(self):
        pass

    def dijkstra(self, G):
        """ Implements Dijkstra algorithm.
        :param struct G: is the graph in the given form.
        """
        # for all u in V:
        #   dist(u) = inf
        #   prev(u) = nil
        # dist(s) = 0
        self.create_struct(G)

        # H = makequeue(V) (using dist-values as keys)
        # while H is not empty:
        #   u = deletemin(H)
        #   for all (u, v) in E:
        #       if dist(v) > dist(u) + l(u, v):
        #           dist(v) = dist(u) + l(u, v)
        #           prev(v) = u
        #           decreasekey(H, v)
        pass
