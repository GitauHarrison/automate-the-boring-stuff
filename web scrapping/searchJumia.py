#! usr/bin/python3

#TO-DO 1:
# Create a requests object
# Check whether the request was successful
import requests, bs4, webbrowser, sys

res = requests.get('https://www.jumia.co.ke/catalog/?q=mi+a2'+ ' '.join(sys.argv[1:]))
res.raise_for_status()

#TO-DO 2:
# Parse through the html page using beautiful soup
# Create a beautiful soup object to work with
# select the links with intended searches
resSoup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElem = resSoup.select('.osh-subcategory a')
numTabs = min(6, len(linkElem))


#TO-DO 3:
# Open the links on the browser
# Each link on its own tab
for tabs in range(numTabs):
    webbrowser.open('https://www.jumia.co.ke/' + linkElem[tabs].get('href'))