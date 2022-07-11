
myString = "I am a leet programmer"

listString = list(myString)

for i in range(len(listString)):
    if listString[i] == 'a' or listString[i] == 'A':
         listString[i ]= '4'
    elif listString[i] == 'e' or listString[i] == 'E':
         listString[i ]= '3'
    elif listString[i] == 'g' or listString[i] == 'g':
         listString[i ]= '6'
    elif listString[i] == 'i' or listString[i] == 'I':
         listString[i ]= '1'
    elif listString[i] == 'o' or listString[i] == 'O':
         listString[i ]= '0'
    elif listString[i] == 's' or listString[i] == 'S':
         listString[i ]= '5'
    elif listString[i] == 't' or listString[i] == 'T':
         listString[i ]= '7'

myString = ''.join(listString)

print(myString)
