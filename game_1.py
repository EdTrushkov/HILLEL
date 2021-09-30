
word = str(input("Enter your word: ").lower()) #'наше слово'
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
      
      
      
      
