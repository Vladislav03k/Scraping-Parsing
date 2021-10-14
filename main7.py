my_dict = {}
with open('text_7.txt', 'r', encoding='utf-8') as firm_file:
    for el_dict in firm_file:
        firm, type_firm, revenue, expenses = el_dict.split(' ')
        firm_income = int(revenue) - int(expenses)
        firm_average = sum(map(int,(firm_income[0:])))
        print(firm_average)
        my_dict[firm + type_firm] = firm_income
    print(f'{my_dict}')
#ДАЛЬШЕ НЕ СОВСЕМ ПОНИМАЮ КАК СДЕЛАТЬ