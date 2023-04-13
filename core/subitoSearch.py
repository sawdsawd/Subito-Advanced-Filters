import requests
import re
import json
from bs4 import BeautifulSoup, Tag
import os.path
from pathlib import Path

queries = []
database = "searches.json"

scheme = "https://"
baseUrl = "www.subito.it"

#SAVE QUERIES TO JSON
def storeQueries():
    
    with open(database, "w") as file:
        file.write(json.dumps(queries, indent = 4))

# URL BUILDER

location = ["italia", "abruzzo", "basilicata", "calabria", "campania", "emilia-romagna", 
            "friuli venezia giulia", "lazio", "liguria", "lombardia", "marche", "molise",
            "piemonte", "puglia", "sardegna","sicilia", "toscana", "trentino alto adige",
            "umbria", "valle d'aosta", "veneto",
]

category = "/vendita/usato"

def buildUrl(q, pageNum):

    q = q.replace(" ", "+")
    query = "/?q=" + q

    return (scheme + baseUrl + "/annunci-" + location[0] + category + query + "&o=" + str(pageNum))

#RUN A SINGLE QUERY
def scanPage(url, minPrice, maxPrice):

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

        if minPrice == "null" or price == "Unknown price" or price >= int(maxPrice) or maxPrice == "null" or price <= int(minPrice):
            print("Not available")
        else:
            queries.append({"title" : title, "price" : price, "location" : location, "link" : link})    
        
    storeQueries()



def search(query, numOfPages, minPrice, maxPrice):
    urls = []

    for num in range(1, numOfPages + 1):
        urls.append(buildUrl(query, num))
    
    for url in urls:
        scanPage(url, minPrice, maxPrice)

    

search("iphone 14", 2, 0, 1800)