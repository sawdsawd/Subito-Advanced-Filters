import requests
import re
import json
from bs4 import BeautifulSoup, Tag
from subitoPrompt import buildUrl

url = "https://www.subito.it/annunci-italia/vendita/usato/?q=tv%204k"

queries = dict()
database = "searches"

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
                queries[title] = {"title" : title, "price" : price, "location" : location, "link" : link}     
    
    print (queries)
    
    storeQueries()

runQuery('monitor 2k' , 0, 250)