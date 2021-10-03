viruchka = int(input("Введите вашу выручку: "))
izdershki = int(input("Введите ваши издержки: "))
if viruchka > izdershki:
    print(f"Финансовый резултат: прибыль. Рентабельность фирмы составила {viruchka // izdershki}")
    chislenost = int(input("Введите количество сотрудников: "))
    print(f"Прибыль фирмы в расчете на 1 сотрудника составила: {viruchka // chislenost}")
elif viruchka == izdershki:
    print("Финансовый резултат: фирма работает в ноль")
else:
    print("Финансовый результат: убыток")
