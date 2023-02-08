def multiply(*args):
    a = 1
    for i in args:
        a *= i
    return a
print(multiply(2, 3, 4, 5))


def mirror_string(string='hello'):
    your_string = input('Введите строку: ')
    your_string_from_end = your_string[::-1]
    if your_string == your_string_from_end:
        return True
    return False
print(mirror_string())


def calculator(number1, operator, number2):
    if operator in ('+', '-', '*', '/', '**', '%'):
        if operator == '+':
            print(number1 + number2)
        elif operator == '-':
            print(number1 - number2)
        elif operator == '*':
            print(number1 * number2)
        elif operator == '%':
            print(number1 % number2)
        elif operator == '**':
            print(number1**number2)
        elif operator == '/':
            if number2 != 0:
                print(number1 / number2)
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
calculator(1, '**', 7)