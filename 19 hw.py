# Домашнее задание
# Напишите декоратор debug, который при каждом вызове
# декорируемой функции выводит её имя (вместе со всеми
# передаваемыми аргументами), а затем — какое значение
# она возвращает. После этого выводится результат её
# выполнения

def debug(fn):
    def wrapper(*args, **kwargs):
        res1 = f'Function name is {fn.__name__},'
        if args and kwargs:
            res2 = f'argument(s) ===> {args} keyword argument(s) ===> {kwargs}'
        elif args:
            res2 = f'argument(s) ===> {args}'
        elif kwargs:
            res2 = f'keyword argument(s) ===> {kwargs}'
        else:
            res2 = f'NO argument(s) and keyword argument(s)'
        res3 = f'Function result ===> {fn(*args, **kwargs)}'
        result = res1 + ' ' + res2 + '\n' + res3
        print(result)
    return wrapper

@debug
def test1(a, b, c, d):
    try:
        result = a + b + c + d
        return result
        # return a, b, c, d
    except:
        return 'Error'

test1(1, 2, 3, 4)
test1(a=2, b=2, c=4, d={1: 'a'})
