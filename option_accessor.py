import requests
from bs4 import BeautifulSoup

import options

classes = options.classes()


for id, clas in enumerate(classes.keys()): 
    print (f'{id+1}) {clas}')

choice = input("select a number \n")

op_link = classes[list(classes.keys())[int(choice)-1]]

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

def summarizer(link):
    url = f"https://2e.aonprd.com/{link}"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup.find_all("i")[1].text

print(summarizer(op_link))