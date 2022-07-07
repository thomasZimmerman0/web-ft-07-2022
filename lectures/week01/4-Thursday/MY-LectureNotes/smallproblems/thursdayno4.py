username = "clintwestwords"
password = "le-epic_password"

un_attempt = ""
pw_attempt = ""

attempts = 5

un_attempt = input("What is your Username?: ")
pw_attempt = input("What is your password?: ")

while un_attempt != username or pw_attempt != password:
    attempts -= 1
    print("Incorrect username password combination, please try again")
    un_attempt = input("What is your Username?: ")
    pw_attempt = input("What is your password?: ")
    
    if attempts == 0:
        print("You have reached the maximum number of attempts, access denied")
        break
        
if attempts == 0:
    print("access denied")
    
elif attempts > 0 :
    print("Welcome clintwestwords!")
    
    


