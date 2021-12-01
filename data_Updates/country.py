""" Class Country """


class Country:
    def __init__(self, name, pop, area, continent):
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent

    def getName(self):
        return self._name

    def getPopulation(self):
        return self._pop

    def getArea(self):
        return self._area

    def getContinent(self):
        return self._continent

    def setPopulation(self, newPop):
        self._pop = newPop

    def setArea(self, newArea):
        self._area = newArea

    def setContinent(self, newContinent):
        self._continent = newContinent

    def __repr__(self):
        return self._name + " (pop: " + str(self._pop) + ", size: " + str(self._area) + ") in " + self._continent

# c1 = Country("Canada", 3000000, 60000000, "North_America")
# print(c1)
# c1.setContinent("blue")
# print(c1)
