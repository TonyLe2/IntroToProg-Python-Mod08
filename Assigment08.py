# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Tony Le, 11.26.2019, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = "products.txt"  # The name of the data file
lstOfProductObjects = [] # A dictionary that acts as a 'table' of rows

# Declare variables and constants
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Product, Price}
strChoice = ""  # Capture the user option selection
strProduct = ""
strPrice = ""

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Tony Le, 11.26.2019, Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class

    # -- Constructor --
    def __init__(self, product_name, product_price):
        #-- Attributes --
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --
    # product_name

    @property  # DON'T USE NAME for this directive
    def product_name(self):  # (getting or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # last_name
    @property  # DON'T USE NAME for this directive
    def product_price(self):  # (getting or accessor)
        return str(self.__product_price).title()  # Title case

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, value):  # (setter or mutator)
        self.__product_price = value

    def __str__(self):
        return self.product_name + ',' + self.product_price

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Tony Le, 11.26.2019, Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Product": data[0].strip(), "Price": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """
        Desc - Writes data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: nothing
        """
        pass # TODO: Add code Here

        objFile = open(file_name, "w")
        for dicRow in list_of_rows:  # Write each row of data to the file
            objFile.write(dicRow["Product"] + "," + dicRow["Price"] + "\n")
        objFile.close()

    @staticmethod
    def AddRowToList(product, price, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows

        :param product: (string) with name of product:
        :param price: (string) with name of price level:
        :param list_of_rows: (list) you want filled with file data:
        :return: nothing
        """
        dicRow = {"Product": product, "Price": price}  # Create a new dictionary row
        list_of_rows.append(dicRow)  # Add the new row to the list/table

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """ A class for performing Input and Output """
    pass
    # TODO: Add code to show menu to user
    @staticmethod
    def PrintMenuItems():
        """  Print a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new product.
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """ Shows the current items in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products and their corresponding prices are: *******")
        for row in list_of_rows:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("************************************************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def userProductInput():
        """ Registers user input for a product and price
        :return: nothing
        """
        global strProduct
        global strPrice
        global objP1
        strProduct = str(input("What is the product? - ")).strip()  # Get product from user
        strPrice = str(input("What is the price? - ")).strip()  # Get price from user
        objP1 = Product(strProduct, strPrice)
        print()  # Add an extra line for looks

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
# TODO: Add Data Code to the Main body

# Step 1 - When the program starts, Load data from products.txt.
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    IO.PrintMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Step 3 - Process user's menu choice
    # Step 3.1 Show current data
    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.2 - Add a new item to the list/Table
    elif strChoice.strip() == '2':

        # Step 3.2.a - Ask user for new product and price
        IO.userProductInput()
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table

        # Step 3.2.b  Add item to the List/Table
        FileProcessor.AddRowToList(objP1.product_name, objP1.product_price, lstOfProductObjects)
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.4 - Save products to the products.txt file
    elif strChoice == '3':

        #Step 3.4.a - Show the current items in the table
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table

        #Step 3.4.b - Ask if user if they want save that data
        if "y" == str(input("Save this data to file? (y/n) - ")).strip().lower():  # Double-check with user

            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)

            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    # Step 3.6 - Exit the program
    elif strChoice == '4':
        break   # and Exit

# Main Body of Script  ---------------------------------------------------- #