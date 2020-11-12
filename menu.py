# import
import os

# Functions


def print_menu():
    print('-' * 50)
    print(' Welcome To The Product Warehouse ')
    print('-' * 50)

    print('[1] Add Product to Catalog')
    print('[2] Display Catalog')
    print('[3] Display Products Out of Stock')
    print('[4] Total Stock Value')
    print('[5] Cheapest Product')
    print('[6] Delete Product')
    print('[7] Update Product Price')
    print('[8] Update Product Stock')

    print('[s] Save Changes')
    print('[x] Exit')
    print('-' * 20)


def print_header(text):
    clear()
    print('-' * 50)
    print(text)
    print('-' * 50)


def print_product_info(prod):
    print(
        prod.title + "  " +
        "ID: " + str(prod.id) + "  " +
        "Stock Amount: " + str(prod.stock) + "  " +
        "Price: $" + str(prod.price)
    )


def clear():
    if(os.name == "nt"):
        return os.system('cls')
    else:
        return os.system('clear')

    # How to write code in one line
    # return os.system('cls' if os.name == 'nt' else 'clear')
