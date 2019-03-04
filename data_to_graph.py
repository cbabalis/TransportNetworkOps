# script which imports a .dbf file, converts it to graph and writes
# the results to json/csv.

import sys
from GraphOperations import GraphOperations


def main():
    graph_ops = GraphOperations()
    # read the file and convert it to dictionary
    g = graph_ops.convert_file_to_adj_list(sys.argv[1])
    print g
    # create the graph
    # write the results to json file
    pass


if __name__ == '__main__':
    main()
