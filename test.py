# Если помните, на старых мобильных телефонах текстовые сообщения набирались при
# помощи цифровых кнопок.
# При этом одна кнопка была ассоциирована сразу с несколькими буквами, а выбор зависел
# от количества нажатий на кнопку.
# Однократное нажатие приводило к появлению первой буквы в соответствующем этой
# кнопке списке, последующие нажатия меняли ее на следующую.
# Напишите программу, отображающую последовательность кнопок, которую необходимо
# нажать, чтобы на экране телефона появился текст,
# введенный пользователем.
# Создайте словарь, сопоставляющий символы с кнопками, которые необходимо нажать, а
# затем воспользуйтесь им для вывода на экран последовательности кнопок в соответствии с
# введенным пользователем сообщением по запросу.#
# Удостоверьтесь, что ваша программа корректно обрабатывает строчные и прописные
# буквы. При преобразовании букв в цифры игнорируйте символы, не входящие в указанный
# перечень, такие как точка с запятой или скобки

# 10
def prog10(str1):
    dict1 = {'1': '.,?!:', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs','8': 'tuv',\
             '9': 'wxyz', '0': ' '}
    for i in str1:
        for k in dict1:
            if i in dict1[k]:
                for x in dict1[k]:
                    if x == i:
                        print(k, end='')
                        break
                    else:
                        print(k, end='')

prog10(str1=(input("Введите фразу: ")).lower())




#11
def prog11(data):
    # data = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
    data2 = []
    for i in data:
        if isinstance(i, list):
            data2.extend(prog11(i))
        else:
            data2.append(i)
    return data2


print(prog11([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))


#3
from datetime import datetime, timedelta

def prog3(d):
    dt = datetime.strptime(d, '%Y-%m-%d')
    print(dt)
    res = dt + timedelta(days=1)
    return res.strftime('%Y-%m-%d')
print(prog3('1978-12-31'))
