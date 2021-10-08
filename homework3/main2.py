def my_func(var_1, var_2, var_3):
    print(f'Сумма двух наибольших аргументов: {var_1 + var_2 + var_3 - min([var_1, var_2, var_3])}')
my_func(
    int(input("argument1 = ")),
    int(input("argument2 = ")),
    int(input("argument3 = "))
)