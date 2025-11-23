while True:
        print("""
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Exit
        """)
        choice = input ("Enter your choice ")
        if choice == "1":
            num1 = float(input("Enter your num1"))
            num2 = float(input("Enter your num2"))
            print("addition is: ",num1+num2)
        elif choice == "2":
             num1 = float(input("Enter your num1"))
             num2 = float(input("Enter your num2"))
             print("subtraction is: ",num1 - num2)
        elif choice == "3":
             num1 = float(input("Enter your num1"))
             num2 = float(input("Enter your num2"))
             print("multiplication is: ",num1 * num2)
        else :
             choice == "4"
             print("Exit")
             break
