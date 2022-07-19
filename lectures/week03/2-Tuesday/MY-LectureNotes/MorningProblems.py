# 1. Determine the total distance travelled and the
# total time it takes to get there by summing up
# the total distance and the total time in the list below

from turtle import distance


trips = [
    { "distance": 34, "time": 10 },
    { "distance": 90, "time": 50 },
    { "distance": 59, "time": 25 },
    { "distance": 83, "time": 60 },
    { "distance": 27, "time": 15 },
    { "distance": 68, "time": 90 }
]

def totals(trips):
    total_distance = 0
    total_time= 0
    
    for i in range(len(trips)):
        total_distance += trips[i]["distance"]
        total_time += trips[i]["time"]
        
    print(total_distance)
    print(total_time)
        
totals(trips)

# 2. Implement a 'pluck' function. 
# Pluck should accept a list and a string representing a 
# property name and return a list containing that property from each object.

# example
paints = [{"color": 'red', "text-align": "right"}, {"color": 'blue', "margin": "0px"}, {"color": 'yellow', "padding": "5px"}]
# pluck(paints, 'color')
#     returns =>>>>> ['red', 'blue', 'yellow']

def pluck(list, string):
    
    new_list = []
    
    for i in range(len(list)):
        if string in list[i]:
            new_list.append(list[i][string])
    
    print(new_list)
    
pluck(paints, 'text-align')