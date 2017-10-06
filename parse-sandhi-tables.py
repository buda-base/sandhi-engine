import os
import csv
import pickle


class SandhiTableParser(object):
    """
    Parse the sandhi tables and pickle them
    """

    def __init__(self, language):
        self.language = language
        self.input_path = os.path.join('resources', '{}_sandhi_charts'.format(language), 'csv')
        self.parsed_tables = {}
        self.current_table = ""

    def parse_tables_folder(self):
        tables = [a for a in os.listdir(self.input_path)]
        for t in tables:
            self.current_table = t.rstrip('.csv')
            absolute_path = os.path.join(self.input_path, t)

            # open the table
            table = self.open_table(absolute_path)

            # parse the table
            self.parse_table(table)

        # pickle all tables
        self.save_parsed_tables()

    def parse_table(self, content):
        # set up the table
        self.parsed_tables[self.current_table] = {'initials': [], 'table': []}

        # first row
        self.parsed_tables[self.current_table]['initials'].extend(content[0][1:])

        # the table proper
        for row in content[1:]:
            finals = row[0]     # first column
            sandhis = row[1:]   # sandhis
            self.parsed_tables[self.current_table]['table'].append((finals, sandhis))

    @staticmethod
    def open_table(path):
        with open(path, 'r', 1, 'utf-8') as csvfile:
            return list(csv.reader(csvfile, delimiter=','))

    def save_parsed_tables(self):
        with open(os.path.join('pickled_tables', self.language+'.pickle'), 'wb') as f:
            pickle.dump(self.parsed_tables, f, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    parser = SandhiTableParser('sanskrit')
    parser.parse_tables_folder()
