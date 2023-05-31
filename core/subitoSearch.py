import requests
import re
import json
from bs4 import BeautifulSoup, Tag
import os
from pathlib import Path

queries = []
database = "client\searches.json"

scheme = "https://"
baseUrl = "www.subito.it"

#SAVE QUERIES TO JSON
def storeQueries():
    with open(database, "w") as file:
        file.write(json.dumps(queries, indent = 4))

#RESET SEARCHES.JSON
def resetQueries():
    queries.clear()
    open(database, "w").close()

# URL BUILDER
regions = ["italia", "abruzzo", "basilicata", "calabria", "campania", "emilia-romagna", 
            "friuli venezia giulia", "lazio", "liguria", "lombardia", "marche", "molise",
            "piemonte", "puglia", "sardegna","sicilia", "toscana", "trentino alto adige",
            "umbria", "valle d'aosta", "veneto",]

category = "/vendita/usato"

def buildUrl(q, pageNum, region, boolNear):

    q = q.replace(" ", "+")
    query = "/?q=" + q
    
    if boolNear:
        return (scheme + baseUrl + "/annunci-" + region + "-vicino" + category + query + "&o=" + str(pageNum))

    return (scheme + baseUrl + "/annunci-" + region + category + query + "&o=" + str(pageNum))

#RUN A SINGLE QUERY
def scanPage(url, minPrice, maxPrice):
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    product_list_items = soup.find_all("div", class_=re.compile(r"picture-group"))

    for product in product_list_items:
        title = product.find("div", class_=re.compile(r"item-key-data")).find("h2").string

        imgSrc = product.find("div", class_=re.compile(r"item-picture")).find("img")["src"]

        try:
            price = product.find("div", class_=re.compile(r"item-key-data")).find("p", class_=re.compile(r"price")).contents[0]
            price_soup = BeautifulSoup(price, 'html.parser')
            if type(price_soup) == Tag:
                continue
            price = int(price.replace('.','')[:-2])
        except:
            price = "Unknown price"

        link = product.parent.parent.get('href')

        try:
            location = product.find("div", class_=re.compile(r"item-key-data")).find('span',re.compile(r'town')).string + product.find('span',re.compile(r'city')).string
        except:
            print("Unknown location for item %s" % (title))
            location = "Unknown location"

        if price == "Unknown price" and (minPrice or maxPrice):
            print("removing:", title)
        elif (minPrice is None or int(price) > minPrice) and (maxPrice is None or int(price) < maxPrice):
            queries.append({"title": title, "imgSrc": imgSrc, "price": price, "location": location, "link": link})

    storeQueries()


#START NEW SEARCH
def search(query, numOfPages, region, minPrice, maxPrice, boolNear = False):
    urls = []
    
    resetQueries()

    if(region == regions[0]):
        boolNear = False

    for num in range(1, numOfPages + 1):
        urls.append(buildUrl(query, num, region, boolNear))
    
    for url in urls:
        scanPage(url, minPrice, maxPrice)

