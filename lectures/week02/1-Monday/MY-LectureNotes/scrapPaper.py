#Do not write copies of the same code

#! function parts
# def name_of_function(parameters):

#! call fuction 
# name_of_function(arguments)

def power(base, exponent):
    
    #base
    if(exponent == 0 ):
        return 1
    
    return base * power(base, exponent -1)

power(3, 2)
