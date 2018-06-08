# encoding: utf-8
import os
import re
import json
from collections import OrderedDict
from parse_sandhi_tables import SandhiTableParser


class FindApplicableSandhis:
    """

    """
    def __init__(self, language, idempotent=False):
        self.language = language
        self.sandhi_rules = {}
        self.load_sandhi_rules()
        self.applicable_sandhis = None
        self.sandhi_types = {
            'vowels': 1,
            'consonants1': 2,
            'consonants1_vowels': 3,
            'consonants2': 4,
            'visarga1': 5,
            'visarga2': 6,
            'absolute_final_consonants': 7,
            'cC_words': 8,
            'punar': 9,
            'idem': 10
        }
        self.idempotent = idempotent
        self.idempotent_groups = {'vowels': '£1', 'consonants1': '£2', 'consonants2': '£3',
                                  'cC_words': '£4', 'consonants1_vowels': '£5', 'visarga1': '£6',
                                  'visarga2': '£7', 'punar': '£8'}

    def all_possible_sandhis(self, inflected_form):
        """
        Generates all the sandhis for an inflected form.
            - 'sandhied' receives the sandhied forms from the sandhi functions
            - the entries are formatted by format_entries()
        :param inflected_form: the form to sandhify
        :return: ex. rAmA['rAmA,a:A,/', 'rAme,i,-e+A/', ...]
        """
        # ensure there are no sandhis from last call
        self.applicable_sandhis = OrderedDict()

        # split in stem and ending
        final = inflected_form[-1]
        stem = inflected_form[:-1]

        a = 'vowels'
        if final in self.sandhi_rules[a]:
            self.find_vowel_sandhis(stem, final, a)

        b = 'consonants1'
        if final in self.sandhi_rules[b]:
            self.find_consonant1_sandhis(stem, final, b)

        c = 'consonants2'
        if final in self.sandhi_rules[c]:
            self.find_consonant2_sandhis(stem, final, c)

        d = 'cC_words'
        if final in self.sandhi_rules[d]:
            self.find_cch_words_sandhis(stem, final, d)

        # the following three sandhis apply to the last two characters
        final = inflected_form[-2:]
        stem = inflected_form[:-2]

        e = 'consonants1_vowels'
        if final in self.sandhi_rules[e]:
            self.find_visarga_or_consonants1_vowels_sandhis(stem, final, e)

        f = 'visarga1'
        if final in self.sandhi_rules[f]:
            self.find_visarga_or_consonants1_vowels_sandhis(stem, final, f)

        g = 'visarga2'
        if final in self.sandhi_rules[g]:
            self.find_visarga_or_consonants1_vowels_sandhis(stem, final, g)

        h = 'absolute_final_consonants'
        self.find_absolute_finals_sandhis(inflected_form, h)

        # Exceptions
        i = 'punar'
        if inflected_form == i:
            self.find_punar_sandhis(i)

        return self.format_found_sandhis()

    def find_idempotent(self, stem, final, name):
        diff = '/-+{}'.format(self.idempotent_groups[name])
        diff += '=' + str(self.sandhi_types['idem'])
        self.add_entries(stem + final + '%' + diff, '£')

    def find_vowel_sandhis(self, stem, final, name):
        """
        Finds all vowel sandhis

        :param stem: the form without the declension
        :param final: the declension (1 char) used to determine which rule to apply
        :param name: the name of the applied sandhi
        """
        for rule in self.sandhi_rules[name][final]:
            initial = rule[0]
            new_final = rule[1]

            # calculating the diff for vowel sandhi
            if ' ' in new_final:
                new_final, new_initial = new_final.split(' ')
                if new_initial == initial:
                    diff = '-{}+{}/- +'.format(new_final, final)
                else:
                    diff = '-{}+{}/- {}+{}'.format(new_final, final, new_initial, initial)
            elif final == new_final:
                diff = '/-+{}'.format(initial)
            else:
                diff = '-{}+{}/-+{}'.format(new_final, final, initial)

            diff += '='+str(self.sandhi_types[name])  # adding sandhi type
            if self.idempotent:
                diff += self.idempotent_groups[name]
            # adding the entries
            self.add_entries(stem + new_final + '%' + diff, initial)

    def find_consonant1_sandhis(self, stem, final, name):
        """
        Finds all sandhis from the 1st consonant sandhi table

        :param stem: the form without the declension
        :param final: the declension (1 char) used to determine which rule to apply
        :param name: the name of the applied sandhi
        """
        for rule in self.sandhi_rules[name][final]:
            initial = rule[0]
            new_final = rule[1][0]
            new_initial = rule[1][1]

            # calculating diff for consonant sandhi
            if final == new_final and initial == new_initial:
                diff = '/- +'
            elif final == new_final and initial != new_initial:
                diff = '/- {}+{}'.format(new_initial, initial)
            elif final != new_final and initial == new_initial:
                diff = '-{}+{}/- +'.format(new_final, final)
            else:
                diff = '-{}+{}/- {}+{}'.format(new_final, final, new_initial, initial)

            diff += '='+str(self.sandhi_types[name])  # adding sandhi type
            if self.idempotent:
                diff += self.idempotent_groups[name]
            # adding the entries
            self.add_entries(stem + new_final + '%' + diff, initial)

    def find_consonant2_sandhis(self, stem, final, name):
        """
        Finds all sandhis from the 2nd consonant sandhi table

        :param stem: the form without the declension
        :param final: the declension (1 char) used to determine which rule to apply
        :param name: the name of the applied sandhi
        """
        for rule in self.sandhi_rules[name][final]:
            initial = rule[0]
            new_final = rule[1]

            # calculating diff for consonant sandhi 2
            diff = ''
            if final == new_final:
                diff = '/- +'
            elif final != new_final:
                diff = '-{}+{}/- +'.format(new_final, final)

            diff += '='+str(self.sandhi_types[name])  # adding sandhi type
            if self.idempotent:
                diff += self.idempotent_groups[name]
            # adding the entries
            self.add_entries(stem + new_final + '%' + diff, initial)

    def find_visarga_or_consonants1_vowels_sandhis(self, stem, final, name):
        """
        Finds all the sandhis from the 1st visarga table

        :param stem: the form without the declension
        :param final: the declension (2 chars) used to determine which rule to apply
        :param name: the name of the applied sandhi
        """
        for rule in self.sandhi_rules[name][final]:
            initial = rule[0]
            new_final = rule[1]

            # calculating diff for visarga sandhi 1
            diff = ''
            if final == new_final:
                diff = '/- +'
            elif ' ' in new_final:
                new_final, new_initial = new_final.split(' ')
                if new_initial == initial:
                    diff = '-{}+{}/- +'.format(new_final, final)
                else:
                    diff = '-{}+{}/- {}+{}'.format(new_final, final, new_initial, initial)
            elif final != new_final:
                diff = '-{}+{}/- +'.format(new_final, final)

            diff += '='+str(self.sandhi_types[name])  # adding sandhi type
            if self.idempotent:
                diff += self.idempotent_groups[name]
            # adding the entries
            self.add_entries(stem + new_final + '%' + diff, initial)

    def find_absolute_finals_sandhis(self, inflected_form, name):
        """
        Finds all the sandhis from the absolute finals sandhi table

        :param inflected_form: unlike other rules. clusters of consonants have to be detected,
                                so the whole inflected form is taken
        :param name: the name of the applied sandhi
        """
        # find ending (can be a cluster of consonants or a single one)
        consonants = ["k", "K", "g", "G", "N", "c", "C", "j", "J", "Y", "w", "W", "q", "Q", "R", "t", "T", "d",
                      "D", "n", "p", "P", "b", "B", "m", "y", "r", "l", "v", "S", "z", "s", "h"]
        if inflected_form[-1] in consonants:
            stem, final = re.split('([' + ''.join(consonants) + ']+)$', inflected_form)[:2]

            # clusters of consonants are reduced to the first consonant
            if len(final) > 1:
                stem = stem + final[0]
                final = final[1:]
                diff = '-+{}/'.format(final)
                diff += '='+str(self.sandhi_types[name])  # adding sandhi type
                self.add_entries(stem + '%' + diff, '')
            elif final in self.sandhi_rules[name].keys():
                for rule in self.sandhi_rules[name][final]:
                    new_final = rule[1]

                    # calculating diff for absolute finals sandhi
                    diff = ''
                    if final == new_final:
                        diff = '/'
                    elif final != new_final:
                        diff = '-{}+{}/'.format(new_final, final)

                    diff += '='+str(self.sandhi_types[name])  # adding sandhi type
                    # adding the entries
                    self.add_entries(stem + new_final + '%' + diff, '')

    def find_cch_words_sandhis(self, stem, final, name):
        """
        Finds all the sandhis from the cC words table

        :param stem: the form without the declension
        :param final: the declension (1 char) used to determine which rule to apply
        :param name: the name of the applied sandhi
        """
        for rule in self.sandhi_rules[name][final]:
            initial = rule[0]
            new_initial = rule[1]

            diff = '/- {}+{}'.format(new_initial, initial)

            diff += '=' + str(self.sandhi_types[name])  # adding sandhi type
            if self.idempotent:
                diff += self.idempotent_groups[name]
            # adding the entries
            self.add_entries(stem + final + '%' + diff, initial)

    def find_punar_sandhis(self, name):
        """
        Finds all sandhis for punar

        :param name: the name of the applied sandhi
        """
        stem = 'puna'
        final = 'r'
        for rule in self.sandhi_rules[name][final]:
            initial = rule[0]
            new_final = rule[1]

            # calculating diff for visarga sandhi 1
            diff = ''
            if final == new_final:
                diff = '/- +'
            elif final != new_final:
                diff = '-{}+{}/- +'.format(new_final, final)

            diff += '=' + str(self.sandhi_types[name])  # adding sandhi type
            if self.idempotent:
                diff += self.idempotent_groups[name]
            # adding the entries
            self.add_entries(stem + new_final + '%' + diff, initial)

    def load_sandhi_rules(self):
        absolute_path_to_sandhi_json = os.path.join(os.path.split(__file__)[0], 'sandhi_rules', self.language + '_rules.json')
        # generate them if they don't exist
        if not os.path.isfile(absolute_path_to_sandhi_json):
            parser = SandhiTableParser(self.language)
            parser.parse()
        with open(absolute_path_to_sandhi_json, 'r') as f:
            self.sandhi_rules = json.load(f)

    def add_entries(self, form_n_diff, initial):
        """
        Used by all the sandhi functions to bring together all the entries sharing
        the same inflected form and the same diffs
        format_entries() is then used to reformat the entry in '<form>,<initials>,<diff>'

        an OrderedDict is filled with form+'%'+diff(form_n_diff) as keys and the list of possible initials as value
        ex: {"rAmo'%-o'+aH/": ['a'], 'rAma%-a+aH/': ['A', 'i', 'u', 'U', 'f', 'e', 'E', 'o', 'O'], ...}
        """
        if form_n_diff not in self.applicable_sandhis.keys():
            self.applicable_sandhis[form_n_diff] = [initial]
        elif initial not in self.applicable_sandhis[form_n_diff]:  # avoid duplicates as the tables contain many of them
            self.applicable_sandhis[form_n_diff].append(initial)

    def format_found_sandhis(self):
        """
        Restructures the output of add_entries() into normal entries

        :return: ex: ["rAmo',a,-o'+aH/", 'rAma,A:i:u:U:f:e:E:o:O,-a+aH/', ...]
        """
        formatted = []
        for k, v in self.applicable_sandhis.items():
            parts = k.split('%')
            form = parts[0]
            diff = parts[1]
            initials = ':'.join(v)
            formatted.append('{},{}${}'.format(form, initials, diff))
        return formatted
