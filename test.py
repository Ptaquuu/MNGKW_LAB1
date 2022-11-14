# Łukasz PTAK WCY19KA1S0
# ZAD_1

import unittest
import csv
from main import RegEx

class Test(unittest.TestCase):
    def test_col1(self):
        input=[]
        with open('details.csv', 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                input.append(row[2])
        tmp=RegEx()
        all=tmp.do_regex()

        col1=[]
        for x in range(0, len(all), 7) :
            col1.append(all[x])

        i=0
        for x,z in zip(input,col1):
            if x==z:
                i+=1
        res = i / 7
        if (i >= 699):
            print("Result: ", (round(res, 2)))
        self.assertEqual(700,i,msg="Result: {}".format(round(res,2)))

    def test_col2(self):
        input=[]
        with open('details.csv', 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                input.append(row[3])
        tmp=RegEx()
        all=tmp.do_regex()

        col1=[]
        for x in range(1, len(all), 7) :
            col1.append(all[x])
        i=0
        for x,z in zip(input,col1):
            if x==z:
                i+=1
        res = i / 7
        if (i >= 699):
            print("Result: ", (round(res, 2)))
        self.assertEqual(700,i,msg="Result: {}".format(round(res,2)))

    def test_col3(self):
        input=[]
        with open('details.csv', 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                input.append(row[4])
        tmp=RegEx()
        all=tmp.do_regex()

        col1=[]
        for x in range(2, len(all), 7) :
            col1.append(all[x])

        i=0
        for x,z in zip(input,col1):
            if x==z:
                i+=1
        res = i / 7

        self.assertEqual(700,i,msg="Result: {}".format(round(res,2)))

    def test_col4(self):
        input=[]
        with open('details.csv', 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                input.append(row[5])
        tmp=RegEx()
        all=tmp.do_regex()

        col1=[]
        for x in range(3, len(all), 7) :
            col1.append(all[x])
        i=0
        for x,z in zip(input,col1):
            if x==z:
                i+=1
        res = i / 7
        if (i >= 699):
            print("Result: ", (round(res, 2)))
        self.assertEqual(700,i,msg="Result: {}".format(round(res,2)))

    def test_col5(self):
        input=[]
        with open('details.csv', 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                input.append(row[7])
        tmp=RegEx()
        all=tmp.do_regex()

        col1=[]
        for x in range(4, len(all), 7) :
            col1.append(all[x])
        i=0
        for x,z in zip(input,col1):
            if x==z:
                i+=1
        res = i / 7
        if (i >= 699):
            print("Result: ", (round(res, 2)))
        self.assertEqual(700,i,msg="Result: {}".format(round(res,2)))

    def test_col6(self):
        input=[]
        with open('details.csv', 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                input.append(row[8])
        tmp=RegEx()
        all=tmp.do_regex()

        col1=[]
        for x in range(5, len(all), 7) :
            col1.append(all[x])
        i=0
        for x,z in zip(input,col1):
            if x==z:
                i+=1
        res = i / 7
        if (i >= 699):
            print("Result: ", (round(res, 2)))
        self.assertEqual(700,i,msg="Result: {}".format(round(res,2)))

    def test_col7(self):
        input=[]
        with open('details.csv', 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                input.append(row[9])
        tmp=RegEx()
        all=tmp.do_regex()

        col1=[]
        for x in range(6, len(all), 7) :
            col1.append(all[x])
        i=0
        for x,z in zip(input,col1):
            if x==z:
                i+=1
        res = i / 7
        if (i >= 699):
            print("Result: ", (round(res, 2)))
        self.assertEqual(700,i,msg="Result: {}".format(round(res,2)))

if __name__ =='__main__':
    unittest.main()