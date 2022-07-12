import pickle #immports a module that allows you to export data to a .pickle file

#reading from a file

#loading

try:
    with open('phonebook.pickle', 'rb') as fh: 
        phonebook = pickle.load(fh)
except:
    phonebook = {}
    
selection = 0
running = True
enter_txt = '(press Enter to continue)'


def look_up():
    search = input('what is the name of the person you are trying to look up? >>')
    print(f"{search}'s phone number is: {phonebook[search]} {enter_txt}")
    pressenter = input()  #forces user to press 'Enter' before continuing


def set_entry():
    name = input("Name >> ")
    phone = input("Phone Number >> ")
    phonebook[name] = phone
    print(f"Entry stored for {name} {enter_txt}")
    pressenter = input() 

def del_entry():
    name = input('What is the name of the person you are trying to delete? >> ')
    del phonebook[name]
    print(f"{name} has been deleted {enter_txt}")
    pressenter = input()

def print_all():
    for i in phonebook:
        print(f'{i} : {phonebook[i]}') #walks through each element and prints accordingly 
    print(f'{enter_txt}')    
    pressenter = input()   
    
    
def quit():
    #save the data from phonebook into this file
    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(phonebook, fh)
    return False
    
        
while running:
    print('''
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit''')
    
    
    selection = int(input('What do you want to do (1-5)? >>'))
    
    
    if selection == 1:
        look_up()
        
    elif selection == 2:
        set_entry()
        
    elif selection == 3:
        del_entry()
        
    elif selection == 4:
        print_all()
        
    elif selection == 5:
       running = quit()

print('Bye')