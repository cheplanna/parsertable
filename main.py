import csv
import pickle
from datetime import datetime
from tabulate import tabulate

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
        file_reader = csv.reader(file, delimiter=",")  # преобразуем файл в лист листов
        table_key_dictionary = {}  # Создаем словарь атрибутов таблицы и записываем их номер
        # Счетчик для подсчета количества строк
        lines_count = 0  # Считаем номер строки
        # Считывание данных из CSV файла
        for row in file_reader:  # Проходимся по строкам таблицы
            if lines_count == 0:  # В первой строк находяться атрибуты, создаем ключи в словаре
                key_count = 0
                for i in row:
                    dictionary[i] = []
                    table_key_dictionary[key_count] = i
                    key_count += 1
            else:
                key_count = 0
                for i in row:
                    dictionary.get(table_key_dictionary.get(key_count)).append(
                        i)  # Записываем нужный столбик нужный элемент
                    key_count += 1
            lines_count += 1
    else:
        return -1
    return dictionary

def save_table(data, type='txt'):
    if type == 'csv':
        temp_table = []
        field_names = data.keys()
        num_of_colums = 0
        for i in field_names:
            num_of_colums = max(num_of_colums, len(data[i]))
        for i in range(0, num_of_colums):
            values = dict.fromkeys(field_names)
            for j in field_names:
                if i < len(data[j]):
                    values[j] = data[j][i]
            temp_table.append(values)
        print(temp_table)
        with open('NewFile2' + '.csv', 'a+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(temp_table)

    elif type == 'pickle':
        with open('NewFile1' + '.pickle', 'wb') as f:
            pickle.dump(data, f)
        f.close()

    elif type == 'txt':
        with open('NewFile1' + '.txt', 'w') as f:
            data = temp_data
            len_of_col = {}  # СЛОВАРЬ ДЛЯ ХРАНЕНИЯ ДЛИНЫ СТОЛБЦОВ
            max_l = 0
            for i in data:  # ПЕРЕБОР СЛОВАРЯ ПО ВСЕМ СЛОВАМ И ЗНАЧЕНИЯМ
                if len(i) > max_l:  # НАХОЖДЕНИЕ САМОГО ДЛИННОГО СЛОВА
                    max_l = len(i)
                for j in data[i]:
                    if len(str(j)) > max_l:
                        max_l = len(str(j))
                len_of_col[i] = max_l  # ЗАПОЛНЕНИЯ СЛОВАРЯ МАКСИМАЛЬНЫМИ ДЛИНАМИ

            field_names_len = {}
            for i in len_of_col:  # ФОРМИРОВАНИЕ РОВНЫХ СТОЛБЦОВ
                temp_key = i
                if len(i) < len_of_col[i]:
                    while len(i) < len_of_col[temp_key]:
                        i = i + ' '
                print(i + '|', file=f, end="")
                field_names_len[i] = len_of_col[temp_key]
            print(file=f)

            num_str = 0
            while True:
                try:
                    for i in data:  # ДОБАВЛЕНИЕ ПРОБЕЛОВ ДЛЯ РОВНЫХ СТОЛБЦОВ
                        temp = str(data[i][num_str])
                        if len(temp) < len_of_col[i]:
                            while len(temp) < len_of_col[i]:
                                temp += ' '
                        temp += '|'
                        print(temp, file=f, end='')
                    print(file=f)
                    num_str += 1
                except IndexError:
                    break
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



load_table('Example', type="csv")
save_table(temp_data, type='csv')

print_table()
new = get_values(3)
print(new)
