# Домашнее задание
# Есть массив состоящий из слов и чисел, нужно записать в
# файл сначала слова в порядке их длины, а после слов
# цифры в порядке возрастания

num = []
wrd = []
mas = [1, 2, 3, 12, -7, 'a', 'class', 'day', '66']
for i in mas:
    if type(i) == int:
        num.append(str(i))
    elif i.isalpha():
        wrd.append(i)
    elif i.isdigit():
        num.append(i)
wrd.sort(key=len)
num.sort()
# print(num, wrd)
with open('homework', 'w', encoding='UTF-8') as f:
    for el in wrd:
        f.write(el)
        f.write(' ')
    for el in num:
        f.write(el)
        f.write(' ')

