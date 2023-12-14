import urllib.request
import json
import webbrowser

response = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
if response.getcode() == 200:
    output = json.loads(response.read())
    print(output)

url = output['message']

webbrowser.open(url)

i = 0
while i < 5:
    response = urllib.request.urlopen("https://dog.ceo/api/breed/puggle/images/random/5")    
    output = json.loads(response.read())
    url = output['message'][i]
    webbrowser.open(url)
    i += 1