my_list = [7, 5, 5, 4, 3, 2, 1]
new_el = int(input("Введите число: "))
a = my_list.count(new_el)
for el in my_list:
    if a > 0:
        i = my_list.index(new_el)
        my_list.insert(i + a, new_el)
        break
    else:
        if new_el > el:
            i_1 = my_list.index(new_el)
            my_list.insert(i_1, new_el)
            break
        elif new_el < my_list[len(my_list) - 1]:
            my_list.append(new_el)
print(my_list)