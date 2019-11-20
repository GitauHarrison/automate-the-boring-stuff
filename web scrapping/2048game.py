#! python3

# 2048game.py - automate the playing of the classic game 2048

# TO-DO 1: Choose the desired browser 
# TO-DO 2: Open and maximise the browser with the link https://play2048.co/
# TO-DO 3: Simulate the key presses to move the tiles
# TO-DO 4:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

browser = webdriver.Chrome()
browser.get('https://play2048.co/')
browser.maximize_window()

# Keys
moves = [Keys.LEFT, Keys.RIGHT, Keys.UP, Keys.DOWN]
while True:
    bodyElem = browser.find_element_by_tag_name('body')
    bodyElem.send_keys(random.choice(moves))

