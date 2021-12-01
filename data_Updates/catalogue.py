import country

class CountryCatalogue():
    def __init__(self, countryFile):

        self._countryCat = []

        #opening the file
        try:
            c_file = open(countryFile, encoding='utf-8', errors='ignore')
        except IOError:
            # if one of the files does not exist, return an empty list
            return self._countryCat

        next(c_file) # skipping first line
        for lineNum in c_file:
            temp = lineNum.strip("\n").split("|")
            self._countryCat.append(country.Country(temp[0], temp[2], temp[3], temp[1]))

    def getCountryList(self):
        return self._countryCat


    # def setPopulationOfCountry(self):
    #
    # def setAreaOfCountry(self):
    #
    # def setContinentOfCountry(self):
    #
    # def findCountry(self,country):
    #
    # def addCountry(self, countryName, pop, area, cont):
    #
    def printCountryCatalogue(self):
        # Method that prints a list of the countries and their info to the screen
        # use __repr__ from Country class
        for i in range(len(self._countryCat)):
            print(self._countryCat[i])

    # def saveCountryCatalogue(self, name):
    #     # Method that enables all the country info in the catalogue to be saved to a file
    #     # countries should be sorted alphabetically prior to saving

countries = CountryCatalogue("data.txt")
print(countries.printCountryCatalogue())
