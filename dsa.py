#RANDOM DSA IN PYTHON

tel = {'jack': 1234, 'ben': 4567, 'ris': 8904}
#print(tel['ris'])

tel['ze'] = 13425664
sorted(tel)

#print(tel['ze'])

#print(list(tel))

#for k in tel.items():
    #print(k)

myList = ['tic', 'tac', 'toe']
print(len(myList))

#for n in myList:
  #  print (n)
 #   print('.......................')
    
#for i in range (len (myList)):
  #  print(myList[i])
   # print('........................')

#presidents = ['kibaki', 'uhuru', 'mwai', 'daniel', 'mzee']
#for num, name in enumerate(presidents):
 #   print(num, name)

question = ['name', 'food', 'career']
answer = ['Harry', 'pork', 'elite software dev']

for q, a in zip(question, answer):
    print ("What is your {0}? It is {1}.".format(q, a))

r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
for i in r:
    print(i)