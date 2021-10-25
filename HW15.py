'''Напишите программа, которая считывает числа из файла 'in.txt", сортирует и пишет их в файл

"out.txt".

Пример входных данных в файле:

2 3 1 4 5 9 7

Пример выходных данных в файле:

1 2 3 4 5 7 9'''

file_read = open('in.txt', 'r')
file_write = open('out.txt', 'w')
try:
    for i in file_read:
        line = list(i.split())
        line.sort()
        for j in line:
            file_write.write(j)
            file_write.write(' ')
except:
    file_read.close()
    file_write.close()