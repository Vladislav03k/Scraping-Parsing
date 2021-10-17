class Worker:
   def __init__(self, name, surname, position, wage, bonus):
       self.name = name
       self.surname = surname
       self.position = position
       self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)


    def get_ful_name(self):
        return self.name + ' ' + self.surname


    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

worker_1 = Position('Oleg', 'Andreev', 'PR-manager', '100000', '20000')
worker_2 = Position('Nikolay', 'Valiev', 'director', '2000000', '1000')
worker_3 = Position('Vladislav', 'Pavlov', 'Data scientist', '150000', '15000')
print(worker_1.get_ful_name(), worker_1.get_total_income())
print(worker_2.get_ful_name(), worker_2.get_total_income())
print(worker_3.get_ful_name(), worker_3.get_total_income())
