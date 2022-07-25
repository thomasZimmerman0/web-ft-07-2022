   
class Bank:
    
    selected_account = 0
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []
        
    #Allows hard coding accounts into Bank's accounts
    def add_account(self, name, balance):
        account = Account(name, balance)
        self.accounts.append(account)
    
    #Allows user to add accounts while programming is running through input
    def add_account_improved(self):
        name = input('What is the name you\'ll be adding to the acccount?')
        balance = float(input('How much is being deposited?'))
        account = Account(name, balance)
        self.accounts.append(account)
    
    #Matches name input to with each element in list of accounts    
    def search_name(self):
        name = input("Who is the person you are trying to lookup?")
        for i in self.accounts:
            if i.name == name:
                print(f'Name: {i.name} \nBalance : {i.balance}')
    
    #Prints the sum of all accounts' balance
    def total_bank_balance(self):
        total = 0
        for i in self.accounts:
            total += i.balance
        print(total)
    
    #Prints each account name in account list, preceeded by a number
    def list_members(self):
        count = 1
        for i in self.accounts:
            print(f'{count}.{i.name}')
            count += 1
    
    #Compares each account to each other to find the highest holder 
    #(Does not account for 2 highest accounts with equal value)

    def highest_account(self):
        highest_balance = self.accounts[0].balance
        highest_account = ''
        for i in self.accounts:
            if i.balance >= highest_balance:
                highest_balance = i.balance
                highest_account = i.name
        print(f'The highest account holder is {highest_account} with ${highest_balance}')
    
    #Sets 'selected account' variable to an interger that can be reffered back to for transactions
    def select_account(self): 
        self.list_members()
        self.selected_account = float(input('Which account holder would you like to transact from? ')) -1 
        print(f'You have selected {self.accounts[self.selected_account].name}')
    
    def withdrawal(self):
        self.select_account()
        amount = float(input('How much would you like to withdrawal? >>'))
        self.accounts[self.selected_account].balance -= amount
        print(f'''
${amount} was withdrawn from {self.accounts[self.selected_account].name}\'s account.
new balance: {self.accounts[self.selected_account].balance}''')
        
    def deposit(self):
        self.select_account()
        amount = float(input('How much would you like to deposit? >>'))
        self.accounts[self.selected_account].balance += amount
        print(f'''
${amount} was deposited to {self.accounts[self.selected_account].name}\'s account.
new balance: {self.accounts[self.selected_account].balance}''')
    
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


TDBank = Bank('TDBank', '1234 Street st')

TDBank.add_account('Bob', 10000)
TDBank.add_account('Dan', 2000)
TDBank.add_account('Jim', 3000)
TDBank.add_account('Tim', 4000)

while True:
    print('''
Welcome to Banker Sim
=====================
1. Add an account
2. Lookup account information
3. List all active accounts
4. Get sum of all accounts
5. Most valued customer
6. Withdraw
7. Deposit
8. Exit''')

    option = int(input("Please choose one of the above options (enter 1-8) >> "))
    
    if option == 1:
        TDBank.add_account_improved()
    elif option == 2:
        TDBank.search_name()
    elif option == 3:
        TDBank.list_members()
    elif option == 4:
        TDBank.total_bank_balance()
    elif option == 5:
        TDBank.highest_account()
    elif option == 6:
        TDBank.withdrawal()
    elif option == 7:
        TDBank.deposit()
    elif option == 8:
        break
    else:
        pass
print('Goodbye')