with open('text_3.txt', 'r', encoding='utf-8') as f:
    salary = []
    poor = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20000: {poor}, средний оклад: {sum(map(float,salary)) / len(salary)}')