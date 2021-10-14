my_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f_dict:
    for el_dict in f_dict:
        subject, hours = el_dict.split(":")
        subject_sum = sum(map(int, ''.join([i for i in hours if i == " " or ('0' <= i <= '9')]).split()))
        my_dict[subject] = subject_sum
    print(f'{my_dict}')