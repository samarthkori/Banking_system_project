class Bank:
    
    def __init__(self,account_holder_name,phone_number,city,account_type,account_number,pre_deposit):
        self.account_holder_name=account_holder_name
        self.phone_number=phone_number
        self.city=city
        self.account_type=account_type
        self.account_number=account_number
        self.pre_deposit=pre_deposit

class Account(Bank):
    
    def deposit(self,amount):

        self.pre_deposit+=amount
        print(f'your bank account {self.account_number} has been credited with {amount} rs')
        print(f'your balance in {self.account_number} is {self.pre_deposit} rs')

    def withdraw(self,amount):

        if self.pre_deposit<amount:
            print("Insufficent funds")
        else:
            self.pre_deposit-=amount
        print(f'your bank account {self.account_number} has been debited with {amount} rs ')
        print(f'your current balance is {self.pre_deposit} rs')

    def check_balance(self):

        print(f'your balance in {self.account_number} is {self.pre_deposit} rs')

    def intrest(self):

        intrest_rate=0.04
        intrest_amount=self.pre_deposit*intrest_rate
        print(f'The intrest amount is {intrest_amount} rs')
        updated_balance=self.pre_deposit+intrest_amount
        print(f'The balance amount after adding interest {updated_balance} rs')

class Savings(Account):
     
     def withdraw(self,amount):
            
            if self.pre_deposit<amount:
                print("Insufficent funds")
            else:
                self.pre_deposit-=amount
                print(f'your bank account {self.account_number} has been debited with {amount} rs')
            print(f'your current balance is {self.pre_deposit} rs')

class Current(Account):

    def withdraw(self,amount):
            over_withdrawl_limit=1000

            if self.pre_deposit + over_withdrawl_limit<amount:
                print("Insufficent funds")
            else:
                if self.pre_deposit>amount:
                    self.pre_deposit-=amount
                    print(f'your bank account {self.account_number} has been debited with {amount} rs')
                    print(f'your current balance is  {self.pre_deposit} rs')

                elif self.pre_deposit==amount:
                    self.pre_deposit-=amount
                    print(f'your bank account {self.account_number} has been debited with {amount} rs')
                    print(f'your current balance is  {self.pre_deposit} rs')
                    
                elif self.pre_deposit<amount:
                    self.pre_deposit+=over_withdrawl_limit
                    self.pre_deposit-=amount
                    print(f'your bank account {self.account_number} has been debited with {amount} rs')
                    print(f'your current balance is  -{over_withdrawl_limit-self.pre_deposit} rs')
                    
    def check_balance(self):
        print(f'your balance in {self.account_number} is {self.pre_deposit} rs')
                                        
                
                

print("Welcome To our bank\n")

print("Please go to the counter number one to get new account created\n ")

print("Please go to the counter number two to get details and services of exisitng account\n")

print("Please go to the counter number three to get details about loan\n")

print("Please go to the counter number four to get locker services\n ")
accounts=[]
while True:
    print("Counter 1.Create new account\n")

    print("Counter 2.Services for exisitng account\n")

    print("Counter 3.Details about Loan\n")

    print("Counter 4.Exit bank\n")

    try:
        x=input("Go_to_counter_number : ")
        counters=["1","2","3","4"]
        if x not in counters:
            raise Exception("Enter the valid counter number")

    except Exception as e:
        print(e)

        while True:
            x=input("Go_to_counter_number : ")
            counters=["1","2","3","4"]
            if x not in counters:
                print(e)
                continue
            else:
                break

    if x=="1":
        
        print("Please co-operate with bank by brefing your credentials being asked")

        #This is Account holder name exception handling block
        while True:
            account_holder_name=input("Enter your name : ")
            if any(char.isdigit() for char in account_holder_name):
                print("Name should hold only alphabets")

                continue

            elif not all(char.isalpha() for char in  account_holder_name.replace(" ","")):
                print("Name should not contain special characters")
        

                continue

            else:
        
                break
   

#This is phone number exception handling block  
#                 
        while True:
            phone_number=input("Enter the account holder's phone number:")
            if  not all(num.isdigit() for num in phone_number  ):
                print("Phone number should contain only numbers")
                continue
            elif len(phone_number)!= 10:
                print("Please enter the valid phone number")
                continue
            else:
                break
    

        while True:
            city=input("Enter Your city name : ")
            if not all(char.isalpha() for char in city ):
                print("Not found any such cities")
                continue
            else:
                break

        try:
            account_type=input("Enter the type of account which you have to open : ").lower()
            if account_type != "savings" and account_type !="current":
                raise Exception("Please enter the coorect account type which you to open")
                       
        except Exception as e: 
            print(e)

            while True:    
                account_type=input("Enter the type of account which you have to open : ").lower()
                if account_type != "savings" and account_type !="current":
                    print(e)
                    continue
                else:
                    break
                                                      


        import random

        ids=random.randint(100000000000,999999999999)
        print("Please press Enter for account generation\n")

        account_number=input(ids)
        
        print("Your account is generated\n")

        while True:
            pre_deposit = input("Enter the initial deposit amount:\n").strip()

    
            if not pre_deposit.isdigit():
                print("Please enter the deposit amount in digits only.")
                continue
            else:
                pre_deposit=int(pre_deposit)
                break
            
        print("PLease give the id throug which you can avail services on your account\n")
        print("Press enter for account creation\n")
        print("Processing Your account is being created....\n")
        print("Account creation sucessfull\n")
        print("Please remeber your account created order number for smooth processing\n")

        if account_type=="savings":
            account=Savings(account_holder_name,phone_number,city,account_type,account_number,pre_deposit)
        elif account_type=="current":
            account=Current(account_holder_name,phone_number,city,account_type,account_number,pre_deposit)

        accounts.append(account)

        print(accounts)


        file = open("accounts.txt", "a")

        file.write("\nAccount Holder Name: " + account_holder_name)
        file.write("\nPhone Number: " + phone_number)
        file.write("\nCity: " + city)
        file.write("\nAccount Type: " + account_type)
        file.write("\nAccount Number: " + account_number)
        file.write("\nInitial Deposit: " + str(pre_deposit))
        file.write("\n-------------------------")

        file.close()
       

    elif x=="2":
       class Bank:
    
        def __init__(self,account_holder_name,phone_number,city,account_type,account_number,pre_deposit):
            self.account_holder_name=account_holder_name
            self.phone_number=phone_number
            self.city=city
            self.account_type=account_type
            self.account_number=account_number
            self.pre_deposit=int(pre_deposit)

        class Account(Bank):
    
            def deposit(self,amount):

                self.pre_deposit+=amount
                print(f'your bank account {self.account_number} has been credited with {amount} rs')
                print(f'your balance in {self.account_number} is {self.pre_deposit} rs')

            def withdraw(self,amount):

                if self.pre_deposit<amount:
                    print("Insufficent funds")
                else:
                    self.pre_deposit-=amount
                    print(f'your bank account {self.account_number} has been debited with {amount} rs ')
                    print(f'your current balance is {self.pre_deposit} rs')

            def check_balance(self):

                print(f'your balance in {self.account_number} is {self.pre_deposit} rs')

            def intrest(self):

                intrest_rate=0.04
                intrest_amount=self.pre_deposit*intrest_rate
                print(f'The intrest amount is {intrest_amount} rs')
                updated_balance=self.pre_deposit+intrest_amount
                print(f'The balance amount after adding interest {updated_balance} rs')

        class Savings(Account):
     
            def withdraw(self,amount):
            
                if self.pre_deposit<amount:
                    print("Insufficent funds")
                else:
                    self.pre_deposit-=amount
                    print(f'your bank account {self.account_number} has been debited with {amount} rs')
                    print(f'your current balance is {self.pre_deposit} rs')

        class Current(Account):

            def withdraw(self,amount):
                over_withdrawl_limit=1000

                if self.pre_deposit + over_withdrawl_limit<amount:
                    print("Insufficent funds")
                else:
                    if self.pre_deposit>amount:
                        self.pre_deposit-=amount
                        print(f'your bank account {self.account_number} has been debited with {amount} rs')
                        print(f'your current balance is  {self.pre_deposit} rs')

                    elif self.pre_deposit==amount:
                        self.pre_deposit-=amount
                        print(f'your bank account {self.account_number} has been debited with {amount} rs')
                        print(f'your current balance is  {self.pre_deposit} rs')
                    
                    elif self.pre_deposit<amount:
                        self.pre_deposit+=over_withdrawl_limit
                        self.pre_deposit-=amount
                        print(f'your bank account {self.account_number} has been debited with {amount} rs')
                        print(f'your current balance is  -{over_withdrawl_limit-self.pre_deposit} rs')
                    
            def check_balance(self):
                print(f'your balance in {self.account_number} is {self.pre_deposit} rs')




        

        k=accounts[int(input("Please enter the order number of your account creation\n "))]
        #k is just a variable for accessing the accounts

        

        while True:
            print("1.deposit")
            print("2.withdraw")
            print("3.check balance")
            print("4.check intrest amount and balance of after adding inrest")
            print("5.Choose this option to exit:")

           
            choice=int(input("Enter the service needs to be provided:"))

            if choice==1:
                
                    amount=int(input("Enter the amount need to be deposited:"))
                    k.deposit(amount)

            elif choice==2:
                
                    amount=int(input("Enter the amount need to be deposited:"))
                    k.withdraw(amount)

            elif choice==3:    
                k.check_balance()

            elif choice==4:
                k.intrest()

            elif choice==5:
                break

            else :
                print("Please enter the valid choice")

    elif x=="3":
        while True:
            print("Welcome to loan section\n")
            print("Domain 1.House loan\n")
            print("Domain 2.Vehicle loan\n")
            print("Domain 3.Personal loan\n")
            print("Domain 4.Education loan\n")
            print("Choose 5 to exit the loaning section\n")

            try:
                Domain=["1","2","3","4","5"]
                y=input("Enter the Domain number : ")
                if y not in Domain:
                    raise Exception("Please give the correct domain to get info")

            except Exception as e:
                print(e)

                while True:
                    Domain=["1","2","3","4","5"]
                    y=input("Enter the Domain number : ")
                    if y not in Domain:
                        print(e)
                        continue
                    else:
                        break

            if y=="1":
                file=open("House loan.txt","r")
                print(file.read())
                file.close()

            elif y=="2":
                file=open("Vehicle loan.txt","r")
                print(file.read())
                file.close()

            elif y=="3":
                file=open("Personal loan.txt","r")
                print(file.read())
                file.close()

            elif y=="4":
                file=open("Education loan.txt","r")
                print(file.read())
                file.close()

            elif y=="5":
                print("Exited loan domain")
                break
    
    elif x=="4":
        print("Exited from bank,Thank you")
        break


    










                



    


   










