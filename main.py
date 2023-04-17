import eel
from core.subitoSearch import search
import json

eel.init('client')

@eel.expose
def newSearch(query, numOfPages, region, minPrice, maxPrice, boolNear):
    search(query, numOfPages, region, minPrice, maxPrice, boolNear)

eel.start('index.html', mode='default')