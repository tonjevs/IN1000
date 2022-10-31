class Sirkel:
    def __init__(self,radius):
        self._radius = radius

    def diameter(self,diameter):
        self._diameter = diameter
        diameter = self._radius*2
        return diameter

    def omkrets(self):
        omkrets = self._diameter*3.14
        return omkrets

    def areal(self):
        areal = (self._radius**2)*3.14
