#Rick&Morty API
import urllib.request
import json
import webbrowser

response = urllib.request.urlopen("https://ricdkandmortyapi.com/api/episode")
data = json.loads(response.read())
episodes = data["results"]
for episode in episodes:
    print("Aflevering:", episode["episode"], " - Naam:", episode["name"], " - Uitzendingsdatum:", episode["air_date"])


character = input("Geef een Rick & Morty personage op: ")
url = "https://rickandmortyapi.com/api/character/?name=" + character
webbrowser.open(url)