# planets = ["Earth", "Jupiter", "Neptue", "Mars", "Saturn", "Mercury", "Uranus", "Venus"]
# i = 0


# planets.append("Pluto")

# while i <= 8:
#     print(f"{planets[i].lower()}")
#     i += 1

# print(f"{len(planets)}\n\n\n")



# index = 0
# sum = 0

# nums = [4, 2, 4, 2, 9, 12, 67, 34, 2]

# while index < len(nums): #num
#     sum += nums[index]
#     index += 1

# print(sum)

# index = 1
# max_num = nums[0]

# while index < len(nums):
#     if nums[index] > max_num :
#         max_num =nums[index]
#     index += 1

# print(f"{max_num}")

# index = 1
# min_num = nums[0]

# while index < len(nums):
#     if nums[index] < min_num :
#         min_num =nums[index]
#     index += 1

# print(f"{min_num}")

# todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

# index = 0
# running = True
# while running:
#     #print out menu
#     index = 0 
#     while index < len(todos):
#         print(f"{index +1} {todos[index]}")
#         index += 1 
#     keep_running = input('Do you want to add an item? Y or N >>')
    
#     if(keep_running.lower() == 'n'):
#         running = False
#     else:
#         #ask for an input
#         new_todo = input('enter a new todo >>')
#         #append it to our list
#         todos.append(new_todo)
        
# list1 = [1, 2, 3, 4, 5,]
# list2 = [6, 7, 8, 9, 10]

# lists = list1 + list2

# print(lists)        
    
ClearLakeCities = ["League City", "Kemah", "Seabrook", "Webster", "El Lago"]

HoustonCities = ["Katy", "Memorial City", "Sugar Land","The Heights", "River Oaks", "Pasadena"]

Houston =  ClearLakeCities + HoustonCities

count = len(Houston)

print(f"{count}")    

Houston.append("Farmer Land")
Houston.append("Constantinople")
Houston.insert(12, "Denver")

index = 0
while index < len(Houston) :
    print(f"{Houston[index]}")
    index += 1
    
htx1 = Houston[0:4]
print(f"{htx1}")
htx2 = Houston[3:6]
print(f"{htx2}")
htx3 = Houston[12:]
print(f"{htx3}")

del Houston[14]