from selenium.webdriver import Firefox
URL = 'https://web.whatsapp.com/'
browser = Firefox(executable_path='./geckodriver')
browser.get(URL)
input('Scan the QR code to make whatsapp web up and running, then press enter')
inputBox = browser.find_element_by_class_name('_2S1VP')
inputBox.send_keys('Surbhi')
contact = browser.find_elements_by_class_name('matched-text')
print(contact)