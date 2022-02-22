from audioop import bias
import csv
from hashlib import md5
import xlwt
import statistics
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def getPrediction(predict, current_index):
    result = []
    for i in range(1, 1 + len(predict[current_index])):
        result.append(predict[current_index + i][-i])
    return result

def getMa(ma_list, value):
    ma_value = []
    for i in ma_list:
        ma_value.append([])
        
    for i in range(0, len(value)):
        for j in range(0, len(ma_list)):
            if i - ma_list[j] < 0:
                ma_value[j].append(-1)
            else:
                ma_value[j].append(statistics.mean(value[i - ma_list[j] : i]))
    return ma_value

predict = []
ground_truth = []
predicted_day = 5

# Open the given file and extract data
with open('outputs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        try:
            ground_truth.append(float(row[-1]))
            predict.append([])
            for i in range(1, len(row) - 1):
                predict[-1].append(float(row[i].split(',')[0]))
        except Exception as e:
            print(e)
            continue

ma_list = getMa([5, 30], ground_truth)
ma5 = ma_list[0]

for i in range(10, len(ground_truth) - 10):
    getPrediction(predict, i)