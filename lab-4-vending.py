balance = 200
running = True

print("Welcome to the awesome vending machine")

while running:
    print(f"Your balance is {balance}p.")
    print("1. Crisps - 100p")
    print("2. Chocolate - 150p")
    print("3. Water - 120p")
    print("4. Quit")

    try:
        choice = int(input("Please select an option: "))
    except ValueError:
        print("Number not used, please use a number to proceed.")
        continue

    if choice == 1:
        price = 100
        name = "Crisps"
    elif choice == 2:
        price = 150
        name = "Chocolate"
    elif choice == 3:
        price = 120
        name = "Water"
    elif choice == 4:
        print("Thank you for using the vending machine.")
        running = False
    else:
        print("Invalid selection. Please try again.")

    if choice in (1, 2, 3):
        print(f"You selected {name}. Price {price}p.")
        if balance >= price:
            balance -= price
            print("Purchase Successful!")
            print(f"Remaining balance: {balance}p.")
        else:
            print("Insufficient funds. Please choose a cheaper product.")