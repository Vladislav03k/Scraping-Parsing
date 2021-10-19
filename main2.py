from abc import ABC, abstractmethod

class Close(ABC):
    def __init__(self, param):
        self._param = param

    @property
    def my_method_1(self):
        pass

    @abstractmethod
    def my_method_2(self):
        pass


class Coat(Close):
    def my_method_1(self):
        return f"Ткань для пальтно: {self._param / 6.5 + 0.5 :.2f}"

    def my_method_2(self):
        pass


class Suit(Close):
    def my_method_1(self):
        return f'Ткань для костюма: {2 * self._param + 0.3:.2f}'

    def my_method_2(self):
        pass

# class Sum(Close):
#     def my_method_1(self):
#         return f"Ткань для пальтно: {self._param / 6.5 + 0.5 :.2f}"
#
#
#     def my_method_2(self):
#         return f'Ткань для костюма: {2 * self._param + 0.3:.2f}'

    # def __add__(self, other):
        #     self._param = self._param + other._param
        # return Sum


coat = Coat(300)
suit = Suit(160)
#my_sum = Sum()
print(Coat.my_method_1())
print(Suit.my_method_1())
#print(Coat.my_method_1().__add__(Suit.my_method_1())

#Вроде все как в практике сделал и методичке, а все равно что-то не получается


