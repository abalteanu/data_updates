import catalogue
from catalogue import CountryCatalogue
import country

# global variables - constants because they are given
africa = "Africa"
antarctica = "Antarctica"
arctic = "Arctic"
asia = "Asia"
europe = "Europe"
nAmerica = "North_America"
sAmerica = "South_America"
continents = ["Africa", "Antarctica", "Arctic", "Asia", "Europe", "North_America", "South_America"]


def processUpdates(cntryFileName, updateFileName, badUpdateFile):
    '''Reads Updates and updates catalogue of countries'''

    '''Processing Files'''
    # opening data file error check
    while True:
        try:
            catalog = CountryCatalogue(cntryFileName)
            break
        except FileNotFoundError:

            exit = input("Country file not found. \nWould you like to quit? Y (yes) or N (no): ")
            if exit == "N":
                cntryFileName = input("Please enter a new country file name: ")
            else:
                outputF = open("output.txt", "w")
                outputF.write("Update Unsuccessful\n")
                outputF.close()
                return False, None

    # processing the file of updates
    while True:
        try:
            u_file = open(updateFileName, "r")
            break
        except FileNotFoundError:
            exit = input("Updates file not found. Would you like to quit? Y (yes) or N (no): ")
            if exit == "N":
                updateFileName = input("Please enter a new country file name: ")
            else:
                outputF = open("output.txt", "w")
                outputF.write("Update Unsuccessful\n")
                outputF.close()
                return False, None


    '''Processing Updates'''
    bu_file = open(badUpdateFile, "w")

    # discarding invalid updates
    for line in u_file:

        # if there is a blank line in the file, skip
        if line == None:
            break


        updatesForCountry = line.strip("\n").split(";")

        # taking the name of the country
        countryName = updatesForCountry.pop(0)
        print(countryName)
        #checking that country name is a sting
        '''im not sure how this should work, because split automatically makes it into a string'''
        if type(countryName) != str:
            bu_file.write(line + "\n")
            break

        # checking that the number of updates is between 0 and 3 (no more no less)
        countUpdates = 0
        for update in updatesForCountry:
            update.strip()
            print(update)
            countUpdates += 1

        if 0 < countUpdates > 3:
            bu_file.write(line + "\n")
            break

        p_counter = 0
        a_counter = 0
        c_counter = 0

        # checking each individual update for a country
        for update in updatesForCountry:
            # update_ list is a list of the two parts of a single update "L=value"
            update_list = update.split("=")
            if update_list[0] == "P":
                p_counter +=1

                # splitting the population information by commas, to check if the length split by each comma is 3
                popCount = update_list[1].split(",")

                # if the start of the number has more than 3 digits with no commas splitting it, its invalid
                if len(popCount[0]) < 3:
                    bu_file.write(line + "\n")
                    break
                #checking that the other groups of three are equal to three
                for i in range(1, len(popCount)):
                    if len(popCount[i]) != 3:
                        bu_file.write(line + "\n")
                        break

            elif update_list[0] == "A":
                a_counter +=1
            elif update_list[0] == "C":
                c_counter +=1
                contFound = False
                for i in continents:
                    if update_list[1] == continent[i]:
                        contFound = True

                if  contFound == False:
                    bu_file.write(line + "\n")
                    break

            print(update_list)

        if p_counter > 1 or c_counter > 1 or a_counter > 1:
            bu_file.write(line + "\n")
            break


        # performing updates


        # finding the index of the country in the catalog so that we can make changes to it.
        countryIndex = catalog.findCountryIndex(countryName)
    bu_file.close()
    catalog.printCountryCatalogue()


def checkUpdate(record, countryCatalogue):
    '''Function that checks whether update record is valid'''

    #if type == "P":
