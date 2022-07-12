#0. Write a function that prints 1-10 using recursion

def print_upto_n(n):
    
    #base
    if n > 0:
        print_upto_n(n-1)
        print(n)

print_upto_n(5)


# 1. Write a function called power which accepts a base and an exponent.
# The function should return the power of the base to the exponent.
#def power(base, exponent):
    
    
def power (base, exponent):
    
    #base
    if exponent == 0:
        return 1
    return base * power(base, exponent -1)


print(power(4, 3))


# 2. Write a function factorial which accepts a number and returns
# the factorial of that number.  A factorial is the product of an
# interger and all the integers below it; eg. , factorial four( 4!) is
# equal to 24, because 4 * 3 * 2 * 1 equals 24.  factorial zero (0!) is always 1.

def factorial(number):
    
    if number == 1:
        return number
    return number * factorial(number -1)

print(factorial(5))
    
    
    
# 3. Write a function called recursiveRange which accepts a number and adds up all
# the numbers from 0 to the number passed to the function
def recursiveRange(number):
    
    if number < 1:
        return 0
    return number + recursiveRange(number - 1)

print(recursiveRange(5))

# 4. Write a recursive function called reverse which accepts
# a string and returns a new string in reverse

def reverse(string):
    if len(string) == 0:
        return
     
    temp = string[0]
    reverse(string[1:])

 
# Driver program to test above function
string = "Geeks for Geeks"
reverse(string)

# 5. Write a recursive function called isPalindrome which returns
# true if the string passed to it is a palindrome (reads the same forward and backward).
# Otherwise returns false.



# isPalindrome('awesome') // false
# isPalindrome('foobar') // false
# isPalindrome('tacocat') // true
# isPalindrome('amanaplanacanalpanama') // true
# isPalindrome('amanaplanacanalpandemonium') // false


# 6. Write  function called product ofArray which takes in
# an array of numbers and returns the product of them all


# 7. Write a recursive function called fib which accepts a number and
# returns the nth number in teh Fibonacci Sequence. Recall that the
# Fibonacci Sequence is the Sequence of whole numbers 1, 1, 2, 3, 5, 8, ... which
# starts with 1 and 1, and where ever number
# thereafter is equal to the sum of the previous two numbers.