import csv
import xlwt
import statistics
from datetime import datetime

# Cast date to correct python date format
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

# Write date to the sheet
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


# Calculate ma (Moving Average)
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
# Open the given file and extract data
with open('BCHAIN-MKPRU.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        try:
            value.append(float(row[0].split(',')[1]))
            date.append(make_date(row[0].split(',')[0]))
        except:
            continue

# Calculate MA
ma_list = [5, 10, 20, 30, 60]
ma_value = getMa(ma_list, value)


# Write to book and save
workbook = xlwt.Workbook(encoding='utf-8')
sheet1 = workbook.add_sheet('BCHAIN')
write_to_book(sheet1, value, ma_list, ma_value,  date)
workbook.save('./BCHAIN.xls')

