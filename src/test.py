import requests
from pprint import pprint

base_url="https://api.worldbank.org/v2/country/"
country="NGA"
page=1
indicator="NY.GDP.PCAP.CD"
url = f"{base_url}{country}/indicator/{indicator}?format=json&page={page}&per_page=50"
print(url)

response = requests.get(url)
json_data = response.json()[1]
for i in json_data:
     print(i["country"]["value"])