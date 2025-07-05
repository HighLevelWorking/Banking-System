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
    option_choosen = input("Enter your choice (1-4): ")
    print("***************************************")
    return option_choosen

def show_balance():
    print(show_balance)

def deposit():
    amount = input("How much money would you like to deposit in your bank account: ")
    return amount

def withdraw():
    amount = input("What amount would you like to withdraw from your bank account: ")
    return amount

def exit():
    exit

def main():
    print("***************************************")
    print("            Banking Program")
    print("***************************************")
    options()
    num_choosen = options_choosen()
    if num_choosen == "1":
        show_balance()

    

if __name__ == "__main__":
    main()