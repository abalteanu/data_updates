import catalogue
from catalogue import CountryCatalogue
import country

# global variables - constants because they are given

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
        if line == "":
            break

        updatesForCountry = line.strip("\n").split(";")

        # taking the name of the country
        countryName = updatesForCountry.pop(0)
        print(countryName)
        if countryName.isalpha():
            print(countryName)
        # checking if country name is valid
        for i in range(len(countryName)):
            print(countryName[i])
            # checking if the first letter is lowercase
            if i == 0 and countryName[i].islower():
                bu_file.write(line + "\n")
                break
            # checking if any char is something other than a letter or an underscore
            if not countryName[i].isalpha():
                if countryName[i] != "_":
                    bu_file.write(line + "\n")
                    print(countryName[i])
                    print("Printing to bad updates")
                    break

            # checking if the char after an underscore is uppercase
            if countryName[i] == "_":
                if countryName[i + 1].islower():
                    bu_file.write(line + "\n")
                    print("Printing to bad updates")
                    break

        # checking that the number of updates is between 0 and 3 (no more no less)
        countUpdates = 0
        for update in updatesForCountry:
            update.strip()
            print(update)
            countUpdates += 1

        # checking if there are more than three updates called
        if 0 > countUpdates > 3:
            bu_file.write(line + "\n")
            print("Printing to bad updates")
            break

        p_counter = 0
        a_counter = 0
        c_counter = 0

        # checking each individual update for a country
        for update in updatesForCountry:
            # update_ list is a list of the two parts of a single update "L=value"
            update_list = update.split("=")
            if update_list[0] == "P":
                # counter to check how many updates of the P type there are
                p_counter += 1
                # if checkNumFormat returns false, it means there was a formatting error in the update and the update
                # is not valid
                if checkNumFormat(update_list) == False:
                    bu_file.write(line + "\n")
                    print("Printing to bad updates")
                    break

            elif update_list[0] == "A":
                # update validity check for area
                a_counter += 1
                if checkNumFormat(update_list) == False:
                    bu_file.write(line + "\n")
                    print("Printing to bad updates")
                    break

            elif update_list[0] == "C":
                c_counter += 1

                # checking in global list of continents to see if the continent entered is valid
                contFound = False
                for i in continents:
                    if update_list[1] == i:
                        contFound = True

                if contFound == False:
                    bu_file.write(line + "\n")
                    print("Printing to bad updates")
                    break

            print(update_list)

        # checking if any of the update types have more than one instance
        if p_counter > 1 or c_counter > 1 or a_counter > 1:
            bu_file.write(line + "\n")
            print("Printing to bad updates")
            break

        # performing updates

        # finding the index of the country in the catalog so that we can make changes to it.
        countryIndex = catalog.findCountryIndex(countryName)
    bu_file.close()
    catalog.printCountryCatalogue()


def checkNumFormat(someList):
    '''Function that checks the number format for the area and population updates'''
    valid = True
    # reversing the number so that it starts with group of three
    reversed = someList[1][::-1]
    print(reversed)

    # checking that number is formatted properly
    if len(someList[1]) > 3:
        counter = 0
        # print(len(update_list[1]))
        for i in range(len(someList[1])):

            # checking if there is a decimal point in the number
            if reversed[i] == '.':
                valid = False
                return valid

            # checking that there is a comma every fourth index
            counter += 1
            print(counter, reversed[i])
            if counter % 4 == 0:
                if reversed[i] != ",":
                    valid = False
                    return valid
            else:
                # checking that there are no repeating commas
                if reversed[i] == ',':
                    valid = False
                    return valid
