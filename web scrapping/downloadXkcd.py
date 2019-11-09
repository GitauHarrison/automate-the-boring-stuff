#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, bs4, os

url = 'https://xkcd.com/'               # starting URL
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd
while not url.endswith('#'):
    # TO-DO: Download the page
    print('Downloading the page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TO-DO: Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            
            # TO-DO: Download the image
            print('Downloading the image %s ...' %(comicUrl))
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip the comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue


            # TO-DO: Save the image to ./Kxcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunck in res.iter_content(100000):
                imageFile.write(chunck)
            imageFile.close()


    # TO-DO: Get the PREV button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')