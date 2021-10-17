class Road:


    def __init__(self, length, width, surface_mass, sickness):
        self._length = length
        self._width = width
        self._surface_mass = surface_mass
        self._sickness = sickness
    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self._surface_mass * self._sickness / 1000
        print(f'Для дорожного покрытия необходимо {round(asphalt_mass)} массы асфалта')


r = Road(5000, 20, 25, 5)
r.asphalt_mass()