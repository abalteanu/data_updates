import country

class CountryCatalogue:
    def __init__(self, countryFile):

        self._countryCat = []

        #opening the file
        try:
            c_file = open(countryFile, encoding='utf-8', errors='ignore')
        except IOError:
            # if one of the files does not exist, return an empty list
            print("Error: file not accepted")

        next(c_file) # skipping first line
        for lineNum in c_file:
            temp = lineNum.strip("\n").split("|")
            self._countryCat.append(country.Country(temp[0], temp[2], temp[3], temp[1]))

    def getCountryList(self):
        # prints the country catalogue out to the screen very simply, without formatting
        return self._countryCat

    def findCountryIndex(self, country):
        # finds the index of a country (string) in countryCat
        # if no country, returns None
        for i in range(len(self._countryCat)):
            if country == self._countryCat[i].getName():
                return i
            else:
                return None

    def setPopulationOfCountry(self, newPopulation, country):
        # takes the new population to be changed and the country for which to change it and uses the findCountryIndex
        # to find the index of the country in coutnryCat list, then uses the setPopulation method in Country class to
        # assign the new population to the country
        index = self.findCountryIndex(country)
        if index != None:
            self._countryCat[index].setPopulation(newPopulation)

    def setAreaOfCountry(self, newArea, country):
        # sets the Area of a specific country
        index = self.findCountryIndex(country)
        if index != None:
            self._countryCat[country].setArea(newArea)

    def setContinentOfCountry(self, newCont, country):
        # sets the continent of a specific country
        index = self.findCountryIndex(country)
        if index != None:
            self._countryCat[country].setContinent(newCont)
    #
    # def findCountry(self,country):
    #
    # def addCountry(self, countryName, pop, area, cont):
    #
    def printCountryCatalogue(self):
        # Method that prints a list of the countries and their info to the screen
        # use __repr__ from Country class
        for i in range(len(self._countryCat)):
            # by printing the class, it calls the __repr__ method in the class Country
            print(self._countryCat[i])

    # def saveCountryCatalogue(self, name):
    #     # Method that enables all the country info in the catalogue to be saved to a file
    #     # countries should be sorted alphabetically prior to saving

countries = CountryCatalogue("data.txt")
countries.printCountryCatalogue()
print(countries.getCountryList())
#print(countries.findCountryIndex("Brazil"))
countries.setPopulationOfCountry(33, "Bazil")
countries.printCountryCatalogue()
