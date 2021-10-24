class Warehouse:
    def __init__(self, name, model, price, quantity, number, *args):
        self.name = name
        self.model = model
        self.price = price
        self.quantity = quantity
        self.number = number
        self.warehouse_full = []
        self.warehouse = []
        self.items = {
            'Наименование устройства:': self.name,
            'Модель:': self.model,
            'Цена устройства:': self.price,
            'Количесто устройств на складе:': self.quantity
        }

    def __str__(self):
        return f'{self.name} {self.model} \nЦена за единицу: {self.price} \nКоличество техники на складе:{self.quantity} '

    def income(self):
        try:
            name = input('Введите наименование устройства: ')
            model = input('Введите наименование модели устройства: ')
            price = int(input('Введите цену за единицу устройства: '))
            quantity = int(input('Введите количество доступных на складе устройств: '))
            items_income = {
            'Наименование устройства:': name,
            'Модель:': model,
            'Цена устройства:': price,
            'Количесто устройств на складе:': quantity
            }
            self.items.update(items_income)
            self.warehouse.append(self.items)
            print(f'Список товаров: {self.warehouse}')
        except ValueError:
            return f"Введено недопустимое значение! Попробуйте ввести текстовый формат, вместо числового и наоборот."
        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.warehouse_full.append(self.warehouse)
            print(f'Весь склад -\n {self.warehouse_full}')
            return f'Выход'
        else:
            Warehouse.income(self)


class Printer(Warehouse):
    def to_print(self):
        return f'Что-то принтерит {self.number} раз :)'


class Scanner(Warehouse):
    def to_scan(self):
        return f'Что-то сканит {self.number} раз :)'


class Xerox(Warehouse):
    def to_xer(self):
        return f'Что-то ксерит {self.number} раз :)'


p = Printer('Canon', 'PIXMA', 12500, 10, 4)
s = Scanner('Plustek', 'SmartOficce', 21000, 8, 12)
x = Xerox('Xerox', 'WorkCenter 3335DNI', 30200, 4, 6)
print(p.income())
print(s.income())
print(x.income())
print(p.to_print())
print(s.to_scan())
print(x.to_xer())