""" This module contains several operations regarding file structures
to graph models.

call it as  follow:

python GraphOps.py #TODO
"""

from xlrd import open_workbook


class GraphOperations:
    """ This class contains operations for converting files to
    appropriate graph forms.
    """
    def __init__(self):
        pass

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

    def convert_dict_to_adj_list(self, a_dict, has_cost=False):
        """ Converts a dictionary to adjacency list ready for use.
        :param bool has_cost: is a boolean indicating if the graph has
            cost or not.
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
