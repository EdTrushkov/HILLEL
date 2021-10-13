from random import choice


def cinderella(mixed_cereals, pattern): #-> list:
    return list(filter(lambda mixed_cereals: pattern in mixed_cereals, mixed_cereals))


def check_cinderella():
    assert cinderella(['мак', 'просо', 'мак', 'пшеница', 'пшеница', 'пшеница'], 'мак') == ['мак', 'мак']
    assert cinderella(['мак', 'просо', 'мак', 'пшеница', 'пшеница', 'пшеница'], 'просо') == ['просо']
    assert cinderella(['мак', 'просо', 'мак', 'пшеница', 'пшеница', 'пшеница'], 'пшеница') == ['пшеница', 'пшеница', 'пшеница']
    print('It works!')


check_cinderella()


def even_numbers(list_of_numbers: list, check_even: bool): # -> list:
    if check_even == True:
        return list(filter(lambda x: x % 2 == 0, list_of_numbers))
    if check_even == False:
        return list(filter(lambda x: x % 2 != 0, list_of_numbers))


def check_even_numbers():
    assert even_numbers([1, 2, 3, 4, 5, 6], True) == [2, 4, 6]
    assert even_numbers([1, 2, 3, 4, 5, 6], False) == [1, 3, 5]
    assert even_numbers([11, 22, 33, 45, 55, 64], False) == [11, 33, 45, 55]
    assert even_numbers([11, 22, 33, 45, 55, 64], True) == [22, 64]
    print('It works!')


check_even_numbers()


def secret_names(real_names: list, secret_names: list):
    return list(map(lambda x: choice(secret_names), real_names))


print(*secret_names(['Iren', 'Alex'], ['Agent Carter', 'Hulk', 'IronMan']))
print(*secret_names(['Iren', 'Alex', 'Ann'], ['Flash', 'Wonder Woman', 'Harley Queen', 'Batman', 'Joker']))
