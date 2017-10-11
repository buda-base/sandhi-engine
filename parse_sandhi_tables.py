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
        this_dir = os.path.split(__file__)[0]
        self.input_path = os.path.join(this_dir, 'resources', '{}_sandhi_charts'.format(language), 'csv')
        self.output_path = os.path.join(this_dir, 'sandhi_rules')
        self.parsed_tables = {}
        self.sandhi_rules = {}

    def parse(self):
        tables = [a for a in os.listdir(self.input_path)]
        self.extract_tables(tables)
        self.format_into_sandhi_rules()
        self.save_sandhi_rules()

    def extract_tables(self, tables):
        for t in tables:
            current_table = t.replace('.csv', '')
            table_content = self.open_table(os.path.join(self.input_path, t))

            # set up the table
            self.parsed_tables[current_table] = {'initials': [], 'table': []}

            # first row
            self.parsed_tables[current_table]['initials'].extend(table_content[0][1:])

            # the table proper
            for row in table_content[1:]:
                finals = row[0]     # first column
                sandhis = row[1:]   # sandhis
                self.parsed_tables[current_table]['table'].append((finals, sandhis))

    def format_into_sandhi_rules(self):
        for table_name, table in self.parsed_tables.items():
            initials = table['initials']
            sandhis = table['table']
            rules = self.format_rules(initials, sandhis, table_name)
            self.sandhi_rules[table_name] = rules

    @staticmethod
    def format_rules(initials, sandhi, table_name):
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
                case = SandhiTableParser.generate_sandhi_case(table_name, initials[num], form)
                if case not in rule:
                    rule.append(case)
            if final in rules.keys():
                rules[final].extend(rule)
            else:
                rules[final] = rule
        return rules

    @staticmethod
    def generate_sandhi_case(table_name, initial, form):
        if table_name == 'consonants1':
            if '(' in form:
                new_final, new_initial = form.strip(')').split('(')
                case = (initial, (new_final, new_initial))
            else:
                case = (initial, (form, initial))
        else:
            case = (initial, form)
        return case

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
    parser.parse()
