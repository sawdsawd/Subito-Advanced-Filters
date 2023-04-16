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
            "umbria", "valle d'aosta", "veneto",
]

category = "/vendita/usato"

def buildUrl(q, pageNum, region, boolNear):

    q = q.replace(" ", "+")
    query = "/?q=" + q
    
    if boolNear:
        return (scheme + baseUrl + "/annunci-" + region + "-vicino" + category + query + "&o=" + str(pageNum))

    return (scheme + baseUrl + "/annunci-" + region + category + query + "&o=" + str(pageNum))

def filterByPrice(min, max):
    
    if(min is None):
        print("No minPrice")
    elif(min is not None):
        for product in queries:
            if(str(product.get("price")) == "Unknown price"):
                print("removing: ", product.get("title"), "unknown")
                queries.remove(product)
            elif(min > (product.get("price"))):
                print("removing: ", product.get("title"), product.get("price"))
                queries.remove(product)
                
    if(max is None):
        print("No maxPrice")
    elif(max is not None):
        for product in queries:
            print("not relevant")
            # if(max < int(product.get("price"))):
            #     queries.pop(product)

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
            
        if (price == "Unknown price" and (minPrice or maxPrice)):
            print("removing: ", title)
        elif minPrice is not None and maxPrice is not None:
            if((int(price) < maxPrice and int(price) > minPrice)):
                queries.append({"title" : title, "price" : price, "location" : location, "link" : link})
        elif minPrice is not None and maxPrice is None:  
            if(int(price) > minPrice):
                queries.append({"title" : title, "price" : price, "location" : location, "link" : link})
        elif maxPrice is not None and minPrice is None:
            if(int(price) < (maxPrice)):
                queries.append({"title" : title, "price" : price, "location" : location, "link" : link})
        else:
            queries.append({"title" : title, "price" : price, "location" : location, "link" : link})
        
    storeQueries()



def search(query, numOfPages, region, minPrice, maxPrice):
    urls = []
    boolVicino = False #To implement
    
    resetQueries()

    for num in range(0, numOfPages):
        urls.append(buildUrl(query, num, region, boolVicino))
    
    for url in urls:
        scanPage(url, minPrice, maxPrice)
  
 
 
 
 
 
   

def getProvince(region):
    siglaProvinceRegione = []
    
    with open('core\province-italia.json') as data:
        provinceItalia = json.load(data)   
    
    for item in provinceItalia:
        if(item.get("regione") == region):
            siglaProvinceRegione.append(item.get("sigla"))
    
    return siglaProvinceRegione
    

def filterByProvince(province, region):
    provinceRegione = getProvince(region)
