# Where USD is the base currency you want to use
url = "https://data.norges-bank.no/api/data/EXR/B.USD.NOK.SP?format=sdmx-json&lastNObservations=60&locale=en"

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print (data)
