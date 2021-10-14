def summary():
    try:
        with open('new_num_file', 'r+', encoding='utf-8') as file:
            file.write((input("Ведите числа через пробел: ")))
            new_list = map(int, file.read().split())
            print(sum(new_list))
    except IOError:
        print("IOError")
    except ValueError:
        print("ValueError")


summary()
#НЕ ПОНИМАЮ КАК СДЕЛАТЬ ТАК, ЧТОБЫ ПРОГРАММА ЧИТАЛАСЬ МГНОВЕННО,А НЕ СО 2 РАЗА

#with open('new_num_file', 'w', encoding='utf-8') as f_change:
    #f_change.write((input("Ведите числа через пробел: ")))
#with open('new_num_file', 'r', encoding='utf-8') as f_read:
    #new_num = f_read.read()
    #new_list = map(int, f_read.read().split())
    #print(sum(new_list))



