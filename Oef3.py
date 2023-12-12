#Countries API
import urllib.request
import json
import webbrowser

#inwoners van Zwitserland
response = urllib.request.urlopen("https://restcountries.com/v3.1/name/switzerland?fields=population")
if response.getcode() == 200:
    output = json.loads(response.read())
    population = output[0]['population']
    print(population)


#Lijst van landen met euro als valuta
webbrowser.open("https://restcountries.com/v3.1/currency/eur?fields=name")

name_string = input("Geef naam van een land op:")
url = "https://restcountries.com/v3.1/name/" + name_string
webbrowser.open(url)
