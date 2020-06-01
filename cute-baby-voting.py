import time
from selenium.webdriver import Chrome
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

#Write the URL here
URL = 'https://mycutebaby.in/contest/participant/?n=5ebe684e8e100'
#Write your name here
NAME = 'Mohit Ranjan'
count = 0
while(1):
    #Open URL
    browser = Chrome(executable_path='./chromedriver')
    browser.get(URL)
    #Fill Info
    nameInput = browser.find_element_by_id('v')
    voteButton = browser.find_element_by_id('vote_btn')
    #Allow page to load completely. This delay should be adjusted as per your internet speed.
    print('Page load hone dete hai')
    countdown(10)
    #Press button to vote
    nameInput.send_keys(NAME)
    # voteButton.click()
    count = count + 1
    print(str(count) + ' vote done')
    #sleep for 30 minutes
    print('Sleeping for 30 minutes now...')
    countdown(30*60)
    #close the browser and restart
    print('Chaliye shuru krte hai :)')
    browser.close()

