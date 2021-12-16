import  requests
from bs4 import  BeautifulSoup
import smtplib
from twilio.rest import  Client

ac_sid ="ACdb5d2da54a1d92edafe3543b8497d46a"
ac_token ="40af5c3e3b5bdfc3841298b305ce382e"

url = "https://www.flipkart.com/hp-pavilion-gaming-ryzen-5-hexa-core-4600h-8-gb-1-tb-hdd-windows-10-home-4-gb-graphics-nvidia-geforce-gtx-1650-15-ec1021ax-laptop/p/itm70c8fb9efbb8c?pid=COMFT8GXGSJZKAAE&lid=LSTCOMFT8GXGSJZKAAEFE91VM&marketplace=FLIPKART&q=hp+gaming+laptop&store=search.flipkart.com&srno=s_1_13&otracker=search&otracker1=search&fm=SEARCH&iid=5b7012e1-42e0-4ae2-9083-6df942f8c632.COMFT8GXGSJZKAAE.SEARCH&ppt=browse&ppn=browse&ssid=tahm3awdio0000001639578880296&qH=ea0dc41f5c63c439"
#url = "https://www.amazon.in/HP-Pavilion-15-6-inch-5-4600H-15-ec1021AX/dp/B08CZ2VRSL/ref=asc_df_B08CZ2VRSL/?tag=googleshopdes-21&linkCode=df0&hvadid=544956768920&hvpos=&hvnetw=g&hvrand=8946251908355809223&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9300728&hvtargid=pla-1426856267741&psc=1"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

def scraper():
    page = requests.get(url, headers=headers)
    bs = BeautifulSoup(page.content, 'html.parser')

    # print(bs.prettify())
    #prodtitle = bs.find(id="productTitle").get_text().strip()
    #print(prodtitle)
    #prodprice = bs.find(class_='a-offscreen').get_text().strip()
    prodprice = bs.find(class_='_30jeq3 _16Jk6d').get_text().strip()
    #print(prodprice)
    prodprice = prodprice[1:]
    price_numeric = float(prodprice.replace(",", ""))
    print(price_numeric)
    return price_numeric


def sendemail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('extrafarziemail@gmail.com','xoctuwurxkvxcfow')
    subject ="Price Check"
    body =f"price slashed\n check: {url}"
    message =f"Subject:{subject}\n\n\n {body}"
    server.sendmail('extrafarziemail@gmail.com','vschs007@gmail.com',message)
    print("email sent")
    server.quit()

def sendmessage():
    client = Client(ac_sid, ac_token)
    body =f"{url}"
    client.messages.create(body=f" hi prices are now down visit\n ,{body} ", from_='+12185177591', to='+917054015768 ')
    print("message sent")

getprice = scraper()
if(getprice<58000):
    sendemail()
    #sendmessage()

