import csv
import pickle
from datetime import datetime
from tabulate import tabulate
import pandas


d1=datetime(2005,7,14,4,2)
d2=datetime(2006,7,14)
d3=datetime(2007,7,14)
d4=datetime(2008,7,14)

temp_data = {'Number': [1, 2, 3], 'first_name': ['Alex', 'Ann', 'Amy', 'Kate'],
             'last_name': ['Brian', 'Bon', 'Bron', 'Jons'], 'grade': ['A', 'B', 'C', 'A'], 'date': [d1, d2, d3, d4]}

temp_spisok = ['1', '2', '3', '4', '5']

types_dict = {}


def load_table(file, type="csv"):
    dictionary = {}  # Храним таблицу
    if type == "pickle":  # Считываем таблицу используя pickle
        dictionary = pickle.load(file)
    elif type == "csv":  # Считываем таблицу используя csv
        dictionary = pandas.read_csv(file)
        print(dictionary)
    else:
        return -1
    return dictionary

def save_table(data, type='txt'):
    if type == 'csv':
        table = pandas.read_csv('NewFile2.csv')
        table.to_csv('Filek.csv')
    elif type == 'pickle':
        with open('Filek' + '.pickle', 'wb') as f:
            pickle.dump(data, f)
        f.close()

    elif type == 'txt':
        with open('Filek' + '.txt', 'w') as f:
            data = temp_data
            f.write(tabulate(data, headers='keys', tablefmt="grid"))
        f.close()

def set_values(values, column=''):
    if column == '':
        column = 0
    try:
        field_names = []
        for i in temp_data:
            field_names.append(i)
        if type(column) == int:
            temp_data[field_names[column]] = values
        else:
            temp_data[column] = values
        save_table(temp_data)
    except IndexError:
        print('Ошибка: номер столбца выбран неверно!')
    except KeyError:
        print('Ошибка: имя столбца введено неверно!')


def set_value(value, column=''):
    if column == '':
        column = 0
    try:
        field_names = []
        for i in temp_data:
            field_names.append(i)

        if type(column) == int:
            values = temp_data[field_names[column]]
            values[0] = str(value)
            temp_data[field_names[column]] = values
        else:
            values = temp_data[column]
            values[0] = str(value)
            temp_data[column] = values
        save_table(temp_data)
    except IndexError:
        print('Ошибка: номер столбца выбран неверно!')
    except KeyError:
        print('Ошибка: имя столбца введено неверно!')


def get_values(column=''):
    if column == '':
        column = 0
    try:
        field_names = []
        for i in temp_data:
            field_names.append(i)
        if type(column) == int:
            return temp_data[field_names[column]]
        else:
            return temp_data[column]
        save_table(temp_data)
    except IndexError:
        print('Ошибка: номер столбца выбран неверно!')
    except KeyError:
        print('Ошибка: имя столбца введено неверно!')


def get_value(column=''):
    if column == '':
        column = 0
    try:
        field_names = []
        for i in temp_data:
            field_names.append(i)
        if type(column) == int:
            return temp_data[field_names[column]][0]
        else:
            return temp_data[column][0]
        save_table(temp_data)
    except IndexError:
        print('Ошибка: номер столбца выбран неверно!')
    except KeyError:
        print('Ошибка: имя столбца введено неверно!')


def get_rows_by_number(start: int, stop=-1, copy_table=False):
    try:
        if stop == -1:
            stop = start + 1
        field_names = []
        ans = {}
        for i in temp_data:
            field_names.append(i)
        for l in field_names:
            ans[l] = []
        for i in range(start, stop):
            for l in field_names:
                ans[l].append(temp_data[l][i])
        return ans
    except IndexError:
        print('Ошибка: диапазон номеров столбцов выбран неверно!')


def get_rows_by_index(*argv, copy_table=False):
    field_names = []
    ans = {}
    for i in temp_data:
        field_names.append(i)
    for l in field_names:
        ans[l] = []
    for i in range(len(list(temp_data.values())[0])):
        v = list(temp_data.values())[0][i]
        if v in argv:
            for l in field_names:
                ans[l].append(temp_data[l][i])
    return ans


def get_column_types(by_number=True):
    ans = {}
    keys = list(temp_data.keys())
    for i in range(len(keys)):
        if by_number:
            ans[i] = type(temp_data[keys[i]][0]).__name__
        else:
            ans[keys[i]] = type(temp_data[keys[i]][0]).__name__
    return ans

def print_table():
    data = temp_data
    print(tabulate(data, headers='keys', tablefmt="grid"))
