import requests

r = requests.get('https://api.jikan.moe/v4/random/anime')
data = r.json()
print(data.keys())
print(f'Random anime {data["data"]["title"]}\nLink: {data["data"]["url"]}')