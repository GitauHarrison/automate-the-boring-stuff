#! python3
# logins.py - logs user to accounts on multiple tabs using selenium

# TO-DO 1: Log into GMAIL in the default tab

# TO-Do 2: Open a new tab

# TO-DO 3: Switch to the new tab

# TO-DO 4: Log into Slack

# TO-DO 5: Open a new tab

# TO-DO 6: Switch to the new tab

# TO-DO 7: Log into trello


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime
from time import ctime 


browser = webdriver.Chrome()
browser.maximize_window()

#--------------------
# SIGN IN
#--------------------

       
            # TAB 1: GMAIL
           
def gmailLogin():
    # Sign In
    browser.get('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=2ahUKEwjPyM2w_NzlAhXZad4KHenwBXcQFjACegQIARAB&url=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&usg=AOvVaw0XvudbS8_frp7iekcbIOHZ')
    emailElem = browser.find_element_by_class_name('whsOnd')
    emailElem.clear()
    emailElem.send_keys('harrison@tinkeredu.net')
    emailNextButtonElem = browser.find_element_by_class_name('RveJvd')
    emailNextButtonElem.click()
    time.sleep(1.5)
    passwordElem = browser.find_element_by_class_name('zHQkBf')
    passwordElem.clear()
    passwordElem.send_keys('S!mps0n@24..,,')
    passwordNextElem = browser.find_element_by_class_name('CwaK9')
    passwordNextElem.click()
    time.sleep(3)
    browser.save_screenshot('gmail.png')

                   
                    # TAB 2: SLACK
                   
def slackLogin():
    browser.get('https://tinkeredu.slack.com')
    slackEmailElem = browser.find_element_by_id('email')
    slackEmailElem.clear()
    time.sleep(1.5)
    slackEmailElem.send_keys('harrison@tinkeredu.net')
    slackPasswordElem = browser.find_element_by_id('password')
    slackPasswordElem.clear()
    slackPasswordElem.send_keys('Turf2013W!n..')
    signInElem = browser.find_element_by_id('signin_btn').submit()
    time.sleep(5)
    browser.save_screenshot('slacksignin.png')

    # Post my commute time
    commuteTimeElem= browser.find_element_by_link_text('commute-time-record')
    commuteTimeElem.click()
    commuteTimeElem.clear
    #commute = print(ctime)
    commuteTimeElem.send_keys(str(ctime))
    time.sleep(1.5)
    commuteTimeElem.send_keys(Keys.ENTER)





              
                # TAB 2: TRELLO
             
def trelloLogin():
    browser.get('https://trello.com/login')
    loginWithGmailElem = browser.find_element_by_id('google-link')
    loginWithGmailElem.click()
    time.sleep(5)
    browser.save_screenshot('trellologin.png')

#gmailLogin()

#------Switching tabs to slack--------

browser.execute_script("window.open('');")
browser.switch_to_window(browser.window_handles[1])
time.sleep(1.5)

slackLogin()

#------Switching tabs trello--------

browser.execute_script("window.open('');")
browser.switch_to_window(browser.window_handles[2])
time.sleep(1.5)

#trelloLogin()

#---------------------------------
#DURATION TO BEGIN LOGGING OUT  
#---------------------------------
#startOfDay = ctime()
#endOfDay = ctime()



#--------------------
# SIGN OUT
#--------------------

def gmailLogOut():
    userProfileElem = browser.find_element_by_class_name('gb_Ha')
    userProfileElem.click()
    signoutElem = browser.find_element_by_id('gb_71')
    signoutElem.click()

def slackLogOut():
    pass


def trelloLogOut():
    pass




#------ Switching through the tabs --------
for tabs in range(3):
    browser.switch_to_window(browser.window_handles[tabs])
    time.sleep(1.5)
    if browser.switch_to_window(browser.window_handles[tabs]) == browser.switch_to_window(browser.window_handles[0]):
        gmailLogOut()
        time.sleep(1.5)
        browser.close()
    elif browser.switch_to_window(browser.window_handles[tabs]) == browser.switch_to_window(browser.window_handles[1]):
        slackLogOut()
        time.sleep(1.5)
        browser.close()
    else:
        trelloLogOut()
        time.sleep(1.5)
        browser.close()

