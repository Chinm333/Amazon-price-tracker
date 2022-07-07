from bs4 import BeautifulSoup
import requests
import smtplib

EMAIL = "teessssssst1@gmail.com"
PASSWORD = 7002340553

response = requests.get(
    url="https://www.amazon.in/New-Apple-iPhone-Pro-256GB/dp/B08L5T31M6/ref=sr_1_1_sspa?crid=2TEA69VZUB64&dchild=1&keywords=iphone%2B12%2Bpro%2Bmax&qid=1628832186&sprefix=iphone%2Caps%2C572&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFXQTlVNEUxNTI1N0wmZW5jcnlwdGVkSWQ9QTA3MTA0MzQxQkpKOVpLMTZSVUtaJmVuY3J5cHRlZEFkSWQ9QTAyNjcxODEzSERPRFo1OVdENklEJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})

print(response)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
price_wo_symbol = price.split("₹")[1]
price_wo_comma = price_wo_symbol.replace(",", "")
price_wo_symbol_float = float(price_wo_comma)

if price_wo_symbol_float <= 100000.00:

    with smtplib.SMTP("smtp.gmail.com") as price_tracker:
        price_tracker.starttls()
        price_tracker.login(user=EMAIL, password=PASSWORD)
        price_tracker.sendmail(from_addr=EMAIL,
                               to_addrs="chinm3333@gmail.com",
                               msg=f"Offer\nOffer\n{price_wo_symbol_float} is the price of 'New Apple iPhone 12 Pro Max (256GB)'\n.Link of the product-https://www.amazon.in/New-Apple-iPhone-Pro-256GB/dp/B08L5T31M6/ref=sr_1_1_sspa?crid=2TEA69VZUB64&dchild=1&keywords=iphone%2B12%2Bpro%2Bmax&qid=1628832186&sprefix=iphone%2Caps%2C572&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFXQTlVNEUxNTI1N0wmZW5jcnlwdGVkSWQ9QTA3MTA0MzQxQkpKOVpLMTZSVUtaJmVuY3J5cHRlZEFkSWQ9QTAyNjcxODEzSERPRFo1OVdENklEJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1")
