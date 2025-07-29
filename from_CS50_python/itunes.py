import json
import re
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()          #this function exits us from whole program

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
