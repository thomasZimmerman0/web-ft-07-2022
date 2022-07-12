import contacts

for i in range(len(contacts.data)):
    print(contacts.data[i]['name'])
    print(f"street: {contacts.data[i]['address']['street']}")
    print(f"suite: {contacts.data[i]['address']['suite']}")
    print(f"city: {contacts.data[i]['address']['city']}")
    print(f"zipcode: {contacts.data[i]['address']['zipcode']}")
    print()