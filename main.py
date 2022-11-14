# Łukasz PTAK WCY19KA1S0
# ZAD_1

import re
import csv

class RegEx:

    no = r'((?P<num>((?<= [n|N]o. )(\d*))|((?<=[n|N]r )(\d*)(?=[ |\(]))|((?<=num. )(\d*))|((?<=iss\. )(\d*)(?= ))|((?<=[i|I]ssue )(\d*))|(?<=Issue: )(\d*))|((?<=6 \()(3\d*))|((?<= 38\()(\d*))|((?<= 8 \()(\d*)))'
    vol = r'((?<=[v|V]ol\.\s)(?P<vol>(\d+))|(?<=[t|T]\.\s)(?P<t>(\d+)))'
    article_no = r'(?P<artnum>((?<=nr art\. )(\w+))|((?<=Article ID )(\w*)))'
    pages_in_range = r'(?P<pagrange>(\d+-\d+)|(\d+(?=\n)))'
    publisher_name = r'(?P<pubname>((?<=: )(.+)(?=\,\ \d\d\d\d))|((?<=: )(.+)(?=\, c))|((?<=: )(.+)(?= \\"\;\d\d\d\d))|((?<=: )(.+)(?=";S))|((?<=: )(.+)(?= \s))|((?<=: )(.+)(?= \\))|((?<=: )(.+)(?=;S)))'
    publisher_location = r'(?P<publoca>((\w+\S \w+(?= :))|(\w+(?=\s:))|(\w+-\w+(?=\s:))|((\w+ ; \w+)(?= ?:))|((\w+ ; \w+ \w+)(?= ?:))))'
    publisher_year = r'((?<= )(?P<pubyear>201\d))'

    pattern = [no, vol, article_no, pages_in_range, publisher_name, publisher_location, publisher_year]
    output = []

    with open('csv_input.csv', 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        input = csv_file.readlines()

    def write_header(self):

        with open('csv_output.csv', 'w', encoding='utf-8-sig', newline='') as file:
            column_header = ['no', "vol", "article_no", "pages_in_range", "publisher_name", "publisher_location",
                             "publisher_year"]
            writer = csv.DictWriter(file, fieldnames=column_header)
            writer.writeheader()

    def do_regex(self):
        all = []
        for row in RegEx.input:
            for i in range(len(RegEx.pattern)):

                if re.search("(%s)" % (RegEx.pattern[i]), row):
                    r = re.search("(%s)" % (RegEx.pattern[i]), row)
                    RegEx.output.append(r.group())
                else:
                    RegEx.output.append('')

            #print(RegEx.output)
            with open('csv_output.csv', 'a', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(RegEx.output)
                all.extend(RegEx.output)
                RegEx.output.clear()

        return all

def main():

    RE = RegEx()
    RE.write_header()
    RE.do_regex()

main()


