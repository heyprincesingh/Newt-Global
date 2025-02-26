import os
import requests  # type: ignore
from send_email import send_email

topic = "tesla"

api_key = os.getenv("NEWS_API_KEY")
url = (
    f"https://newsapi.org/v2/everything?"
    + f"q={topic}"
    + "&sortBy=publishedAt"
    + f"&apiKey={api_key}"
    + "&language=en"
)

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = "Subject: Today's news"
        + "\n" + body + article["title"] + "\n" 
        + article["description"] 
        + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(user_email="princsingh3632@gmail.com", message=body)
