#random number devider
#import random module
import random
#asking user for a integer
OriginalNumber = 5
#getting a random integer to get for the cross sum
NewNumber = random.randint(0,9)
combiNumber = int(str(OriginalNumber) +str(NewNumber))
#Devide the new cross sum number by the user inputed integer
devided = combiNumber/OriginalNumber

#print numbers
print (NewNumber)
print (combiNumber)
print (devided)