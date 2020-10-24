import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

def linker(aspect):
    url = f"https://2e.aonprd.com/{aspect}.aspx"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        if f"{aspect}.aspx?ID" in link.get('href'):
            links.append(link.text)
    return links

def classes():
    return linker("Classes")


def ancestries():
    doub_ancs =  linker("Ancestries")
    def filterAncs(link):
        return not("Click here" in link)
    ancs = list(filter(filterAncs, doub_ancs))
    return ancs

def backgrounds():
    return linker("Backgrounds")

# def classes():
#     clas = ["Alchemist", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Wizard"]
#     return clas