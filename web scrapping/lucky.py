#! /usr/bin/env python3
# lucky.py - opens severals Google search results.

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=gitauharrison' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#retrieve top search results links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Open a browser tab for each result
linkElems = soup.select('a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    