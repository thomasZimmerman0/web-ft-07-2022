


#1. Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"])
names =  ["Elie", "Tim", "Matt"]
letters =[]

for i in names:
    letters.append(i[0:1])
    
print(letters)
#2. Print out the numbers 1-10 from the list below
nums = [
    {"num": 1},
    {"num": 2},
    {"num": 3},
    {"num": 4},
    {"num": 5},
    {"num": 6},
    {"num": 7},
    {"num": 8},
    {"num": 9},
    {"num": 10},
]

for i in nums:
    print(i['num'])

#3. Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] return a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

abbreviations = ["CA", "NJ", "RI"] 
state_names = ["California", "New Jersey", "Rhode Island"]

dicts = {}
keys = range(len(abbreviations))

for i in keys:
        dicts[abbreviations[i]] = state_names[i]
        
print(dicts)
#4. see colorsProblems.py