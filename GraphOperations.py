""" This module contains several operations regarding file structures
to graph models.

call it as  follow:

python GraphOps.py #TODO
"""


class GraphOperations:
    """ This class contains operations for converting files to
    appropriate graph forms.
    """
    def __init__(self):
        pass

    def convert_file_to_adj_list(self, a_file, has_cost=False):
        """ Converts a file to an adjecency list.
        :param file a_file: is the file to be converted.
        :param bool has_cost: is a boolean indicating if the graph has
            cost or not.

        :rtype: list
        """
        # if A->B vertix has a transportation cost, then create a
        # dictionary of the form: {A:[{B:3}, {C:6}]}
        # if A->B vertix has no transportation cost, then create
        # a dictionary of the form {A:[B, C]}
        # TODO return the list
        pass

    def write_adj_list_to_file(self, has_cost, output_file):
        """ Method to write an adjacency list to a .csv file.
        :param bool has_cost: boolean variable indicating if the graph
            has cost or not.
        :param str output_file: is the file where the  adjacency list
            will be written.
        """
        # read the dictionary
        pass

    def convert_csv_to_xls(self, csv_file, xls_file):
        """ This method converts a csv file to xls.
        :param str csv_file: the .csv file formed after the conversion.
        :param str xls_file: the .xls file to be converted.
        """
        pass

    def convert_xls_to_csv(self, xls_file, csv_file):
        """ This method converts an xls file to csv.
        :param str xls_file: the .xls file to be converted.
        :param str csv_file: the .csv file formed after the conversion.
        """
        pass
