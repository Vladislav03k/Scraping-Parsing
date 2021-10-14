with open('text_2.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines()
    for i in range(len(my_list)):
        new_list = my_list[i].split()
print(f'Количество строк в файле: {len(my_list)}. В {i + 1}-ой строке {len(new_list)} слов')
