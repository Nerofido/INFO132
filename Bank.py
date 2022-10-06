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