from country import Country


class CountryCatalogue:
    def __init__(self, countryFile):

        self._countryCat = []

        # opening the file
        c_file = open(countryFile, 'r', encoding='utf-8', errors='ignore')

        next(c_file)  # skipping first line

        for line in c_file:
            #if the line is empty (contains no info), skip the line
            if line == "\n":
                continue

            temp = line.strip("\n").split("|")
            new_country = Country(temp[0], temp[2], temp[3], temp[1])
            self._countryCat.append(new_country)

        c_file.close()

    def getCountryList(self):
        # prints the country catalogue out to the screen very simply, without formatting
        return self._countryCat

    def findCountryIndex(self, country_name):
        # if country_name inputted exists in country list, returns country object from catalogue
        # if no country, returns None
        for i in range(len(self._countryCat)):
            if country_name == self._countryCat[i].getName():
                return i

    '''Required Methods'''

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
            self._countryCat[index].setArea(newArea)

    def setContinentOfCountry(self, newCont, country):
        # sets the continent of a specific country
        index = self.findCountryIndex(country)
        if index != None:
            self._countryCat[index].setContinent(newCont)

    def findCountry(self, country):
        # uses findCountryIndex method to find if a country is in the catalogue, and returns the country obj if it is
        found = False
        for i in range(len(self._countryCat)):
            if str(self._countryCat[i]) == str(country):
                found = True
        if found:
            return country
        else:
            return None

    def addCountry(self, countryName, pop, area, cont):
        success = False
        if self.findCountry(countryName) is None:
            new_country = Country(countryName, pop, area, cont)
            self._countryCat.append(new_country)
            success = True
        return success

    def printCountryCatalogue(self):
        # Method that prints a list of the countries and their info to the screen
        # use __repr__ from Country class
        for i in range(len(self._countryCat)):
            # by printing the class, it calls the __repr__ method in the class Country
            print(self._countryCat[i])

    def saveCountryCatalogue(self, fname):
        # Method that enables all the country info in the catalogue to be saved to a file
        # countries should be sorted alphabetically prior to saving

        counter = 0
        try:
            out_file = open(fname, 'w', encoding='utf-8', errors='ignore')
        except IOError:
            print("Error: output file not accepted")

        # first line
        out_file.write("Country|Continent|Population|Area\n")
        # sorting before inputting into file
        self._countryCat = sorted(self._countryCat)
        # writing each line to the file in the proper format, while updating counter
        for count_index in range(len(self._countryCat)):
            new_line = self._countryCat[count_index].getName() + "|" + self._countryCat[count_index].getContinent() + "|" + self._countryCat[count_index].getPopulation() + "|" + self._countryCat[count_index].getArea()
            out_file.write(new_line + "\n")
            counter += 1

        if counter != 0:
            return counter
        else:
            return -1

        out_file.close()


# countries = CountryCatalogue("data.txt")
# countries.printCountryCatalogue()
#
# #
# # # countries.printCountryCatalogue()
# # # print(countries.getCountryList())
# print(countries.findCountryIndex("Brazil"))
# countries.setContinentOfCountry("Africa", "Brazil")
# # countries.printCountryCatalogue()
# # # print(countries.findCountry("China"))
# countries.addCountry("Bulgaria", 4000000, 3000000, "Europe")
# countries.saveCountryCatalogue("output.txt")
# countries.printCountryCatalogue()
