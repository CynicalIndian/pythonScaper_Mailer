import requests
import re
from bs4 import BeautifulSoup
import smtplib as mail

def check_price():
    URL = 'https://www.amazon.in/Sony-Slim-Console-Free-Game/dp/B07JM5GPQY/ref=sr_1_3?keywords=PS4&qid=1562568430&s=gateway&sr=8-3' #link of product

    headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    price = price.replace(" ","")
    price = price.replace(",","")

    con_price = float(price)
    print(title.strip())

    print(price)

    print(type(price))


    print(con_price)

    if(con_price<40000):
        mailer()

def mailer():
    server = mail.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your_email@gmail.com','some_password')  #Enter an email and a password obviously a temp password

    subject = "Price is down"
    body = "check out the price. https://www.amazon.in/Sony-Slim-Console-Free-Game/dp/B07JM5GPQY/ref=sr_1_3?keywords=PS4&qid=1562568430&s=gateway&sr=8-3"
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail('your_email@gmail.com','your_email@gmail.com',msg)  #To, from, message
    print("Email sent")
    server.quit()

def main():
    check_price()

main()
