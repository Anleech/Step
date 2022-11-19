import csv

# with open("data.csv") as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит: {', '.join(row)}")
#         else:
#             print(f"    {row[0]} - {row[1]}. Родился в {row[2]} году")
#         count += 1
#     print(f"Всего в файле {count} строки")

# with open("data.csv") as r_file:
#     field_names = ['Имя',  'Профессия',  'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит: {', '.join(row)}")
#         print(f"{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году")
#         count += 1

# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_new.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=',', lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('data_new.csv') as f:
#     print(f.read())

with open('student1.csv', 'w') as f:
    names = ["Имя", "Возраст"]
    file_writer = csv.DictWriter(f, delimiter=";", lineterminator='\r',fieldnames=names)
    file_writer.writeheader()
    file_writer.writerow(["Женя", "9", "15"])
    file_writer.writerow(["Саша", "5", "12"])
    file_writer.writerow(["Маша", "11", "18"]
