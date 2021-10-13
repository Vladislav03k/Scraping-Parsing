from functools import reduce
my_list = list(range(100, 1001))
new_list = [el for el in my_list if el % 2 == 0]
print(new_list)
def my_func (el1, el2):
    return el1 * el2
print(reduce(my_func, new_list))
