print("="*20)
customerNames=['James','mathew','abby','ben','micheal']
customerPins=['0123','5369','7535','5296','5375']
customerBalances=[10000,50000,36000,45000,70000]
deposition=0
withdrawal=0
balance=0
counter_1=1
counter_2=5
i=0
while True:
    print("======================================================================")
    print("----------------------Welcome to Times Bank---------------------------")
    print("**********************************************************************")
    print("=<<1.Open a new account             >>=")
    print("=<<2.Withdraw money                 >>=")
    print("=<<3.Deposit Money                  >>=")
    print("=<<4.check customers and balance    >>=")
    print("=<<5.Exit/Quit                      >>=")
    print("**********************************************************************")
    choiceNumber=input("select your choice number from above:")
    if choiceNumber=="1":
        print("choice number 1 is selected by customer")
        NOC=eval(input("Number of customers:"))
        i=i+NOC
        if i>5:
            print("\n")
            print("customer registration exceed reached or customer registration is to low")
            i=i-NOC
        else:
            while counter_1<=i:
                name=input("Input FullName:")
                customerNames.append(name)
                pin=str(input("please enter pin of your choice:"))
                customerPins.append(pin)
                balance=0
                deposition=eval(input("please enter the value to deposit:"))
                balance=balance+deposition
                customerBalances.append(balance)
                print("\nName=",end="")
                print(customerNames[counter_2])
                print("pin=",end="")
                print(customerPins[counter_2])
                print("balance=",end="")
                print(customerBalances[counter_2])
                print("-/Rs")
                counter_1=counter_1+1
                counter_2=counter_2+1
                print("\nYour name is added to customers list")
                print("Your pin is added to customer list")
                print("Your balance is added to customer list")
                print("----New account created successfully----")
                print("\n")
                print("Your name is available on the customers list now")
                print(customerNames)
                print("\n")
                print("Note! Please remember the name and pin")
                print("=========================================================")
        mainMenu=input("please press enter key to go back to main menu")
    elif choiceNumber=="2":
        j=0
        print("choice Number 2 is selected by customer")
        while j<1:
            k=-1
            name=input("please enter name:")
            pin=input("please enter pin:")
            while k<len(customerNames)-1:
                k=k+1
                if name==customerNames[k]:
                    if pin==customerPins[k]:
                        j=j+1
                        print("Your current balance:",end="")
                        print(customerBalances[k],end="")
                        print("-/Rs\n")
                        balance=(customerBalances[k])
                        withdrawal=eval(input("Input amount to withdrawal:"))
                        if withdrawal>balance:
                            deposition=eval(input("please deposit a higher amount because your balance is insufficient: "))
                            balance=balance+deposition
                            print("Your current balance:",end="")
                            print(balance,end="")
                            print("-/Rs\n")
                            balance=balance-withdrawal
                            print("-\n")
                            print("----Withdraw Successful----")
                            customerBalances[k]=balance
                            print("your balance:",balance,end="")
                            print("-/Rs\n\n")
                        else:
                            balance=balance-withdrawal
                            print("-\n")
                            print("----Withdraw Successful----")
                            customerBalances[k]=balance
                            print("your balance:",balance,end="")
                            print("-/Rs\n\n")
        if j<1:
            print("Your name and pin does not match\n")
            break
        mainMenu=input("please press enter key to go back to main menu")
    elif choiceNumber=="3":
        print("choice Number 3 is selected by customer")
        n=0
        while n<1:
            k=-1
            name=input("please enter name:")
            pin=input("please enter pin:")
            while k<len(customerNames)-1:
                k=k+1
                if name==customerNames[k]:
                    if pin==customerPins[k]:
                        n=n+1
                        print("Your current balance:",end="")
                        print(customerBalances[k],end="")
                        print("-/Rs")
                        balance=customerBalances[k]
                        deposition=eval(input("Enter the amount to be deposited: "))
                        balance=balance+deposition
                        customerBalances[k]=balance
                        print("\n")
                        print("----Deposit successful----")
                        print("Your balance:",balance,end="")
                        print("-/Rs\n\n")
        if n<1:
            print("Your name and pin does not match!\n")
            break
        mainMenu=input("please press enter key to go back to main menu")
    elif choiceNumber=="4":
        print("choice Number 4 is selected by customer")
        k=0
        print("customer name list and balances mentioned below: ")
        print("\n")
        while k<=len(customerNames)-1:
            print("->customer=",customerNames[k])
            print("->Balance=",customerBalances[k],end="")
            print("-/Rs")
            print("\n")
            k=k+1
        mainMenu=input("please press enter key to go back to main menu")
    elif choiceNumber=="5":
        print("choice Number 5 is selected by customer")
        print("Thank you for visiting!")
        print("\n")
        print("visit again")
        break
    else:
        print("Invalid option selected by customer")
        print("Please try again")
        mainMenu=input("please press enter key to go back to main menu")