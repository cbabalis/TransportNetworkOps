""" This module contains several operations regarding file structures
to graph models.

call it as  follow:

python GraphOps.py #TODO
"""

from xlrd import open_workbook
import random
import sys
sys.setrecursionlimit(60000)


class GraphOperations:
    """ This class contains operations for converting files to
    appropriate graph forms.
    """
    def __init__(self):
        self.S = []
        self.counter = 0

    def load_file(self, xlsx_file):
        """ Converts a file to an adjecency list.
        :param file xlsx_file: is the file to be converted.

        :rtype: list
        """
        # open and load the file
        book = open_workbook(xlsx_file)
        sheet = book.sheet_by_index(0)

        # read header values into the list
        keys = [sheet.cell(0, col_index).value
                for col_index in xrange(sheet.ncols)]

        dict_list = []
        for row_index in xrange(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value
                 for col_index in xrange(sheet.ncols)}
            dict_list.append(d)
        return dict_list

    def convert_dict_to_adj_list(self, a_dict, from_n, to_n, cost_n):
        """ Converts a dictionary to adjacency list ready for using.
        """
        # G_adj_list represents the graph.
        G_struct = {}
        # if A->B vertex has a transportation cost, then create a
        # dictionary of the form: {A:[{B:3}, {C:6}]}
        # if A->B vertex has no transportation cost, then create
        # a dictionary of the form {A:[B, C]}
        for entry in a_dict:
            from_node = entry[from_n]
            to_node = entry[to_n]
            cost = float(entry[cost_n])
            self._add_edge_to_network(G_struct, from_node, to_node, cost)
            # also, populate the neighbor with no nodes in it
            if to_node not in G_struct:
                G_struct[to_node] = [{from_node: cost}]
        return G_struct

    def convert_dict_to_edges(self, a_dict, from_n, to_n, cost_n):
        """ Converts a dictionary to all edges in graph.
        """
        G_struct = []
        for entry in a_dict:
            from_node = entry[from_n]
            to_node = entry[to_n]
            cost = float(entry[cost_n])
            G_struct.append((str(from_node), str(to_node), float(cost)))
        return G_struct

    def _add_edge_to_network(self, G_struct, from_node, to_node, cost):
        """ Method which adds an edge from "from_node" to "to_node"
        adding the transportation cost.
        :param str from_node: a node
        :param str to_node: a node.
        :param float cost: the transtportation cost between the two
            nodes.
        """
        # check if from_node is already in the list. If not, add it
        # else, append to the list the new entry.
        if from_node not in G_struct:
            G_struct[from_node] = []
        G_struct[from_node].append({to_node: cost})

    def write_adj_list_to_file(self, has_cost, output_file):
        """ Method to write an adjacency list to a .csv file.
        :param bool has_cost: boolean variable indicating if the graph
            has cost or not.
        :param str output_file: is the file where the  adjacency list
            will be written.
        """
        # read the dictionary
        pass

    def convert_csv_to_xls(self, csv_file, xlsx_file):
        """ This method converts a csv file to xls.
        :param str csv_file: the .csv file formed after the conversion.
        :param str xlsx_file: the .xls file to be converted.
        """
        pass

    def convert_xls_to_csv(self, xlsx_file, csv_file):
        """ This method converts an xls file to csv.
        :param str xlsx_file: the .xls file to be converted.
        :param str csv_file: the .csv file formed after the conversion.
        """
        pass

    def _extract_edge(self, G, key=None):
        """ Method which extracts a random entry of G, or
        a specific key, if given.
        """
        if not key:
            random_entry = G.popitem()
            return random_entry[0], random_entry[1]
        else:
            for g in G:
                if float(key) == g:
                    entry = G.pop(key)
                    return key, entry
        print "Nothing has been found!"
        return -1

    def run_dijkstra(self, G):
        """ Runs dijkstra algorithm. """
        # get all nodes of the graph and initialize them.
        self.dist = {}
        self.prev = {}
        self._initialize_dijkstra(G, self.dist, self.prev)
        while G:
            # pop a random node (vertex)
            first_node = random.choice(list(G))
            self.dist[first_node] = 0
            # run dijkstra starting from random vertex
            self._relax(first_node, self.dist, self.prev, G)
        # return the distance and previous dictionaries, respectively.
        return self.dist, self.prev

    def _initialize_dijkstra(self, G, dist, prev):
        """ method to initialize all vertices of a graph.
        """
        inf = 10000000000000000000
        for v in G:
            neighbors = G[v]
            for neighbor in neighbors:
                for n in neighbor:
                    dist[n] = inf
                    prev[n] = None

    def _relax(self, vertex, dist, prev, G):
        """ Method which relaxes a vertex as described in dijkstra
        algorithm.
        """
        self.counter += 1
        if vertex in G:
            neighbors = G[vertex]
            for neighbor in neighbors:
                for key in neighbor:
                    print self.counter
                    if dist[key] > neighbor[key] + dist[vertex]:
                        dist[key] = neighbor[key] + dist[vertex]
                        prev[key] = vertex
                        self._relax(key, dist, prev, G)
            # G[vertex] has been relaxed. remove it from struct.
            # if it has been removed previously, just ignore it
            del G[vertex]
