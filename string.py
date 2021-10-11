def has_substring(s, t):
    for i in range(len(s) - len(t) + 1):
        matched = True
        for j in range(0, len(t)):
            if s[i + j] == t[j]:
               matched = False
            if matched:
                return True
    return False

def is_number(s):
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    b = []
    for i in s:
        if i in numbers:
            b += [i]
    if len(s) == len(b):
        return True
    elif len(s) != len(b):
        return False

def is_case_insensitive_equal(s, t):
    if s.lower() == t.lower():
        print(True)
    else:
        print(False)