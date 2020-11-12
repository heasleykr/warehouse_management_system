"""
Program: Warehouse Control
Author:  Katelynn Heasley
Date:    November 2020
Functionality:
    - Register Products
        - id (auto generated)
        - title
        - category
        - stock
        - price

"""


# imports
# import functions from menu file.
from menu import clear, print_menu, print_header, print_product_info
from product import Product
import pickle

# global
catalog = []
next_id = 1

# functions


def serialize_data():
    # open a write file
    # 'data' is not a common extension, so users can't open and edit your file.
    # Two params for 'open': File name, 'wb' means 'write binary'
    try:
        writer = open('warehouse.data', 'wb')
        pickle.dump(catalog, writer)  # Two params: object to save, stream
        writer.close()  # close stream
        print("** Data serialized!")

    except:
        print("** Error, data not saved. DONT Close the system.")


def deserialize_data():
    # import global variable
    global next_id

    try:
        # open file to read. 'rb' = read binary
        reader = open('warehouse.data', 'rb')
        temp_list = pickle.load(reader)
        reader.close()  # close stream

        # returns the array of the catalog
        for prod in temp_list:
            # add the products from temporary array into real array.
            catalog.append(prod)

        # get the last used id, and increase by 1
        last = catalog[-1]
        next_id = last.id + 1

        # get catalog array length
        how_many = len(catalog)

        print("** Read: " + str(how_many) + " products")

    except:
        print("** Error, no data file found")


def register_product():
    # import your global variable
    global next_id

    try:
        print_header("Register New Product")
        title = input("What is the product title: ")
        category = input("Provide the Category: ")
        stock = int(input("Please provide intial stock amount: "))
        price = float(input("Please provide the price: "))

        # validate data
        if(len(title) < 1):
            print("*Error: Title should not be empty")

        # Python Object
        product = Product(next_id, title, category, stock, price)
        next_id += 1  # increment your id

        # add to catalog array
        catalog.append(product)

    except:
        print("** Error, Invalid Data Type")


def display_catalog():
    # display title
    print_header("Current Catalog")
    for i in catalog:
        print_product_info(i)


def out_Stock():
    print_header("Products Out Of Stock")
    for i in catalog:
        if(i.stock == 0):
            print_product_info(i)


def total_Stock():
    print_header("Total Stock Value")
    total = 0
    for prod in catalog:
        total += (prod.stock * prod.price)

    print("Total Value of Stock: $" + str(total))


def cheapest():
    print_header("Cheapest Product in Stock: ")
    min = catalog[0].price
    product = catalog[0].title
    for d in catalog:
        if(d.price < min):
            min = d.price
            product = d.title

    print("Cheapest item in Stock: " + product)
    print("Price: " + str(min))


def delete_product():
    print_header("Delete Product")
    display_catalog()

    try:
        prodDelete = int(
            input("Enter id of the product you would like to delete: "))

        found = False
        for prod in catalog:
            if(prodDelete == prod.id):
                found = True
                catalog.remove(prod)
                print("** Item Removed! **")

        if(not found):
            print("** Incorrect Id, try again")

    except:
        print("** Invalid data format **")


def update_price():
    print_header("Update Product Price")
    display_catalog()

    try:
        id = int(input("Enter Product Id to update price: "))
        price = float(input("What is the new unit price? "))

        found = False

        for prod in catalog:
            if(id == prod.id):
                found = True
                prod.price = price
                print("** Updated Successfully: ")
                print_product_info(prod)
        if(not found):
            print("** Invalid Product Id **")

    except:
        print("** Error: Invalid Data Type Entry **")


def update_stock():
    print_header("Update Product Stock")
    display_catalog()

    found = False

    try:
        id = int(input("Enter Product Id to update price: "))
        stock = int(input("What is the new stock amount? "))

        for prod in catalog:
            if(id == prod.id):
                found = True
                prod.stock = stock
                print("** Updated Successfully: ")
                print_product_info(prod)
        if(not found):
            print("** Invalid Product Id **")

    except:
        print("** Error: Invalid Data Type Entry **")


# load our data, wait for user to see before pressing enter.
deserialize_data()
input("Press Enter to continue...")

opc = ""
while(opc != 'x'):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_product()
        serialize_data()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        out_Stock()
    elif(opc == '4'):
        total_Stock()
    elif(opc == '5'):
        cheapest()
    elif(opc == '6'):
        delete_product()
        serialize_data()
    elif(opc == '7'):
        update_price()
        serialize_data()
    elif(opc == '8'):
        update_stock()
        serialize_data()
    elif(opc == 's'):
        serialize_data()

    input("Press Enter to continue...")
# loop to present the menu, ask for an option

print("Good byte")
