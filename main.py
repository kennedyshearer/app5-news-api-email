import requests
import time
from send_email import send_email

date = time.strftime("%Y-%m-%d")
topic = "tesla"

api_key = "{API-KEY-HERE}"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       f"from={date}&sortBy=publishedAt&apiKey=" \
       "a0860cae40a9404ca4315c8bf416c069&" \
       "language=en"

# Make a request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

# Access the articles titles adn description
body = ""
for article in content['articles'][:20]:
    if article['title'] is not None or article['description'] is not None:
        title = article['title'] or ""
        description = article['description'] or ""
        url_link = article['url'] or ""
        body = "Subject: Today's news" \
               + "\n" + body + title \
               + "\n" + description \
               + "\n" + url_link + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)
