'''
1. Вручную создайте текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
    car_date_txt.py
2. Создайте шаблон документа doc

3. Внесите данные из файла в шаблон

4. Создайте csv-файл с данными о машине.

5. Создайте json-файл с данными о машине.
'''

#
from docxtpl import DocxTemplate
import jinja2
import json
import datetime
import csv

# Задание №1
#1. Вручную создайте текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).

dict_car_data = {
    'Brand': 'Volvo',
    'Model': 'CX90',
    'Fuel consumption, l': 12,
    'Price': 1500000
    }
car_data = json.dumps(dict_car_data)

with open('car_data.txt', 'w') as f: # вывод в файл car_date_txt.py
    json.dump(dict_car_data, f)

with open('car_data.txt') as f:
    car_data_imp = json.load(f)

print('Задание №1: Текстовый файл <car_date.txt> с данными об автомобиле - CREATED! \n',car_data_imp, '\n')


# Задание №2-№3
# 2. Создайте шаблон документа doc
# 3. Внесите данные из файла в шаблон

report_doc = DocxTemplate("template_car_data.docx")
with open('car_data.txt', 'r') as f: #импортируем данные из файла txt и приводим их к словарю
    car_param_data = f.read()
    dict_car_data = json.loads(car_param_data.replace("'", '"'))
    context = {
        'car_param_1': dict_car_data['Brand'],
        'car_param_2': dict_car_data['Model'],
        'car_param_3': dict_car_data['Fuel consumption, l'],
        'car_param_4': dict_car_data['Price'],
        'date_param': datetime.date.today(),
        'car_param_5': 'PYTHON'
    }
    report_doc.render(context)
    report_doc.save("generated_car_report.docx")
print('Задание №№2-3: Создайте шаблон документа doc (template_car_data.docx) и внесение данных из файла car_data.txt в шаблон \n', 'Файл <generated_car_report.docx> - CREATED!', '\n' )


# Задание №4
# 4. Создайте csv-файл с данными о машине.

with open('car_data.csv', 'w') as f:
    writer = csv.writer(f, delimiter=':')
    for key, value in dict_car_data.items():
       writer.writerow([key, value])

with open('car_data.csv') as f:
    reader = csv.reader(f,delimiter = ':')
    print('Задание №4: Создайте csv-файла и извлечение из него данных:', '\n')
    for row in reader:
        if len(row)>0:
            print(row)



# Задание №5
# 5. Создайте json-файл с данными о машине

with open('json_car_data.txt', 'w') as f:
    json.dump(dict_car_data, f)

# чтение Json-файла:
with open('json_car_data.txt', 'r') as f:
    open_json_file = json.load(f)
print('Задание №5: создание Json-файла и извлечение из него данных:\n',open_json_file)
