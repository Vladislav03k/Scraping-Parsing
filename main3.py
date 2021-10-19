class Cell:
    def __init__(self, el_cell):
        self.el_cell = int(el_cell)

    def __add__(self, other):
        self.el_cell = self.el_cell + other.el_cell
        return self.el_cell
        #return Cell(self.el_cell + other.el_cell)

    def __sub__(self, other):
        self.el_cell = self.el_cell - other.el_cell
        return self.el_cell
        #return Cell(self.el_cell - other.el_cell)

    def __mul__(self, other):
        self.el_cell = self.el_cell * other.el_cell
        return self.el_cell
        #return Cell(self.el_cell * other.el_cell)

    def __truediv__(self, other):
        self.el_cell = self.el_cell // other.el_cell
        return self.el_cell
        #return Cell(self.el_cell / other.el_cell)

    def make_order(self, row):
        result = ''
        for i in range(int(self.el_cell / row)):
            result += '*' * row + '\n'
        result += '*' * (self.el_cell % row) + '\n'
        return result


cell = Cell(12)
cell_2 = Cell(9)
print(cell.__add__(cell_2))
print(cell.__sub__(cell_2))
print(cell.__mul__(cell_2))
print(cell.__truediv__(cell_2))
print(cell.make_order(6))
