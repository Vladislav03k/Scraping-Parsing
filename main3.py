class NumbersException(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    my_list = []
    count = 0
    while count != 10:
        count += 1
        el_inp = int(input('Введите элемент списка: '))
        if el_inp is int:
            my_list.append(el_inp)
        elif el_inp is not int:
            raise NumbersException ('Вы ввели не число!')
except NumbersException as err:
    print(err)
except ValueError:
    print('ValueError')
finally:
    print('Попробуйте еще раз с учетом ошибок!')
