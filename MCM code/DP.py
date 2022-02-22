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


BCHAIN = "BCHAIN"
GOLD = "GOLD"

class budget:
    def __init__(self, initial_money):
        self.money = initial_money

        self.bchain_stock = 0
        self.bchain_cost = 0

        self.gold_stock = 0
        self.gold_cost = 0

        self.log = []
    
    def get_stock(self, stock_type):
        if stock_type == BCHAIN:
            return self.bchain_stock
        elif stock_type == GOLD:
            return self.gold_stock

    def addLog(self, add_v):
        self.log.append(add_v)

    def getLog(self):
        return self.log

    def add_stock(self, price, num_stock, stock_type):
        if stock_type == BCHAIN:
            self.bchain_cost = self.bchain_cost * self.bchain_stock + price * num_stock
            self.bchain_stock += num_stock
            self.bchain_cost /= self.bchain_stock

        elif stock_type == GOLD:
            self.gold_cost = self.gold_cost * self.gold_stock + price * num_stock
            self.gold_stock += num_stock
            self.gold_cost /= self.gold_stock


    def buy(self, stock_type, current_price, percent, day):
        spent = self.money * percent
        self.money -= spent
        stock_bought = spent / current_price

        self.add_stock(current_price, stock_bought, stock_type)
        if stock_bought != 0:
            self.log.append([day, stock_type, stock_bought, self.get_stock(stock_type), self.money, self.get_stock(stock_type) * current_price + self.money])
        

    def sell(self, stock_type, current_price, percent, day):
        stock_sold = 0
        if stock_type == BCHAIN:
            stock_sold = self.bchain_stock * percent
            self.bchain_stock -= stock_sold
    
        if stock_type == GOLD:
            stock_sold = self.gold_stock * percent
            self.gold_stock -= stock_sold
        
        self.money +=  stock_sold * current_price
        if stock_sold != 0:
            self.log.append([day, stock_type, -stock_sold, self.get_stock(stock_type), self.money, self.get_stock(stock_type) * current_price + self.money])






# Check the proliximity of the predict data
def validity(predict, truth, trace_day, current_index):
    val = 0
    for i in range(current_index - 10, current_index):
        val += abs(predict[i][0] - truth[i]) / truth[i]
    val = val / trace_day
    return val


def valid_date(predict, truth):
    error = 0.1
    trace_day = 10;

    for i in range(trace_day, len(predict)):
        if validity(predict, truth, trace_day, i) < error:
            return i
    return -1


def getSingleMa(data, current_index, ma):
    return sum(data[current_index - ma + 1: current_index + 1]) / ma

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


def curve_intersect(curve1, curve2):
    if curve1[0] < curve2[0] and curve1[1] > curve2[1]:
        return 1
    
    if curve1[0] > curve2[0] and curve1[1] < curve2[1]:
        return -1
    
    return 0


def getPrediction(predict, current_index):
    result = []
    for i in range(1, 1 + len(predict[current_index])):
        result.append(predict[current_index + i][-i])
    return result


#--------------------------------------------------------------------------------------------------
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

print(valid_date(predict, ground_truth))

# Initial condition
current_budget = budget(1000)
sell_percent = 1
buy_percent = 1

# Calculate MA
ma_list = getMa([5, 30], ground_truth)
ma5 = ma_list[0]
ma30 = ma_list[1]


# Start simulation
for i in range(31, len(ground_truth)):
    current_price = ground_truth[i]
    '''
    intersect = curve_intersect([ma5[i-1], ma5[i]], [ma30[i-1], ma30[i]])
    
    if intersect == 1:
        current_budget.buy(BCHAIN, current_price, buy_percent, i)
    if intersect == -1:
        current_budget.sell(BCHAIN, current_price, sell_percent, i)
    '''
    
    
    # Before the ml data's validity small enough to use: directly use daily ma
    if i < valid_date(predict, ground_truth) or i >= len(ground_truth) - predicted_day * 2:
        intersect = curve_intersect([ma5[i-1], ma5[i]], [ma30[i-1], ma30[i]])
        
        if intersect == 1:
            current_budget.buy(BCHAIN, current_price, buy_percent, i)
        if intersect == -1:
            current_budget.sell(BCHAIN, current_price, sell_percent, i)

    # Once the ml data's validity small enough to use: Use ML data to sell/buy ahead
    else:
        predicted_ma = getMa([5, 30], ground_truth[i - 31 : i + 1] + getPrediction(predict, i))
        predicted_ma5 = predicted_ma[0]
        predicted_ma30 = predicted_ma[1]
        #print(i, predicted_ma, getPrediction(predict, i))


        for j in range(1, predicted_day + 1):
            intersect = curve_intersect([predicted_ma5[-(j + 1)], predicted_ma5[-j]], [predicted_ma30[-j - 1], predicted_ma30[-j]])
            if intersect == 1:
                current_budget.buy(BCHAIN, current_price, buy_percent, i)
                break

            if intersect == -1:
                current_budget.sell(BCHAIN, current_price, sell_percent, i)
                break
    
    
'''
    if i == 250:
        break
'''

print(current_budget.getLog()[-1][-1] + current_budget.getLog()[-1][-2] * ground_truth[-1])

'''
for i in range(31, 300):
    print(i, ma_list[0][i], ma_list[1][i])
'''

final_value = current_budget.getLog()[-1].copy()
final_value[0] = len(ground_truth) - 1
final_value[-1] = final_value[-2] + final_value[-3] * ground_truth[-1]
current_budget.addLog(final_value)

log_df = pd.DataFrame(current_budget.getLog())
print(log_df)
log_df.to_csv("log.csv", index = False, sep = ',')