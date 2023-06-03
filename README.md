# Advanced Search Filters for Subito.it

![SubitoAdvancedFilters](https://github.com/sawdsawd/Subito-Advanced-Fitlers/assets/92443986/7f9137aa-b7ca-400a-a12c-6269587d0957)

Advanced Search Filters for Subito.it is a web scraper for the popular italian ads website.

Features:
* Automatic URL builder for your query
* Multi-page search
* Price filters
* Location filters (only by region)
* Modern web GUI
* Multiplatform: runs anywhere python can run

## Setup

### Requirements

The app requires Python to run

### Install Dependencies

```pip3 install -r requirements.txt```

### Launch

If you are on Windows, you can simply launch the app via ```run.bat```.
On any other OS you can open your console, navigate to the folder of the app and type ```python main.py```.

## Usage

Once the program loads, it will open the web GUI on ```http://localhost:8000/index.html``` using your default browser.
If you have any problem using the GUI please try using another browser.

To close the app just close the system console.

The app lets you scan multiple pages at once, a very useful feature, please use it carefully as it may take too much time or could get the site to think you are a bot. I reccomend using maximum 50 pages, ideally less then 20 per search.

The results of your last query will be saved in ```searches.json```, inside the client folder.
If you need the raw outputs, you can find them there and maybe use another software to filter them based on your needs.

## How it works

When you run a query it first builds the correct url based on your filters, it then uses BeautifulSoup to scrape the results and saves them in ```searches.json```.
Python Eel builds the web GUI and looks at  ```searches.json``` to show the results

### Tecnologies:
* BeautifulSoup
* Python Eel

## Credits

I started from morrolinux's repo and went with a different different approach which is more intuitive and user-friendly, just a simple GUI instead of typing in the console. I achieved this by creating a function that dynamically generates the url for your query, it then checks the results based on the filters you apply, either price or location. I do not include any notification service as it pretty useless unless you are searching for a very specific item that is not put on sale often.

* https://github.com/morrolinux/subito-it-searcher/
