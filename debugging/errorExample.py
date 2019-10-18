def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()

# Obtaining an exception as a string on the interpreter


#import traceback
#try:
         #raise Exception('This is the error message.')
#except:
         #errorFile = open('errorInfo.txt', 'w')
         #errorFile.write(traceback.format_exc())
         #errorFile.close()
         #print('The traceback info was written to errorInfo.txt.')