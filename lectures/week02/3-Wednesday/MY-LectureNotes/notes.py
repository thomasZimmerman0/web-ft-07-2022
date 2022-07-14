#template for creating a class

class Student:
    pass
    #?properrties(atributes):
        #-
        #-
        #-
    #?functions(behavior):
        #-
        #-
        #-


class Student: 
    def __init__(self, fName, my_city): #THE CONSTRUCTOR!
        print("I'm a constructor and I was just called")
        self.firstName = fName
        self.city = my_city
    # firstName = "Chloe"
    # city = "London"
    
    def greeting(self):
        print('hello')

student1 = Student("chloe", "london")
student2 = Student("tri", "philly")

print(student1.firstName)
print(student2.firstName)
#student1.greeting()

# class Area:
    
#     pi = 3.14

#     def circle(r):
#         return pi * r * r

# class Calculus:
#     def intergration():
#         pass
#     def differentiaition():
#         pass
    
# Calculus.intergration()

class Area:
    PI = 3.14
    
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(f'I am a {self.name} pi={self.PI}')
        
    circle = Area('circle')
    
    