#function to calculate your average earnings during your poop time,
#predetermined with average time for poop and hourly wage in nok
def poopcalc(minutes= 2, wage= 322):
	cost = format((wage /60) * minutes , ".2f")
	costperyear = format(((minutes * 230)/60)* wage , ".2f")
	print ("your pooptime made you kr {}"  .format(cost))
	print ("And you will make on average {} kr per year" .format(costperyear))

poopcalc(2,400)
poopcalc (input("How loong do you poop?"), input("How much do you make an hour?"))