username = 'DkillaK'
password = 'password123!'

login_attempt_username = ""
login_attempt_password = ""
attempts = 0

while login_attempt_username != username and login_attempt_password != password and attempts < 5: 
    login_attempt_username = input('enter a username')
    login_attempt_password = input('enter a password')
    attempts += 1
    if login_attempt_username == username and login_attempt_password == password: 
        print('welcome!')
    elif attempts == 5:
        print('too many attempts. Restart program and try again.')