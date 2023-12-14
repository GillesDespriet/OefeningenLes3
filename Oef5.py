#Rick&Morty API
import urllib.request
import json
import webbrowser

response = urllib.request.urlopen("https://rickandmortyapi.com/api/episode")
data = json.loads(response.read())
episodes = data["results"]
for episode in episodes:
    print("Aflevering:", episode["episode"], " - Naam:", episode["name"], " - Uitzendingsdatum:", episode["air_date"])


response = urllib.request.urlopen("https://rickandmortyapi.com/api/character")
data = json.loads(response.read())
all_chars = data["results"]
char_array = []
for char in all_chars:
    char_array.append(char["name"])

input = input("Geef een Rick & Morty personage of seizoen op: ")
if input in char_array:
    url = "https://rickandmortyapi.com/api/character/?name=" + input
    webbrowser.open(url)
elif input.isdigit():
    input = int(input)
    if input < 10:
        input = str(input)
        url = "https://rickandmortyapi.com/api/episode/?episode=S0" + input
        webbrowser.open(url)
    else:
        input = str(input)
        url = "https://rickandmortyapi.com/api/episode/?episode=S" + input
        webbrowser.open(url)