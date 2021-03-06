# script which imports a .dbf file, converts it to graph and writes
# the results to json/csv.

import sys
from GraphOperations import GraphOperations


def main():
    graph_ops = GraphOperations()
    # read the file and convert it to dictionary
    g = graph_ops.load_file(sys.argv[1])
    # create the graph
    dest = 'FromNodeID,N,18,0'
    arrival = 'ToNodeID,N,18,0'
    a_cost = 'LinkLength,N,18,6'
    G = graph_ops.convert_dict_to_adj_list(g, dest, arrival, a_cost)
    print "Now the graph as edges"
    # TODO G = graph_ops.convert_dict_to_edges(g, dest, arrival, a_cost)
    print G
    # write the results to json file
    print len(graph_ops.S)
    dist, prev = graph_ops.run_dijkstra(G)


if __name__ == '__main__':
    main()
