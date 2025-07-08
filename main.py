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
    global balance_remain
    amount = int(input("How much money would you like to deposit in your bank account: "))
    balance_remain = balance_remain + amount

def withdraw():
    global balance_remain
    amount = int(input("What amount would you like to withdraw from your bank account: "))
    balance_remain -= amount

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
        return False
    return True
        
   

def main():
    while True:
        print("***************************************")
        print("            Banking Program")
        print("***************************************")
        options()
        num_choosen = options_choosen()
        if not selection(num_choosen):
            break
    

    

if __name__ == "__main__":
    main()