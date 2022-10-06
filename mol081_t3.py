#Assignment 1
#Here are two logical (or boolean) expressions :
#• x!=7 and y<=50                             	= False
#• (x>7 or 50<y) and (x>y or y<100)				= True
#What are the expressions evaluated to when x = 9, and y = 66?
# the first expression is False and the second is True

#2.
def mayoroftulleby ():
	#variable used in function. asking user for input of age and recidency length
	yourAge  = input ("Please state your age")
	recidencyTulleby = input("How long have you lived in Tulleby?") 
	mayorMinimum = 30
	mayorRecidency= 9
	consulMinimum = 25
	consulRecidency = 5 
	ageLeft = mayorMinimum - yourAge 
	recidencyLeft = mayorRecidency - recidencyTulleby
	if ((ageLeft <= 0) and (recidencyLeft <= 0)):
		return ("You can become the mayor or sit in the city council.")
	elif(consulMinimum<=yourAge and recidencyTulleby>=consulRecidency):
		return("You are qualified to sit in the city council. You can try again in "+str(recidencyLeft)+ " years to become the mayor.")
	else: 
		#do not take in to account that the user can be under age to be counsilmember or mayor as in the provided example
		return("You are not eligible yet, try again in "+ str(consulRecidency - recidencyTulleby) + " year.")

#take away the next pund sing to run mayoroftulleby
#print(mayoroftulleby())

#3 
#make a function that don't have nestle if statments
def checkvalue():
	x = int(input('Number: '))
	if (x>=10):
		print('at least 10')
	elif (x >=5 and x <10 ):
		print('6, 7, 8 or 9')
	else:
		print('at most 5')

#Take away pund sing to run checkvalue
#checkvalue()

#4
#easy solution where the program just prints out the desired output
table =("""
  | 1 2 3 4 5 6 7 8 9
--+-----------------------------
1 | 1 2 3 4 5 6 7 8 9
2 | 2 4 6 8 10 12 14 16 18
3 | 3 6 9 12 15 18 21 24 27
4 | 4 8 12 16 20 24 28 32 36
5 | 5 10 15 20 25 30 35 40 45
6 | 6 12 18 24 30 36 42 48 54
7 | 7 14 21 28 35 42 49 56 63
8 | 8 16 24 32 40 48 56 64 72
9 | 9 18 27 36 45 54 63 72 81

""")

print (table)
