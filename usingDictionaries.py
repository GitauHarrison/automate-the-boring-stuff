spam = {'name': 'Tash', 'age': '7'}

#find the keys in dictionary
print('age' in spam.keys())


#find only the value
print(8 in spam.values())

#print key and value using the items() function
for i, h in spam.items():
    print(i, h)

#use the get() method to find an item in a dictionary
#set a fallback value in case it does not exist in the dict
print('I have a dog called '+ spam.get('eggs', 'rex') + ' and he is ' + spam.get('age', 0) + ' years old' )


#how to create a default value in a dictionary using the setdefault() function
#option 1
spam = {'name': 'Cool', 'age': 2}
if 'color' not in spam:
    spam['color'] = 'black'
    print(spam)

#option 2
spam =  {'name': 'Cool', 'age': 2}
spam.setdefault('car','lambo')
print(spam)