import requests
from send_email import send_email

api_key = "a0860cae40a9404ca4315c8bf416c069"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2025-06-15&sortBy=publishedAt&apiKey="
       "a0860cae40a9404ca4315c8bf416c069")

# Make a request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

# Access the articles titles adn description
body = ""
for article in content['articles']:
    if article['title'] is not None or article['description'] is not None:
        title = article['title'] or ""
        description = article['description'] or ""
        body = body + title + "\n" + description + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)