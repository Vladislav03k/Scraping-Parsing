num_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []
with open('text_4.txt', 'r+', encoding='utf-8') as file:
    with open('new_file_text_4.txt', 'w', encoding='utf-8') as new_file:
        my_list = file.readlines()
        for i in my_list:
            i = i.split(' ', 1)
            new_text.append(num_rus[i[0]] + ' ' + i[1])
        new_file.writelines(new_text)
print(new_text)