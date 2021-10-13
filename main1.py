my_list = [39, 56, 87, 13, 91,28, 7, 16, 52, 2, 5, 5, 39, 87, 45, 67, 89, 23, 54, 53, 13, 12, 14, 56]
new_list = [el1 for el2, el1 in enumerate(my_list) if el2 != 0 and el1 > my_list[el2 - 1]]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")