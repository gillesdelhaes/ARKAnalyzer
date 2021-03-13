#!/usr/bin/python3
import sys
import csv

def ReadARKFile(file):
    print(file)
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['fund'] != '':
                print(row)

if __name__ == '__main__':
    ReadARKFile('../data/2021-03-13_ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv')