# Задача №1
# Ввод с клавиатуры. Если строка введённая с клавиатуры –
# это числа, то поделить первое на второе. Обработать
# ошибку деления на ноль. Если второе число 0, то
# программа запрашивает ввод чисел заново. Также если
# были введены буквы, то обработать исключение
while True:
    try:
        n1 = input('Enter number 1:  ')
        n2 = input('Enter number 2:  ')
        if n1.isdigit() and n2.isdigit():
            print(f'{n1} / {n2} =', int(n1)/int(n2))
        if int(n2) != 0:
            break
    except ZeroDivisionError:
        print('Division by zero')
    except ValueError:
        print('Check input')
        break


