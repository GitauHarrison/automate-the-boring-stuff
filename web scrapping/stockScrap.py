#! usr/bin/python3

# TO-DO 1:
#import all necessary libraries
import requests, bs4, webbrowser

# TO-DO 2: 
# Create a requests object to download a html page
stock = requests.get('https://www.bloomberg.com/quote/SPX:IND')
stock.raise_for_status() # checks for successful access

# TO-DO 3:
# Parse through the downloaded page using Beautiful soup
# Create a soup object
soup = bs4.BeautifulSoup(stock.text, 'html.parser')

# TO-DO 4: 
# Select relevant element from the page to get info
# print the name and price of the product on the terminal
elemName = soup.select('//*[@id="root"]/div/div/section[2]/div[1]/div[2]/section[1]/section/section[1]/div/h1')
print(elemName)

elemPrice = soup.find('span', attrs={'class': 'priceText__1853e8a5'})
print(elemPrice)







#import urllib3
#from bs4 import BeautifulSoup

# Specify the URL
#quote_page = 'https://www.bloomberg.com/quote/SPX:IND'

# Querry the website and return the html to the variable page
#page = urllib3.urlopen(quote_page)

# Parse the html using Beautiful Soup and create an object
#soup = BeautifulSoup(page, 'html.parser')

#name_box = soup.findall('section', attrs={'class': 'company_c1979f17'})
#name = name_box.text.strip()
#print (name)

#price_box = soup.findall('section', attrs={'class': 'priceText_1853e8a5'})
#price = price_box.text
#print (price)