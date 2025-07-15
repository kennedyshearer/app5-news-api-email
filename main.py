import requests

api_key = "a0860cae40a9404ca4315c8bf416c069"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2025-06-15&sortBy=publishedAt&apiKey="
       "a0860cae40a9404ca4315c8bf416c069")

# Make a request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

# Access the articles titles adn description
for article in content['articles']:
    print(article['title'])
    print(article['description'])