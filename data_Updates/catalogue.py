class CountryCatalogue:
    def __init__(self, countryFile):

        self._countryCat = {
            # Dictionary to hold country info from file
            "countries": [],
            "continents": [],
            "populations": [],
            "areas": []
        }

        #opening the file
        try:
            c_file = open(countryFile, encoding='utf-8', errors='ignore')
        except IOError:
            # if one of the files does not exist, return an empty list
            return self._countryCat

        next(c_file) #skipping first line
        for lineNum in c_file:

            temp = lineNum.strip("\n").split("|")

            print(temp)
            self._countryCat["countries"] = temp[0]
            self._countryCat["continents"] = temp[1]
            self._countryCat["populations"] = temp[2]
            self._countryCat["areas"] = temp[3]

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
        for i in range(len(self._countryCat["countries"])):
            print(i)
            print(self._countryCat["countries"][0])
            print("Country: ", self._countryCat["countries"[i]])
            print("Continent: ", self._countryCat["continents"[i]])
            print("Population: ", self._countryCat["populations"[i]])
            print("Area: ", self._countryCat["areas"[i]])
    #
    # def saveCountryCatalogue(self, name):
    #     # Method that enables all the country info in the catalogue to be saved to a file
    #     # countries should be sorted alphabetically prior to saving

countries = CountryCatalogue("data.txt")
print(countries.printCountryCatalogue())
