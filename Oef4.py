#Github ApI
import urllib.request
import json

response = urllib.request.urlopen("https://api.github.com/users/GillesDespriet/repos")
if response.getcode() == 200:
    repos = json.loads(response.read())
    for repo in repos:
        print(repo["html_url"])
else:
    print(f"Error: {response.status_code}")


response = urllib.request.urlopen("https://api.github.com/repos/GillesDespriet/OefeningenLes3/commits")
if response.getcode() == 200:
    repos = json.loads(response.read())
    for repo in repos:
        print("Author:",repo["commit"]["author"]["name"], "- Message:", repo["commit"]["message"])
        
else:
    print(f"Error: {response.status_code}")


response = urllib.request.urlopen("https://api.github.com/search/repositories?q=language:csharp")
if response.getcode() == 200:
    data = json.loads(response.read())
    repos = data["items"]
    for repo in repos:
        print("repo:", repo["html_url"])
        
else:
    print(f"Error: {response.status_code}")