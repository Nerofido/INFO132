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