my_str = str(input("Введите предложение: "))
my_str_split = my_str.split(" ")
for i, el in enumerate(my_str_split, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. {el}")