#import random mudule to make random numbers
import random 
#make three random numbers
a =  random.randint(1,9)
b =  random.randint(1,9)
c =  random.randint(1,9)

#Add them to a lis
unsortedList = [a,b,c]
#sort that list and save in new list
sortedList = sorted(unsortedList)
print (sortedList)