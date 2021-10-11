def calc(num1, operator, num2):
    num1 = int(num1)
    num2 = int(num2)
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
