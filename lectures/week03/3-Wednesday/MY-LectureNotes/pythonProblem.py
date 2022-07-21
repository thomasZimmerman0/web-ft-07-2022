# in the dictionary below, extract the following 
# first_name 
# last_name 
# user's employement title 
# user's key_skills
# user's street address
# user's city 
# user's credit card number 
# user's subscription plan
user = {
    "id": 5487,
    "uid": "7b98255c-be80-483e-a508-1edbc9ffcc58",
    "password": "vtN0KSaejW",
    "first_name": "Regina",
    "last_name": "O'Keefe",
    "username": "regina.o'keefe",
    "email": "regina.o'keefe@email.com",
    "avatar": "https://robohash.org/anihilexcepturi.png?size=300x300&set=set1",
    "gender": "Woman",
    "phone_number": "+240 441.465.1205 x2861",
    "social_insurance_number": "471267534",
    "date_of_birth": "1964-08-23",
    "employment": {
        "title": "Forward Consulting Producer",
        "key_skill": "Networking skills"
    },
    "address": {
        "city": "West Rivabury",
        "street_name": "Kassulke Key",
        "street_address": "63277 Sarita Neck",
        "zip_code": "06366",
        "state": "Illinois",
        "country": "United States",
        "coordinates": {
        "lat": -11.987728561637226,
        "lng": -124.02257039722036
    }
    },
    "credit_card": {
        "cc_number": "5228-8351-1376-5139"
    },
    "subscription": {
        "plan": "Professional",
        "status": "Active",
        "payment_method": "Google Pay",
        "term": "Annual"
    }
}

result = 100

for i in range(21):
    print(result)
    result -= 5
    
result = 100
count = 0
while count < 21:
    print(result)
    result -= 5
    count += 1
    
for i in user:
    if i == 'first_name':
        print(user[i])
    if i == 'last_name':
        print(user[i])
    if i == 'employment':
        print(user[i]['title'])
        print(user[i]['key_skill'])
    if i == 'address':
        for j in user['address']:
            if j == user['address']['street_address']:
                print(j)
            if j == user['address']['city']:
                print(j)
