userNameInput = input("Enter your username: ")
userPasswordInput = input("Enter your password: ")
if userNameInput == "elle-developer" and userPasswordInput == "147258":
    print("Welcome to Elle Developer")
    print("---------Market----------")
    print("Product list")
    print("1.IPHONE 18 PROMAX       50,000 THB")
    print("2.NoteBook Acer          30,000 THB")
    print("3.Super Car              80,000 THB")
    userSelection = int(input("Enter your choice: "))
    quantity = int(input("Enter quantity: "))
    if userSelection == 1:
        productTotal = 50000 * quantity
        print(productTotal, "THB")
    elif userSelection == 2:
        productTotal = 30000 * quantity
        print(productTotal, "THB")
    elif userSelection == 3:
        productTotal = 80000 * quantity
        print(productTotal, "THB")
    else:
        print("Please enter a valid input")
else:
    print("Failed Login")

