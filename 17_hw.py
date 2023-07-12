# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим: если произведение гласных и согласных букв
# меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class Hw:

    def __init__(self):
        self.a = input('Enter a:')

    def met1(self):
        sum = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        num_vow = 0
        num_cons = 0
        self_vow = []
        self_cons = []
        if self.a.isdigit():
            for i in range(len(self.a)):
                if int(self.a[i]) % 2 == 0:
                    sum += int(self.a[i])
            return (f'Произведение суммы чётных цифр на длину числа = {sum * (len(self.a))}')
        elif self.a.isalpha():
            for i in range(len(self.a)):
                if self.a[i] in vowels:
                    num_vow += 1
                    self_vow.append(self.a[i])
                else:
                    num_cons += 1
                    self_cons.append(self.a[i])
        if num_vow * num_cons <= len(self.a):
            return (f' все гласные: {self_vow}')
        else:
            return (f' все согласные: {self_cons}')



    def met2(self):
        str1 = self.a.strip(' ')
        len_str = []
        len_num = []
        if str1.isdigit():
            return (f'Dlinna chisla =  {len(str1)}')
        elif str1.isalpha():
            return (f'Dlinna stroki =  {len(str1)}')
        elif self.a.strip:
            for i in range(len(str1)):
                if str1[i].isdigit():
                    len_num.append(i)
                elif str1[i].isalpha():
                    len_str.append(i)
            return (f'Длина числа =  {len(len_num)}, Длина строки = {len(len_str)} ')

test1 = Hw()
print(test1.met2())

