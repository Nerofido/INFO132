#Asking user for input of scentence
Sentence = "      Always	look on	the	bright	side           	of	life"
#Asking user for guess of how many characters
guess = 37

#taking away whitespace with replacing them with nothing
StripSentence = Sentence.replace(" ", "")
NumberOfLetters = len(Sentence)


#function for giving back true or false in non boolean terms
def guessLetters( Sentence, guess):
	NumberOfLetters = len(Sentence)
	if NumberOfLetters == guess : 
		return "That is True"
	else:
		return "That is False"

# calling up function with users input and the stripped sentence
print(guessLetters(StripSentence, guess))