def my_func():
    try:
        arg_1 = int(input())
        arg_2 = int(input())
    except ZeroDivisionError:
        return
    my_division = arg_1 / arg_2
    return my_division

last_step = my_func()
print((last_step))
