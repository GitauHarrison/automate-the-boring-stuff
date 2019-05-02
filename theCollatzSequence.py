#THE COLLATZ SEQUENCE

#Write a function named collatz() that has one parameter named number. 
# #If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.

#Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print (number)
        return number
    elif number % 2 == 1:
        new_number = 3 * number + 1
        print (new_number)
        return new_number

try:
    user = int(input ('Type a number: '))
    while user != 1:
        user = collatz(int(user))
except ValueError:
        print('Enter an interger')


#Add try and except statements to the previous project to detect whether the user types in a noninteger string. 
# Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). 
# In the except clause, print a message to the user saying they must enter an integer.





    