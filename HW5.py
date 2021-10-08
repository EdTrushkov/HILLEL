"""
Здесь вам нужно реализовать несколько фукнкций.
Для каждой функции есть другая тестовая функция, которая ее проверяет.
Чтобы убедиться, что ваше решение работает запустите ее.
Если функция нвзывется some_function, то тестирующия функция называется test_some_function.
Для проверки просто запустите тестирующую функцию, если после запуска увидели сообщение
Great your solution works! значит все ок!
Если возникла ошибка AssertionError значит решение не работает.
Если вдруг вы нашли ошибку в тестах, пишите в чат мы обсудим.
"""


def unique(numbers):
    b = set()
    b.update(numbers)
    return list(b)


def test_unique():
    assert unique([1, 1, 2, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]
    assert unique([1, 1, 1, 1]) == [1]
    assert unique([]) == []


def count_words(string):
    res = dict()
    for i in string:
        if i in res:
            res[i] += 1
        elif i not in res:
            res[i] = 1
    return res


def test_count_words():
    assert count_words(["text", "text", "apple", "orange", "yellow", "orange"]) == {
        "text": 2,
        "orange": 2,
        "yellow": 1,
        "apple": 1
    }
    assert count_words(["text", "text", "text", "text", "text", "orange"]) == {
        "text": 5,
        "orange": 1,
    }
    assert count_words([]) == {}


def consistent_string(strings, allowed):
    set_allowed = set(allowed)
    result = set()
    for i in strings:
        if len(set_allowed & set(i)) == len(set(i)):
            result.add(i)
    return result


def test_consistent_string():
    assert consistent_string(allowed="ab", strings=["ad", "bd", "aaab", "baa", "badab"]) == {"aaab", "baa"}
    assert consistent_string(allowed="abc", strings=["a", "b", "c", "ab", "ac", "bc", "abc"]) == {"a", "b", "c", "ab",
                                                                                                  "ac", "bc", "abc"}
    assert consistent_string(allowed="cad", strings=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == {"cc", "acd",
                                                                                                           "ac", "d"}


def sort_desc(strings):
    return sorted(strings, reverse=True)


def test_sort_desc():
    assert sort_desc(["ad", "bd", "aaab", "baa", "badab"]) == ['bd', 'badab', 'baa', 'ad', 'aaab']
    assert sort_desc(["a", "b", "c", "ab", "ac", "bc", "abc"]) == ['c', 'bc', 'b', 'ac', 'abc', 'ab', 'a']


def filter_even(numbers):
    return  sorted(list(filter(lambda x: x % 2 == 0, numbers)))


def test_filter_even():
    assert filter_even([1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12]) == [2, 4, 6, 8, 10, 12]
    assert filter_even([2, 2, 4, 6, 6, 8, 10, 12]) == [2, 2, 4, 6, 6, 8, 10, 12]
    assert filter_even([1, 1, 2, 3]) == [2]
    assert filter_even([1, 3, 5]) == []

