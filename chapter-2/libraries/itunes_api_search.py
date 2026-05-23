import requests
import sys
import json


if len(sys.argv) != 2:
    sys.exit("Usage: python itunes_api_search.py artist_name")


response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term="
    + sys.argv[1]
)

print(json.dumps(response.json(), indent=2))


data = response.json()

for result in data["results"]:
    print(result["trackName"])
