#Variable for farenheit
Far = 60
Celsius = 40

# 
def FarenheitConvertor(Far):
	Celsius = "{:.2f}".format((Far-32) * 5/9)
	return (str(Far)+" grader Fahrenheit tilsvarer "+str(Celsius) +" grader Celsius")

def CelsiusConvertor(Celsius):
	Farenheit = "{:.2f}".format((Celsius * 9/5 )+32)
	return (str(Celsius)+" grader Celsius tilsvarer "+str(Farenheit) +" grader Farenheit")

print (FarenheitConvertor(Far))
print (CelsiusConvertor(Celsius))


def FarToCelToFar(far):
	F1 = Far
	Celsius = (Far-32) * 5/9
	F2 = "{:.2f}".format((Celsius * 9/5 )+32)
	return (""+str(F1)+ u"\N{degree fahrenheit}"+" = " + str(Celsius)+ u"\N{degree celsius}" + "\n" +str(Celsius) + " = " + str(F2)+u"\N{degree fahrenheit}" )
print (FarToCelToFar(10))	
