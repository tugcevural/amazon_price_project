import requests
import lxml
from bs4 import BeautifulSoup

url="https://www.amazon.com.tr/Philips-HD9650-90-Collection-Airfryer/dp/B0767DNSMH"
header= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
         "Accept-Language":"tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"}

response=requests.get(url, headers=header)

soup=BeautifulSoup(response.content,"lxml")
cost=soup.find(class_="a-offscreen")
cost_without_tl=cost.getText().split("TL")
cost_only=cost_without_tl[0]

a=cost_only.split(".")
print(a)
k=a[1].split(",")
print(k)
b=a[0]+k[0]+"."+ k[1]
print(b)

float_cost=float(b)
print(float_cost)

#---------------Sending cost alert-------------

import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE=3000

if float_cost < BUY_PRICE:
    message = f"{title} is now {cost}"

  with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )