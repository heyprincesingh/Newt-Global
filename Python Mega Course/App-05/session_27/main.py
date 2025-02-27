import os
import requests # type: ignore
from send_email import send_email

api_key = os.getenv("NEWS_API_KEY")
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-01&sortBy=publishedAt&apiKey=" + api_key

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body += article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(user_email="princsingh3632@gmail.com", message=body)