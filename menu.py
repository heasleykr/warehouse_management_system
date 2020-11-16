# import
import os
import datetime

# Functions


def print_menu():
    print('-' * 53)
    print(' Welcome To The Product Warehouse [' + get_date_time() + "]")
    print('-' * 53)

    print('[1] Add Product to Catalog')
    print('[2] Display Catalog')
    print('[3] Display Products Out of Stock')
    print('[4] Total Stock Value')
    print('[5] Cheapest Product')
    print('[6] Delete Product')
    print('[7] Update Product Price')
    print('[8] Update Product Stock')
    print('[9] Most Expensive Items')
    print('[10] Distinct Categories')

    print('[s] Save Changes')
    print('[x] Exit')
    print('-' * 20)


def get_date_time():
    now = datetime.datetime.now()
    # Look at reference for display codes.
    return now.strftime("%b/%d/%Y %H:%M")


def print_header(text):
    clear()
    print('-' * 76)
    print(text)
    print('-' * 76)


def print_product_info(prod):
    print(
        "| " + str(prod.id).rjust(3) + " | " +
        prod.title.ljust(25) + " | " +
        prod.category.ljust(12) + " | " +
        str(prod.stock).rjust(7) + " | $" +
        str(prod.price).rjust(12) + " |"
    )


def clear():
    if(os.name == "nt"):
        return os.system('cls')
    else:
        return os.system('clear')
