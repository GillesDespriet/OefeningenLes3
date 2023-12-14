#Github ApI
import urllib.request
import json

response = urllib.request.urlopen("https://api.github.com/users/GillesDespriet/repos")
repos = json.loads(response.read())
for repo in repos:
    print(repo["html_url"])


response = urllib.request.urlopen("https://api.github.com/repos/GillesDespriet/OefeningenLes3/commits")
repos = json.loads(response.read())
for repo in repos:
    print("Author:",repo["commit"]["author"]["name"], "- Message:", repo["commit"]["message"])
        



response = urllib.request.urlopen("https://api.github.com/search/repositories?q=language:csharp")
data = json.loads(response.read())
repos = data["items"]
for repo in repos:
   print("repo:", repo["html_url"])
    