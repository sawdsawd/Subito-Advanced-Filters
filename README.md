# Advanced Search Filters for Subito.it

Advanced Search Filters for Subito.it is a web scraper for the popular italian ads website.

Features:
* Automatic URL builder for your query
* Price filters
* Location filters (only by region)
* Modern web GUI
* Multiplatform: runs anywhere python can run

## Setup

You will need Python to run this app

### Install Dependencies

```pip3 install -r requirements.txt```

## Usage

The easiest way is to run the .bat file for Windows.
If you are on another OS you can directly call ```python main.py```.

It will open the web GUI on ```http://localhost:8000/index.html``` using your default browser.
If you have any problem using the GUI please try using another browser.

To close the app just close the system console.

The results of the last query will be saved in ```searches.json```, if you need the raw results you can find them there and maybe use another software to filter them based on your needs.

## How it works

When you run a query it first builds the correct url based on your filters, it then uses BeautifulSoup to scrape the results and saves them in ```searches.json```.
Python Eel builds the web GUI and looks at  ```searches.json``` to show the results

### Tecnologies:
* BeautifulSoup
* Python Eel

## Credits

I started from morrolinux's repo and went with a different different approach which is more user-friendly and does not require any particular "skill" in using a computer. I achieved this by creating a function that dynamically generates the url for your query and including price and location filters. I do not include any notification service as it pretty useless unless you are searching for a very specific item that is not put on sale often.

* https://github.com/morrolinux/subito-it-searcher/