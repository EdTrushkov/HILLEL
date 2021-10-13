"""Нужно написать программу, которая угадывает число загаданное пользователем в диапазоне от 1 до 100.

При запуске программа задает вопрос: "Is x guessed number?", где х - это предположение программы. В ответ пользователь вводит yes если х это загаданное им число, no - если нет.

Программа завершает работу если угадала и печатает сколько вопросов она задала. Если не угадала продолжает спрашивать до тех пор пока не угадает. """


from random import choice

n = 0
numbers = [i for i in range(1, 101)]
while n <= 100:
    x = choice(numbers)
    print(f"Is {x} guessed number?")
    answer = input()
    if answer.lower() == "yes":
        print(n)
        break
    elif answer.lower() == "no":
        numbers.remove(x)
        n += 1
    else:
        print("Incorrect enter, try one more!")