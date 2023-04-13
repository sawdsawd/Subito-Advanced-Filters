import requests
import re
import json
from bs4 import BeautifulSoup, Tag
import os.path
from pathlib import Path

url = "https://www.subito.it/annunci-italia/vendita/usato/?q=tv%204k"

queries = []
database = "client\searches.json"

scheme = "https://"
baseUrl = "www.subito.it"

location = [
    "italia",
    "abruzzo",
    "basilicata",
    "calabria",
    "campania",
    "emilia-romagna",
    "friuli venezia giulia",
    "lazio",
    "liguria",
    "lombardia",
    "marche",
    "molise",
    "piemonte",
    "puglia",
    "sardegna",
    "sicilia",
    "toscana",
    "trentino alto adige",
    "umbria",
    "valle d'aosta",
    "veneto",
]

category = "/vendita/usato"

def buildUrl(q):
    query = "/?q=" + q

    return (scheme + baseUrl + "/annunci-" + "italia" + category + query)

def storeQueries():
    
    with open(database, "w") as file:
        file.write(json.dumps(queries, indent = 4))

def runQuery(name, minPrice, maxPrice):

    url = buildUrl(name)

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    product_list_items = soup.find_all("div", class_=re.compile(r"item-key-data"))

    for product in product_list_items:
        title = product.find("h2").string

        try:
            price = product.find("p", class_=re.compile(r"price")).contents[0]
            price_soup = BeautifulSoup(price, 'html.parser')
            if type(price_soup) == Tag:
                continue
            price = int(price.replace('.','')[:-2])
        except:
            price = "Unknown price"

        link = product.parent.parent.parent.parent.get('href')

        try:
            location = product.find('span',re.compile(r'town')).string + product.find('span',re.compile(r'city')).string
        except:
            print("Unknown location for item %s" % (title))
            location = "Unknown location"

        if minPrice == "null" or price == "Unknown price" or price >= int(minPrice):
            if maxPrice == "null" or price == "Unknown price" or price <= int(maxPrice):
                print("Not available")
            else:
                queries.append({"title" : title, "price" : price, "location" : location, "link" : link})    
        
    storeQueries()
