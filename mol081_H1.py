#assignment 1 
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

#assignment 2
# converts from farenheit
def FarenheitConvertor(Far):
	Celsius = format((Far * 5/9 -32) , ".2f")
	return (Celsius)

# converts from celsisus
def CelsiusConvertor(Celsius):
	Farenheit = format((Celsius * 9/5 )+32 , ".2f")
	return (Farenheit)

#function that takes in arguments and have a predefined value for scale
def converter(degre , scale = "C" ):
	if scale == "C":
		return (CelsiusConvertor(degre))
	elif scale == "F":
		return (FarenheitConvertor(degre))

#Call function and print outcome
print (converter( 44 , "C"))
print (converter( 70))
print (converter( 10 , "F"))

#assignment 3

#golbal variables to be used in bank
balance = 500 
interest_rate = 0.01
#saves your acount history of withdrawls and deposits
history = []

#function to put in deposit
def deposit (amount):
	global balance
	balance += amount
	history.append("+" + str(amount))
	if balance >1000000:
		return ("Congratulations, you get a higher interest rate!")
	return (balance)

#Function for withdrawal and cheking if you have the balance
def withdrawal(amount):
	global balance
	if balance>amount:
		balance -= amount
		history.append("-" + str(amount))
		return balance
	elif balance <amount:
		return("Too large withdrawal")

#to change interest rate if your balance is over or under 1 000 000 nok
def calculate_interest():
	global balance
	global interest_rate
	if balance > 1000000:
		interest_rate = 0.02
		return (balance*interest_rate)
	elif balance<1000000:
		interest_rate = 0.01
		return (balance*interest_rate)

#To give you the amount in principla you have made over one year with your current balance
def interest_settlement():
	global balance
	global interest_rate
	if balance > 1000000:
		interest_rate = 0.02
		balance += balance*interest_rate
		return (balance)
	elif balance<1000000:
		interest_rate = 0.01
		balance += balance*interest_rate
		return (balance)

#interface with the terminal
def gui():
	global balance
	global interest_rate
	while True:
		print ("1 – show balance \n2 – deposit  \n3 – withdraw \n4 – interest settlement \n5 - last Changes \n6 - Terminate session")
		choce = input("Please enter your option")
		if choice == 1:
			print( balance)
		elif choice == 2:
			amount = input("How much would you like to deposit?")
			print(deposit(amount))
		elif choice == 3:
			amount = input("How much do you want to withdraw") 
			print(withdrawal(amount))
		elif choice == 4:
			print(interest_settlement())
		elif choice == 5:
			print(history[-1])
			print(history[-2])
			print(history[-3])
		#will break session on any other input 
		else:
			break
#call up function to run your interface
gui()

#assignment 4
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