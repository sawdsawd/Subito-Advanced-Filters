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