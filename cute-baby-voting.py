import time
from selenium.webdriver import Chrome
#Write the URL here
URL = 'https://mycutebaby.in/contest/participant/?n=5ebe684e8e100'
#Write your name here
NAME = 'Mohit Ranjan'
while(1):
    #Open URL
    browser = Chrome(executable_path='./chromedriver')
    browser.get(URL)
    #Fill Info
    nameInput = browser.find_element_by_id('v')
    voteButton = browser.find_element_by_id('vote_btn')
    time.sleep(10)
    #Press button to vote
    nameInput.send_keys(NAME)
    voteButton.click()
    #sleep for 30 minutes
    time.sleep(30*60)
    #close the browser and restart
    browser.close()

