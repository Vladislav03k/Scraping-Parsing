def calculate_sum(*args):
    sum = 0
    checkpoint = False
    for arg in args:
        try:
            if arg:
                sum += float(arg)
        except ValueError:
            checkpoint = True
    return sum, checkpoint
general_sum = 0
while True:
    args_string = input("Введите числа через пробел: ").split(' ')
    sum, stop_checkpoint = calculate_sum(*args_string)
    general_sum += sum
    print(f'сумма {general_sum}')
    if stop_checkpoint:
        break