month = int(input("Введите месяц числом: "))
if month <= 12 and month >= 1:
    my_dict = {1 : "зима", 2 : "зима", 3 : "весна", 4 : "весна", 5 : "весна", 6 : "лето", 7 : "лето", 8 : "лето", 9 : "осень", 10 : "осень", 11 : "осень", 12 : "зима"}
    my_list = list(my_dict.values())
    for i, el in enumerate(my_list):
        if i == month - 1:
            print(my_list[i])
            break
else:
    print("Неверное значение!")

