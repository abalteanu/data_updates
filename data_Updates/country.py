""" Class Country """


class Country:
    # Initializing class instance
    def __init__(self, name, pop, area, continent):
        self._name = str(name)
        self._pop = str(pop)
        self._area = str(area)
        self._continent = str(continent)

    # Getters
    def getName(self):
        return self._name

    def getPopulation(self):
        return self._pop

    def getArea(self):
        return self._area

    def getContinent(self):
        return self._continent

    # Setters
    def setPopulation(self, newPop):
        self._pop = str(newPop)

    def setArea(self, newArea):
        self._area = str(newArea)

    def setContinent(self, newContinent):
        self._continent = newContinent

    def __lt__(self, other):
        # for sorting the list
        return self._name < other._name

    def __repr__(self):
        return self._name + " (pop: " + self._pop + ", size: " + self._area + ") in " + self._continent



