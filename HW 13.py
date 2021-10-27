'''Напишите программа, которая считывает слова из файла 'in.txt", фильтрует все длина которых больше 5 и пишет их в файл

"out.txt".

Пример входных данных в файле:

a ab abc abcd abcde abcdef'''

file_read = open('in.txt', 'r')
file_write = open('out.txt', 'w')
try:
    for i in file_read:
        line = list(i.split())
        for j in line:
            if len(j) >= 5:
                file_write.write(j)
                file_write.write(' ')
except:
    file_read.close()
    file_write.close()
