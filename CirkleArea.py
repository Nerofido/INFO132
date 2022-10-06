#importing Math module for pi
import math
#Asking for Radia
radius = 6.73


# Function calculating area with 3 decimal places
def AreaCirkle(radius):
	area = format(math.pi * radius **2 , ".3f")
	print (area)

#Calling up function with user number
AreaCirkle(radius)

print (math.pi)

