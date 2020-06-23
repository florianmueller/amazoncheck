# Python script for Amazon product availability checker

# importing libraries
from lxml import html
import requests
from time import sleep
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import http.client
import urllib
import json

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
browser = webdriver.Chrome('/Users/flo/Downloads/amazoncheck/webdrivers/chromedriver')
#raspbian
#browser = webdriver.Chrome('/usr/bin/chromedriver')
### END CONFIG ###

def check(url):
    browser.get(url)
    sleep(3)

    RAW_AVAILABILITY = browser.find_element_by_xpath('//*[@id="availability"]/span').text
    AVAILABILITY = ''.join(RAW_AVAILABILITY).strip() if RAW_AVAILABILITY else None
    return AVAILABILITY


def sendMail(ans, product, url, productname):
    recipient = receiverMailAdress
    body_of_email = url + ' -> ' + ans
    email_subject = product + ' product availability'

    # creates SMTP session
    s = smtplib.SMTP(mailSMTPserver, mailPort)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(mailUsername, mailPasswd)

    # message to be sent
    headers = "\r\n".join(["from: " + mailUsername,
                        "subject: " + email_subject,
                        "to: " + recipient,
                        "mime-version: 1.0",
                        "content-type: text/html"])

    content = headers + "\r\n\r\n" + body_of_email
    s.sendmail(mailUsername, recipient, content)
    s.quit()

    
# pushover
def sendPush(ans, product, url, productname):
    if pushoverToken :
        def pushover (sensordata_entity, pushover_title,pushover_priority):
            conn = http.client.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
              urllib.parse.urlencode({
                "token": pushoverToken,
                "user": pushoverUser,
                "device": pushoverDevice,
                "title": pushover_title,
                "url": url,
                "message": pushover_message,
                "priority": pushover_priority,
                "sound": "intermission",
              }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()
        pushover_message = ans
        pushover_priority = 1
        pushover_title = "Amazon: " + productname
        pushover(pushover_message, pushover_title, pushover_priority)


def ReadAsin(Asin, productname, url):
#    print ("Processing: "+url)
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
    print(productname +'-'+ Asin +'-'+ ans, end ="-")
    if ans in arr:
        print('green')
        #in case product available
        #notify user with mail and push
        sendMail(ans, Asin, url, productname)
        #send pushover
        sendPush(ans, Asin, url, productname)
    else:
        print('red')


# LOAD CONFIG FILE & RUN FOR EACH ITEM
with open('./amazon-items.json') as data_file:
    data = json.load(data_file)
    for i in data['products']:
        #DEBUG log if items parsed
    # Asin Id is the product Id which
    # needs to be provided by the user in items.json
        Asin = i['id']
        productname = i['name']
        url = "http://www.amazon.de/dp/" + Asin
        ReadAsin(Asin, productname, url)
