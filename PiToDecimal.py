#importing Math module for pi
import math

# missing variable format rule
decimals = 17
#function to return decimals
def printPi(decimals= 2):
	#
	d = "." + str(decimals) + "f"
	if (decimals < 2 or decimals == "") : 
		return format(math.pi, ".2f")
	elif (decimals > 2 and decimals < 15): 
		return format(math.pi , d)
	elif (decimals > 15):
		print ("Too many decimals")
		return math.pi
	else:
		return format(math.pi, ".2f")

print(printPi(decimals))
