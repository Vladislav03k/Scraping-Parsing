class MyOwnExeption(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_a = input("Введите положительный числитель: ")
inp_b = input("Введите положительный знаменатель: ")

try:
    a = int(inp_a)
    if a < 0:
        raise MyOwnExeption ('Вы ввели отрицательное число!')
    b = int(inp_b)
    if b < 0:
        raise MyOwnExeption ('Вы ввели отрицательное число!')
    devision = a / b
except ZeroDivisionError:
    print("На ноль делить нельзя")
except ValueError:
    print("ValueError")
except MyOwnExeption as err:
    print(err)
else:
    print(f'{devision}. Ошибок не обнаружено')
finally:
    print("Попробуйте еще раз!")

