import requests
import datetime as dt
from twilio.rest import Client

STOCK = ""
COMPANY_NAME = ""
NEWS_API_KEY = ""
STOCK_API_KEY = ""

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY,
}

news_parameters = {
    "q":COMPANY_NAME,
    "language":"en",
    "sortby":"publishedAt",
    "apikey":NEWS_API_KEY,
}

news_response = requests.get("https://newsapi.org/v2/everything", params = news_parameters)
news_response.raise_for_status()
stock_response = requests.get("https://www.alphavantage.co/query", params = stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
yesterday_date = dt.datetime.now().date() - dt.timedelta(days = 1)
the_day_before_date = dt.datetime.now().date() - dt.timedelta(days = 2)
yesterday_close = float(stock_data["Time Series (Daily)"][yesterday_date.strftime("%Y-%m-%d")]["4. close"])
the_day_before_close = float(stock_data["Time Series (Daily)"][the_day_before_date.strftime("%Y-%m-%d")]["4. close"])
change = ((yesterday_close - the_day_before_close) / the_day_before_close) * 100
if change >= 5:
    news_data = news_response.json()
    articles = news_data["articles"]
    for article in articles[:3]:
        title = article["title"]
        description = article["description"]
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_ ='',
        body = f" 🔺 {round(change)}%\n"
            f"Headline: {title}\n"
            f"Brief: {description}",
        to=''
    )
    print(message.sid)

elif change <= -5:
    news_data = news_response.json()
    articles = news_data["articles"]
    for article in articles[:3]:
        title = article["title"]
        description = article["description"]
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_ ='',
        body = f" 🔻 {round(change)}%"
            f"Headline: {title}"
            f"Brief: {description}",
        to = ''
    )
    print(message.sid)