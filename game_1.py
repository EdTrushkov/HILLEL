
'''
Реализовать игру виселица. Правила следующие:
1. Слово задаем заранее (присваиваем переменной значение хардкодом)
2. Количество попыток для отгадывания = кол-во букв в слове * 2
3. В начале игры выводим кол-во букв в слове и кол-во попыток
4. Необходимо проверять ввод:
   - нельзя вводить пустую строку: счетчик не уменьшаем
   - нельзя вводить цифры: счетчик не уменьшаем
   - нельзя вводить букву второй раз: счетчик не уменьшаем
5. Если буква встречается в слове несколько раз, пользователю достаточно угадать ее один раз
6. Если пользователь угадал букву, он видит следующий вывод: 
   отгаданные буквына своих местах, неотгаданные - заменены на прочерки (_).
   hello h_ll_o
7. В случае проиграша игрок видит статистику: сколько букв было в слове и сколько он отгадал
'''
'''
word = 'наше слово'
counter = 'счетчик = длина слона * 2'
used_letters = set('использованные буквы')
result = list('промежуточный результат')
gessed_leters = ['отгаданные буквы для статистики']
'''
'''
цикл while True
Условия остановки игры:
1. Если слово угадано list(word) == result
2. Если закончились попытки counter == 0

Если угадали букву:
Получить индекс буквы
Обновляем result: заменяем элемент с индексом на букву
Если буква встречается несколько раз - используем доп.цикл

Проверки:
1. На пустую строку len(строка) == 0 строка == ''
2. Цифра вхождение в массив 0-9, строка.isdigit()
3. Повтор буквы, вхождение в массив used_letters

Формирование результата:
word = 'hello'
result = list('_' * len(word))
print(*result)
'''
word = str(input().lower()) #'наше слово'
counter = len(word) * 2     #'счетчик = длина слона * 2'
hiden_word = list(len(word) * "_")
used_letters = set()        #'использованные буквы')
result = list()               #('промежуточный результат')
gessed_letters = set()       #['отгаданные буквы для статистики']
while counter > 0:
    print(f"Your word: {' '.join(hiden_word)}\n Gessed letters: {' '.join(gessed_letters)}\n Used letters: {' '.join(used_letters)}\n Attempts left: {counter}\n Enter letter:", end = " ")
    t_letter = str(input().lower())     # t_letter - временная введенная буква
    if t_letter in used_letters or t_letter.isdigit() == True:
        print("You already used this letter or you used numbers. Be more attentively you lose 1 attempts")
        counter -= 1
    elif len(t_letter) >= 2:
        z = 0
        while z < 9000000:
            print("You are cheating, enter just ONE letter:", end = " ")
            t_letter = str(input())
            if len(t_letter) > 1:
                z += 1
                continue
            elif len(t_letter) == 1:
                break
    elif len(t_letter) == 1:
        for i in range(len(word)):
            if t_letter == word[i]:
                hiden_word[i] = word[i]
                print("Nice, good job")
                gessed_letters.add(t_letter)
                result += t_letter
        if t_letter not in word:
            counter -= 1
        used_letters.add(t_letter)
    if len(hiden_word) == len(result):
        print('You WINNER')
        break




























































