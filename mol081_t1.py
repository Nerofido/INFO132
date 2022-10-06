#1a print name 
#variables with name
FirstName = "Nero"
LastName ="Fido"

#first print
print (FirstName)
print (LastName)

#1b print name in a diffrent way
#Second print with use of breaklines 007 style
print ("Hi my name is "+ LastName +". \n" +FirstName+" "+ LastName+".")


#2 Convert NOK to Euro and Dollar
#Variabel to use in formula
Kroneamount = 10

#Formula to calculate and return Euro and dollar amount from NOK
def EuroDollar (Kroneamount):
	euro =  "{:.2f}".format(Kroneamount/9.74)
	dollar = "{:.2f}".format(Kroneamount/9.80)
	return("NOK "+ str(Kroneamount)+" corresponds to " + str(euro)+"€ and "+ str(dollar)+"$")

print (EuroDollar(Kroneamount))