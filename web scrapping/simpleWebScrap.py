#! python3

#TO-DO 1: Import all the necessary modules
import requests, bs4, time, webbrowser

# TO-DO 2: Download a html page using requests
req = requests.get('https://chezalab.netlify.com/')
req.raise_for_status()

#TO-DO 3: Parse through the html page using beautifulSoup
#req.text
#time.sleep(5)

soup = bs4.BeautifulSoup(req.text, 'html.parser')
#print(soup.prettify())
#time.sleep(5)

#TO-DO 4: Print relevant info on the terminal
print(soup.find_all('p')[3].get_text())

time.sleep(2)

print(soup.find_all(class_='feature-title')[0].get_text())
#TO-DO 5: Open links from the html page on new tabs using webbrowser 

time.sleep(2)

for link in soup.find_all('a'):
    #webbrowser.open_new_tab(link.get('href'))
    print(link.get('href'))

print(soup.get_text())