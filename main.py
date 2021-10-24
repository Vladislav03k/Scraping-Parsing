from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split("-")

    @classmethod
    def first_method(cls, data):
        try:
            day, month, year = [i for i in data.split("-")]
            return f'{cls.first_method(day), day} \n {cls.first_method(month), month} \n {cls.first_method(year), year}'
        except ValueError:
            return "Неправильная дата"

    @staticmethod
    def sec_method(data):
        try:
            day, month, year = data.split("-")
            date(int(year), int(month), int(day))
            return 'DATA'
        except ValueError:
            return "Неправильная дата"


print(Data.first_method('03-04-2001'))
print(Data.sec_method('03-04-2001'))
