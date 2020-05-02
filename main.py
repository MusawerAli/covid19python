from plyer import notification
import requests
from bs4 import BeautifulSoup

import time
def notifyME(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "assets/icon.ico",
        timeout = 10

    )
def getData(url):
    r = requests.get(url)
    return r.text
if __name__ == '__main__':
    while True:
        # notifyME('COVID-19','Total Register Cases')
        myHtmlData = getData('http://www.ndma.gov.pk')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        # for table in soup.find_all('h4'):
        #     print(table.get('b'))
        myDataStr = ""
        for h4 in soup.find_all(attrs={"class": "panel-body text-left"})[1].find_all('h4'):
            myDataStr += h4.get_text()
        itemList = myDataStr.split('|')[1:]
        states = ['Punjab:','Sindh:','KP:','AJK:','Balochistan:','GB:']
        for item in itemList[0:4]:
            dataLists =   item.split()
            if dataLists[0] in states:
                for x in dataLists:
                    print(x)
                nTitle = "Cases of COVID-19 in Pakistan"
                nText = f"{dataLists}"
                print(nText)
                notifyME(nTitle,nText)
                time.sleep(2)
        time.sleep(3500)