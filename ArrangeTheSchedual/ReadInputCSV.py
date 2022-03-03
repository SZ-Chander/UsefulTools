# -*- coding: utf-8 -*-
import os

def ReadInputCSV(inputpath):
    try:
        with open(inputpath,encoding='gbk') as csv_r:
            csv = csv_r.readlines()
    except:
        with open(inputpath,encoding='utf-8') as csv_r:
            csv = csv_r.readlines()
    new_csv = []
    for line in csv:
        line = line.replace(' ','')
        line = line.split(',')
        new_csv.append(line)
    return new_csv

if __name__ == '__main__':
    inputpath = "/Users/szchandler/Desktop/VScodePy/ForMUJI/TestFiles/人员表.csv"
    csv = ReadInputCSV(inputpath)
    print(csv)