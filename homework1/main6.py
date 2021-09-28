a = int(input("Введите фактический результат бега в км: "))
b = int(input("Введите желаемый результат бега в км: "))
resultat_days = 1
resultat_km = a
while resultat_km <= b:
    a= a + 0.1 * a
    resultat_days += 1
    resultat_km = resultat_km + a
print(f"Достигнут желаемый результат на {resultat_days} день")