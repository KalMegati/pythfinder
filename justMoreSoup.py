import requests
from bs4 import BeautifulSoup


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "https://2e.aonprd.com/Classes.aspx"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
classes = []
for link in soup.find_all('a'):
    if "Classes.aspx?ID" in link.get('href'):
        classes.append(link.text)

print(classes)