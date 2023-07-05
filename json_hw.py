# Задача №1
# Пользователь будет вводить название и стоимость каждой
# своей покупки за день, до тех пор пока он не напишет
# “стоп”. Ваша задача записать это в json файл в формате:
# {"название" : "яблоко",
#  "стоимость": "200"}

# Задача №2
# Прочитать файл из предыдущего задания и вывести
# стоимость всех покупок за день

import json

with open('json_homework', 'w', encoding='utf-8') as f:
    all_b = [] #будет список всего, что купили
    while True:
        name = input('vvedite nazvanie pokypki:')
        if name == 'stop':
            break
        price = input('vvedite ceny pokypki:')
        all_b.append(dict(nazvanie=name, cena=price))
    json.dump(all_b, f)
with open('json_homework', 'r', encoding='utf-8') as f:
    data = json.load(f)
    all_cost = 0 #будет общая стоимость покупок за день
    for dicts in data:
        all_cost += int(dicts['cena'])
        print(f"stoimostb {dicts['nazvanie']}:{dicts['cena']}")
    print(f"stoimostb vseh pokypok za denb :{all_cost}")
    if not data:
        print(f'Vi nichego ne kypili ;(')




