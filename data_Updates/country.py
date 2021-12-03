""" Class Country """


class Country:
    def __init__(self, name, pop, area, continent):
        self._name = str(name)
        self._pop = str(pop)
        self._area = str(area)
        self._continent = str(continent)

    def getName(self):
        return self._name

    def getPopulation(self):
        return self._pop

    def getArea(self):
        return self._area

    def getContinent(self):
        return self._continent

    def setPopulation(self, newPop):
        self._pop = str(newPop)

    def setArea(self, newArea):
        self._area = str(newArea)

    def setContinent(self, newContinent):
        self._continent = newContinent

    def __repr__(self):
        return self._name + " (pop: " + self._pop + ", size: " + self._area + ") in " + self._continent


# c1 = Country("Canada", 3000000, 60000000, "North_America")
# print(c1)
# c1.setPopulation("33")
# print(c1)
