# Case 1 - Conditional Branching Statement
def Buying_Something():

    # Sequential
    print("One day, a mother asked her son to buy food.\n"
          "Then, his finally went to the shop.")

    # Main Program
    print("The child asked, does it have milk (yes/no)?")
    command_A = input()

    conclusion = "Conclusion is His son come home and \nthe result is "

    if command_A == "yes":
        print("His son asked again, do you have eggs (yes/no)?")
        command_B = input()
        if command_B == "yes":
            print(conclusion + "His son bought 6 eggs and 1 bottle of milk in the end")
        else:
            print(conclusion + "His son only bought 1 bottle of milk")
    else:
        print(conclusion + "not buying anything")

# Case 2 - Looping using For
def Stock_Opname_A():
    # Database
    stock_list = {
        "Egg": 10,
        "Rice": 3,
        "Milk": 7,
        "Flour": 2,
        "Salt": 6,
        "Sugar": 1
    }


    # Minimum stock threshold
    min_stock = 5

    # Looping program using for
    for item, stock in stock_list.items():
        print(f"Item: {item}")
        print(f"Current stock: {stock}")

        if stock < min_stock:
            print("Status : Need reorder")
        else:
            print("Status : Stock Available")

        print("-"*30)

# Case 3 - Looping using While
def Stock_Opname_B():
    # Database
    stock_list = {
        "Egg": 10,
        "Rice": 3,
        "Milk": 7,
        "Flour": 2,
        "Salt": 6,
        "Sugar": 1
    }

    # Minimum stock threshold
    min_stock = 5

    # Convert database become list data
    items    = list(stock_list.items())
    index   = 0

    # Looping program using while
    while index < len(items):
        item, stock = items[index]

        print(f"Item: {item}")
        print(f"Current Stock: {stock}")

        if stock < min_stock:
            print("Status : Need reorder")
        else:
            print("Status : Stock Available")

        print("-"*30)

        index +=1 # Increment Index to continue the next item

def main_menu():
    while True:
        print("*" * 30)
        print("Main Menu")
        print("1. Case 1. Conditional Branching Statement")
        print("2. Case 2. Looping using For")
        print("3. Case 3. Looping using While")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        print("*" * 30)

        if choice == "1":
            Buying_Something()
        elif choice == "2":
            Stock_Opname_A()
        elif choice =="3":
            Stock_Opname_B()
        else:
            break

# Running Program
main_menu()

