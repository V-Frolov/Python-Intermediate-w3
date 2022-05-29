# Напишите программу, которая будет считывать содержимое файла, добавлять к
# считанным строкам порядковый номер и сохранять их в таком виде в новом файле.
# Имя исходного файла необходимо запросить у пользователя, так же, как и имя
# целевого файла. Каждая строка в созданном файле должна начинаться с ее номера,
# двоеточия и пробела, после чего должен идти текст строки из исходного файла.

file_source = input('Enter source file name: ')
file_dest = input('Enter destination file name: ')

counter = 1
with open(file_source, 'r', encoding="utf8") as f_s, open(file_dest, 'w', encoding="utf8") as f_d:
    for line in f_s:
        print(str(counter) + ': ' + line, file=f_d, end="")
        counter += 1
