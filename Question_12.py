"""
12. Create the following class
    > BankAccount:
        * Initialization: __init__ () method
        1. Account holder name
        2. Account number
        3. Balance
        4. Pin

        * Check the pin of the user: check_pin():
        1. The method check_pin() checks if user has entered correct pin, then
        his/her account details will be shown.

        * Deposit the money: deposit(amount)
        1. Arguments:
            a. Amount: The amount to be added in the back account 
        2. Conditions:
            a. Check the pin number before deposit the money
            b. If user enters the correct pin:
                i. Add the money to the current balance of the user and show the message that “X rupees are successfully added to your account.”:
                    balance = balance + amount
                            
        * Withdraw the money: withdraw(amount) 
        1. Arguments:
            a. Amount: The amount to be withdrawn from the bank account
        2. Conditions:
            a. Check the pin number before withdrawing money
            b. If pin number is correct:
                i. Check if user has sufficient balance for withdraw i.e. if user has 1000 rupees in his bank and he tries to withdraw 1200 rupees then show the message that “Your account don’t have sufficient balance”.
                ii. If user has sufficient balance, then withdraw the money from account and show message that “X rupees has been withdrawn successfully” balance = balance – amount

        * __str__() method: Display the user account details: 
        1. It should be display like:
            Account Holder Name: User name
            Account Number: User Bank Account number 
            Total Balance: User total balance
    
    
    > Operations and their expected output:
        b1 = BankAccount(name=“Ram”,acct_num “12345”, balance=1000, pin=3456)
            o Print(b1)
            Account Holder Name: Ram
            Account Number: 12345       
            Total Balance: 10000

            o b1.deposit(200)
            1. It will ask user to enter the pin.
            2. If entered pin is wrong, then it should be print:
            Please enter correct pin.
            3. Else add the money to account
            200 rupees added to account successfully.
                        
            o Print(b1)
            Account Holder Name: Ram 
            Account Number: 12345 
            Total Balance: 10200
            
            o b1.withdraw(12000)
            1. It will ask user to enter the pin.
            2. If pin is entered correctly,
                a. Here Ram has 10000 rupees in his bank and he trying to withdraw 12000, then show the message:
                Your account don't have sufficient balance
                
            o b1.withdraw(8000)
            1. It will ask for the pin first
            2. If pin is entered correctly,
                a. 8000 will be withdrawn from the account.
       
            o Print(b1)
                Account Holder Name: Ram 
                Account Number: 12345 
                Total Balance: 2200
"""

class BankAccount():
    def __init__(self, name, acc_num, balance, pin):
        self.name = name
        self.acc_num = acc_num
        self.balance = balance
        self.pin = pin
    
    def check_pin(self):
        pin = int(input("Enter your Account Pin : "))
        return True if pin == self.pin else False
    
    def deposit(self, amount):
        print("\n Deposit Request Processing .....\n")
        pin_status = self.check_pin()
        if pin_status:
            self.balance += amount
            print(f'\n{amount} rupees are successfully added to your account.')
            print(f'Your Updated balance is {self.balance} rupees.\n')
        else:
            print('\nInvalid PIN. Please Try Again !!\n')
        
    def withdraw(self, amount):
        print("\n Withdraw Request Processing .....\n")
        pin_status = self.check_pin()
        if pin_status:
            if amount > self.balance:
                print("\nYour account don’t have sufficient balance. ")
            else:   
                self.balance -= amount
                print(f'\n{amount} rupees are successfully withdrawn to your account.')
                print(f'Your Updated balance is {self.balance} rupees.\n')
        else:
            print('\nInvalid PIN. Please Try Again !!\n')

    def __str__(self):
            return f"\nAccount Holder Details:\nName: {self.name}\nAcc No.: {self.acc_num}\nBalance: Rs.{self.balance}"


b1 = BankAccount("tarun",123456,5000,0000)
print(b1)
b1.deposit(1000)
b1.withdraw(2000)
print(b1)