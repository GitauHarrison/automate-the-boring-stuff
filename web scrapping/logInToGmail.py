#! python3

# logInToGmail.py - logs you into your GMAIL account,
# then log you out after a short while

#--------------------------
#SIGNING IN
#--------------------------
# TO-DO 1: Import all the needed modules
from selenium import webdriver
import time

# TO-DO 2: Choose the browser to use
browser = webdriver.Firefox()

# TO-DO 3: Create a URL link to GMAIL
browser.get('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=2ahUKEwjPyM2w_NzlAhXZad4KHenwBXcQFjACegQIARAB&url=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&usg=AOvVaw0XvudbS8_frp7iekcbIOHZ')

# TO-DO 4: Find the element to the email address
emailElem = browser.find_element_by_class_name('whsOnd')

# TO-DO 5: Fill in the email address
emailElem.send_keys('Your email')

# TO-DO 6: Click Next
emailNextButtonElem = browser.find_element_by_class_name('RveJvd')
emailNextButtonElem.click()

time.sleep(1.5)

# TO-DO 7: Find the element to the password box
passwordElem = browser.find_element_by_class_name('zHQkBf')

# TO-DO 8: Fill in the password
passwordElem.send_keys('Your password')

# TO-DO 9: Click Next
passwordNextElem = browser.find_element_by_class_name('CwaK9')

# passwordElem.find_element_by_link_text('Next')
passwordNextElem.click()

#--------------------------
#SIGNING OUT
#--------------------------

# TO-DO 10: Find the element to the user profile
userProfileELem = browser.find_element_by_class_name('gb_na')

# TO-DO 11: Click the user profile
userProfileELem.click()

# TO-DO 12: Find the element to the sign out text link

# TO-DO 13: Sign out
