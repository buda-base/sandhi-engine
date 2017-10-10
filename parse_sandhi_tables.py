# encoding: utf-8
import os
import csv
import json


class SandhiTableParser:
    """
    Parse the sandhi tables, format them into rules and save them in a json file
    """

    def __init__(self, language):
        self.language = language
        self.input_path = os.path.join('resources', '{}_sandhi_charts'.format(language), 'csv')
        self.output_path = 'sandhi_rules'
        self.parsed_tables = {}
        self.current_table = ""
        self.sandhi_rules = {}

    def parse_tables_folder(self):
        tables = [a for a in os.listdir(self.input_path)]
        for t in tables:
            self.current_table = t.replace('.csv', '')

            table = self.open_table(os.path.join(self.input_path, t))

            self.parse_table(table)

        self.format_into_sandhi_rules()
        self.save_sandhi_rules()

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

    def format_into_sandhi_rules(self):
        for table_name, table in self.parsed_tables.items():
            initials = table['initials']
            sandhis = table['table']
            rules = self.format_rules(initials, sandhis)
            self.sandhi_rules[table_name] = rules

    @staticmethod
    def format_rules(initials, sandhi):
        """
        Unpacks the sandhi table into individual rules

        :param initials: The first row containing the initial char of the next word
        :param sandhi: The remaining rows, the first column contains the ending char of the current word
        :return: [('a', [('a', 'A'), ('A', 'A'), ...]), ('A', [('a', 'A'), ('A', 'A'), ...]), ...]
        """
        rules = {}
        for final, sandhied_forms in sandhi:
            rule = []
            for num, form in enumerate(sandhied_forms):
                rule.append((initials[num], form))
            rules[final] = rule
        return rules

    @staticmethod
    def open_table(path):
        with open(path, 'r', 1, 'utf-8') as csvfile:
            return list(csv.reader(csvfile, delimiter=','))

    def save_sandhi_rules(self):
        with open(os.path.join(self.output_path, self.language+'_rules.json'), 'w') as f:
            json.dump(self.sandhi_rules, f, sort_keys=True)

if __name__ == '__main__':
    lang = 'sanskrit'

    parser = SandhiTableParser(lang)
    parser.parse_tables_folder()
