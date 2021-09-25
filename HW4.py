"""
Здесь вам нужно реализовать несколько фукнкций.
Для каждой функции есть другая тестовая функция, которая ее проверяет.
Чтобы убедиться, что ваше решение работает запустите ее.
Если функция нвзывется some_function, то тестирующия функция называется test_some_function.
Для проверки просто запустите тестирующую функцию, если после запуска увидели сообщение
Great your solution works! значит все ок!
Если возникла ошибка AssertionError значит решение не работает.
Если вдруг вы нашли ошибку в тестах, пишите в чат мы обсудим.
Краткая заметка. Прочитайте про оператор включения in в коллекциях.
https://www.geeksforgeeks.org/python-membership-identity-operators-not-not/
"""


def count_greater_or_equal(numbers, x):
     assert_list = []
     for i in numbers:
         if i >= x:
            assert_list += [i]
     return len(assert_list)


def test_count_greater_or_equal():
    assert count_greater_or_equal([1, 2, 3, 4, 5], 2) == 4
    assert count_greater_or_equal([1, 2, 3, 4, 5], 1) == 5
    assert count_greater_or_equal([1, 2, 3, 4, 5], 0) == 5
    assert count_greater_or_equal([0, 1], 2) == 0
    assert count_greater_or_equal([], 2) == 0
    print("Great your solution works!")


def rotate(numbers, n):
    time = 0
    if len(numbers) > 0:
        while time < n:
            numbers = [numbers[-1]] + numbers[:-1]
            time += 1
    return numbers



def test_rotate():
    assert rotate([1, 2, 3], 1) == [3, 1, 2]
    assert rotate([1, 2, 3], 2) == [2, 3, 1]
    assert rotate([1, 2, 3], 3) == [1, 2, 3]
    assert rotate([1, 2, 3], 0) == [1, 2, 3]
    assert rotate([1], 1) == [1]
    assert rotate([1], 0) == [1]
    assert rotate([], 2) == []
    print("Great your solution works!")


def extend(a, b):
    return a + b


def test_extend():
    assert extend([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert extend([4, 5, 6], [1, 2, 3], ) == [4, 5, 6, 1, 2, 3]
    assert extend([], [4, 5, 6]) == [4, 5, 6]
    assert extend([1, 2, 3], []) == [1, 2, 3]
    assert extend([1], [4]) == [1, 4]
    print("Great your solution works!")


def is_prime(n):
    if n != 0 and (n % n == 0 and n // 1 == n and n != 1 and n % 2 != 0) or n == 2:
        n = True
    else:
        n = False
    return n
# заранее извиняюсь за такое количество or и and, я решил что так и должно быть, ведь в задаче есть исключения в виде 0, 1, 2

def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(24) is False
    assert is_prime(5) is True
    assert is_prime(0) is False
    assert is_prime(107) is True
    assert is_prime(19) is True
    print("Great your solution works!")


def merge(a, b):
    list = a + b
    copy_list = []

    while len(list) > 0:
        copy_list.append(min(list))
        list.remove(min(list))
    return copy_list



def test_merge():
    assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
    assert merge([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]
    assert merge([4, 5, 6], []) == [4, 5, 6]
    assert merge([], [1, 3, 5]) == [1, 3, 5]
    assert merge([], []) == []
    print("Great your solution works!")


def has_substring(s, t):
    n = 1
    z = False
    if len(t) == 0 or (len(s) == 0 and len(t) == 0):
        z = True
    else:
        first_sym = t[0]
        for i in range(len(s)):
            if s[i] == first_sym:
                while n < len(t):
                    if s[i + n] == t[0 + n]:
                        n += 1
                        z = True
                        continue
                    else:
                        z = False
                break
            else:
                z = False
    return z


def test_has_substring():
    assert has_substring("some text", "text") is True
    assert has_substring("some text", "some") is True
    assert has_substring("", "text") is False
    assert has_substring("text", "") is True  # любая строка содержит в себе пустую подстроку
    assert has_substring("", "") is True  # даже пустая строка содержит в себе пустую подстроку :)
    print("Great your solution works!")