import eel
from core.subitoSearch import runQuery
import json

eel.init('client')

@eel.expose
def search(query):
    runQuery(query, 0, 100)

eel.start('index.html')