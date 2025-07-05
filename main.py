balance_remain = 0

def options():
    option = {
        "Show Balance" : "1.",
        "Deposit" : "2.",
        "Withdraw" : "3.",
        "Exit" : "4."        
    }
    for value, keys in option.items():
        print(keys, end = " ")
        print(value)
        print()
    print("***************************************")
    
def options_choosen():
    while True:
        option_choosen = input("Enter your choice (1-4): ")
        if option_choosen in ["1", "2", "3", "4"]:
            print("***************************************")
            return option_choosen
        else:
            print("You can only enter a number between 1 and 4")

def show_balance():
    print(balance_remain)

def deposit():
    amount = input(int("How much money would you like to deposit in your bank account: "))
    balance_remain = balance_remain + amount

def withdraw():
    amount = input("What amount would you like to withdraw from your bank account: ")
    return amount

def exit():
    exit

def selection(num_choosen):
    if num_choosen == "1":
        show_balance()
    elif num_choosen == "2":
        deposit()
    elif num_choosen == "3":
        withdraw()
    elif num_choosen == "4":
        exit()
   

def main():
    print("***************************************")
    print("            Banking Program")
    print("***************************************")
    options()
    num_choosen = options_choosen()
    selection(num_choosen)
    

    

if __name__ == "__main__":
    main()