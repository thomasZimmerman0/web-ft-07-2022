



my_dictionary = {}

#? initalize 

contacts = {
    "firstName": "Shannon",
    "phone": "333-333-3333",
    "city": "Phoenix",
    "zip": 77002,
    "isFriendly": True,
    0 : 12,
    True: False,
    "myList" : [0, 2, 4],
    'some_dictionary' : { 'cell': "333-333-3333"}
}

result = contacts["myList"][1]


contacts["state"] = 'Arizona'
contacts['firstName'] = 'Tommy'

result = 'state' in contacts

if 'firstName' in contacts:
    print(contacts["firstName"])
    
keys = contacts.keys()

print(keys)

for key in contacts.keys():
    print(f"{key} : {contacts[key]}")
    
del contacts["phone"]

print(contacts)


