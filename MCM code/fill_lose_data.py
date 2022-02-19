import csv
import xlwt
import statistics
from datetime import datetime, timedelta


def make_date(data):
    data_list = data.split('/')

    data_str = ""
    for i in range(0, 2):
        if len(data_list[i]) == 1:
            data_list[i] = '0' + data_list[i]
        data_str += data_list[i] + '/'
    data_list[-1] = '20' + data_list[-1]
    data_str += data_list[-1]

    return datetime.strptime(data_str, '%m/%d/%Y')    


def write_to_book(sheet, value, ma_list, ma_value, date):
    shift = 3;
    for i in range(shift, len(ma_list) + shift):
        sheet.write(0, i, 'ma' + str(ma_list[i - shift]))

    sheet.write(0, 0, 'index')
    sheet.write(0, 1, 'date')
    sheet.write(0, 2, 'value')

    for row in range(0, len(date)):
        sheet.write(row + 1, 1, date[row])
        sheet.write(row + 1, 2, value[row])
        sheet.write(row + 1, 0, row)

    for col in range(0, len(ma_value)):
        for row in range(0, len(ma_value[col])):
            if (ma_value[col][row] != ''):
                sheet.write(row + 1, col + shift, float(ma_value[col][row]))


def getMa(ma_list, value):
    ma_value = []
    for i in ma_list:
        ma_value.append([])
        
    for i in range(0, len(value)):
        for j in range(0, len(ma_list)):
            if i - ma_list[j] < 0:
                ma_value[j].append('')
            else:
                ma_value[j].append("{:.2f}".format(statistics.mean(value[i - ma_list[j] : i])))
    return ma_value



value = []
date = []
with open('LBMA-GOLD.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        try:
            today_value = float(row[0].split(',')[1])
            today = make_date(row[0].split(',')[0])

            if len(date) > 0 and date[-1] != today - timedelta(days=1):
                date.append(date[-1] + timedelta(days=1))
                date.append(date[-1] + timedelta(days=1))
                value.append(value[-1])
                value.append(value[-1])

            date.append(today)
            value.append(today_value)
        except Exception as e:
            print(e)
            continue


'''
for i in range(0, len(date)):
    print(date[i], value[i])
'''

ma_list = [5, 10, 20, 30, 60]
ma_value = getMa(ma_list, value)

workbook = xlwt.Workbook(encoding='utf-8')
sheet1 = workbook.add_sheet('GOLD')
write_to_book(sheet1, value, ma_list, ma_value,  date)
workbook.save('./GOLD.xls')
