#Variabel to use in formula
Kroneamount = 10

#Formula to calculate and return Euro and dollar amount from NOK
def EuroDollar (Kroneamount):
	euro =  "{:.2f}".format(Kroneamount/9.74)
	dollar = "{:.2f}".format(Kroneamount/9.80)
	return("NOK "+ str(Kroneamount)+" corresponds to " + str(euro)+"€ and "+ str(dollar)+"$")

print (EuroDollar(Kroneamount))
