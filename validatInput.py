#the isX string methods
while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
         break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only): ')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers')


'''
isalpha() - returns TRUE only letters and it is not blank
isalnum() - returns TRUE only letters and numbers and is not blank
isdecimal() - returns TRUE consists of numeric characters and is not empty
isspace() - returns TRUE if string consists of only spaces, tabs, new-lines and is not blank
istitle() - returns TRUE if the string consists of words that begin with uppercase letters followed by lowercase letters

'''