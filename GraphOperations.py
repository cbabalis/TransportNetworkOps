""" This module contains several operations regarding file structures
to graph models.

call it as  follow:

python GraphOps.py #TODO
"""

from xlrd import open_workbook
import pdb


class GraphOperations:
    """ This class contains operations for converting files to
    appropriate graph forms.
    """
    def __init__(self):
        self.S = []

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
        """ Converts a dictionary to adjacency list ready for use.
        """
        # G_adj_list represents the graph.
        G_struct = {}
        # if A->B vertix has a transportation cost, then create a
        # dictionary of the form: {A:[{B:3}, {C:6}]}
        # if A->B vertix has no transportation cost, then create
        # a dictionary of the form {A:[B, C]}
        for entry in a_dict:
            from_node = entry[from_n]
            to_node = entry[to_n]
            cost = float(entry[cost_n])
            self._add_edge_to_network(G_struct, from_node, to_node, cost)
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

    def dijkstra(self, G):
        dist = {}
        prev = {}
        v_conns = {}  # dictionary which has vertex' connections
        # initialize algorithm
        self._initialize_dijkstra(dist, prev, v_conns, G)
        # start from a random node (vertex)
        v_key, v_value = self._extract_edge(G)
        self._start_relaxation(v_key, v_value, G, dist, prev)
        return dist, prev

    def _initialize_dijkstra(self, dist, prev, v_conns, G):
        for g in G:
            self._insert_vertex_to_dict(dist, prev, g)
            neighbors = G[g]
            v_conns[g] = []
            for neighbor in neighbors:
                self._insert_vertex_to_dict(dist, prev, neighbor.keys()[0])
                v_conns[g].append(neighbor.keys()[0])

    def _insert_vertex_to_dict(self, dist, prev, v):
        inf = 100000000000000
        if v not in dist:
            dist[v] = inf
            prev[v] = None

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

    def _start_relaxation(self, v_key, v_value, G, dist, prev):
        from_vertex = v_key
        for v in v_value:
            to_vertex = v.keys()[0]
            cost = v.values()[0]
            self._relax(from_vertex, to_vertex, cost, G, dist, prev)

    def _relax(self, from_vertex, to_vertex, cost, G, dist, prev):
        if not G:
            return
        if dist[to_vertex] > dist[from_vertex] + cost:
            dist[to_vertex] = dist[from_vertex] + cost
            prev[to_vertex] = from_vertex
        v_key, v_value = self._extract_edge(G, to_vertex)
        self._start_relaxation(v_key, v_value, G, dist, prev)
