my_list1 = input("Введите список элементов без запятых и пробелов: ")
my_list1 = list(my_list1)
print(my_list1)
if len(my_list1) % 2 == 0:
    i = 0
    while i < len(my_list1):
        el = my_list1[i]
        my_list1[i] = my_list1[i + 1]
        my_list1[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(my_list1) - 1:
        el = my_list1[i]
        my_list1[i] = my_list1[i + 1]
        my_list1[i + 1] = el
        i += 2
print(my_list1)






