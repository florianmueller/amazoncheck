# Python script for Amazon product availability checker
# importing libraries
from lxml import html
import requests
from time import sleep
import smtplib
from selenium import webdriver
import http.client
import urllib
import json
from pyvirtualdisplay import Display

### START CONFIG ###
receiver_email_id = "YOURDESIREDMAIL@mail.com"
pushoverToken = ''
pushoverUser = ''
pushoverDevice = ''
mailUsername = ''
mailPasswd = ''
mailSMTPserver = 'smtp.gmail.com'
mailPort = 587
#CHROME WEBDRIVER LOCATION, on MAC OR WIN OR LINUX DIFFERENTLY
#mac
#browser = webdriver.Chrome('/Users/yourusername/Downloads/chromedriver')
#raspbian
#browser = webdriver.Chrome('/usr/bin/chromedriver')
### END CONFIG ###



def check(url):
    with Display():
        # we can now start Firefox and it will run inside the virtual display
#        browser = webdriver.Firefox(executable_path='/home/pi/amazoncheck/webdrivers/geckodriver')
        browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        # put the rest of our selenium code in a try/finally
        # to make sure we always clean up at the end
        try:
    #        browser.get('http://www.google.com')
    #        print(browser.title) #this should print "Google"
            browser.get(url)
            sleep(3)

            RAW_AVAILABILITY = browser.find_element_by_xpath('//*[@id="availability"]/span').text
            AVAILABILITY = ''.join(RAW_AVAILABILITY).strip() if RAW_AVAILABILITY else None
            return AVAILABILITY

        finally:
            browser.quit()





#def check(url):
#    browser.get(url)
#    sleep(3)
#
#    RAW_AVAILABILITY = browser.find_element_by_xpath('//*[@id="availability"]/span').text
#    AVAILABILITY = ''.join(RAW_AVAILABILITY).strip() if RAW_AVAILABILITY else None
#    return AVAILABILITY


def sendMail(ans, product):
    GMAIL_USERNAME = "YOUR_GMAIL_ID"
    GMAIL_PASSWORD = "YOUR_GMAIL_PASSWORD"

    recipient = receiver_email_id
    body_of_email = ans
    email_subject = product + ' product availability'

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    # message to be sent
    headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                        "subject: " + email_subject,
                        "to: " + recipient,
                        "mime-version: 1.0",
                        "content-type: text/html"])

    content = headers + "\r\n\r\n" + body_of_email
    s.sendmail(GMAIL_USERNAME, recipient, content)
    s.quit()

# pushover
def sendPush(ans, product):
    if pushoverToken :
        def pushover (sensordata_entity, pushover_title,pushover_priority):
            conn = http.client.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
              urllib.parse.urlencode({
                "token": pushoverToken,
                "user": pushoverUser,
                "device": pushoverDevice,
                "title": pushover_title,
                "message": pushover_message,
                "priority": pushover_priority,
                "sound": "intermission",
              }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()
        pushover_message = ans
        pushover_priority = 0
        pushover_title = "Amazon: " + productname
        pushover(pushover_message, pushover_title, pushover_priority)


def ReadAsin():
    print ("Processing: "+url)
    ans = check(url)
    #debug
    #print (AVAILABILITY)
    arr = [
        'Nur noch 1 auf Lager',
        'Nur noch 1 auf Lager.',
        'Nur noch 2 auf Lager',
        'Nur noch 2 auf Lager.',
        'Nur noch 3 auf Lager',
        'Nur noch 3 auf Lager.',
        'Nur noch 4 auf Lager',
        'Nur noch 4 auf Lager.',
        'Nur noch 5 auf Lager',
        'Nur noch 5 auf Lager.',
        'Nur noch 6 auf Lager',
        'Nur noch 6 auf Lager.',
        'Nur noch 7 auf Lager',
        'Nur noch 7 auf Lager.',
        'Nur noch 8 auf Lager',
        'Nur noch 8 auf Lager.',
        'Nur noch 9 auf Lager',
        'Nur noch 9 auf Lager.',
        'Nur noch 10 auf Lager',
        'Nur noch 10 auf Lager.',
        'Nur noch 11 auf Lager',
        'Nur noch 11 auf Lager.',
        'Nur noch 12 auf Lager',
        'Nur noch 12 auf Lager.',
        'Nur noch 13 auf Lager',
        'Nur noch 13 auf Lager.',
        'Nur noch 14 auf Lager',
        'Nur noch 14 auf Lager.',
        'Nur noch 15 auf Lager',
        'Nur noch 15 auf Lager.',
        'Nur noch 16 auf Lager',
        'Nur noch 16 auf Lager.',
        'Nur noch 17 auf Lager',
        'Nur noch 17 auf Lager.',
        'Nur noch 18 auf Lager',
        'Nur noch 18 auf Lager.',
        'Nur noch 19 auf Lager',
        'Nur noch 19 auf Lager.',
        'Nur noch 20 auf Lager',
        'Nur noch 20 auf Lager.',
        'Auf Lager',
        'Auf Lager.',
        'In stock.']
    print(ans)
    if ans in arr:
        #in case product available
        #notify user with mail and push
#        sendMail(ans, Asin)
        #send pushover
        sendPush(ans, Asin)



# LOAD CONFIG FILE & RUN FOR EACH ITEM
with open('amazon-items.json') as data_file:
    data = json.load(data_file)
    for i in data['products']:
        #DEBUG log if items parsed
        print (i['name'])
        print (i['id'])
    # Asin Id is the product Id which
    # needs to be provided by the user in items.json
        Asin = i['id']
        productname = i['name']
        url = "http://www.amazon.de/dp/" + Asin
        ReadAsin()
