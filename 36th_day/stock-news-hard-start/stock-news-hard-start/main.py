import requests
import os
import time
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime, timedelta

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_key = os.getenv("NEWS_API_KEY")
stock_key = os.getenv("STOCK_API")
phone_number = os.getenv("PHONE_NUMBER")

yesterday = (datetime.now()-timedelta(2)).strftime('%Y-%m-%d')
before_yesterday=(datetime.now()-timedelta(4)).strftime('%Y-%m-%d')

params = {"q":COMPANY_NAME,
          "from": yesterday,
          "to":before_yesterday,
          "sortBy":"popularity",
          "apiKey":news_key}

response_news = requests.get(NEWS_ENDPOINT,params=params)
response_news.raise_for_status()
relevant_news:list = []

#--------------------Stocks---------------------#
params_stock = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":stock_key,
}
response_stock = requests.get(STOCK_ENDPOINT,params_stock)
response_stock.raise_for_status()

stock_info =response_stock.json()["Time Series (Daily)"]
stock_info_last_day = stock_info[yesterday]
stock_info_before_last_day = stock_info[before_yesterday]


stock_difference = float(stock_info_last_day["4. close"]) - float(stock_info_before_last_day["4. close"])
sign = "-" if stock_difference<0 else "+"
change_percentage = float((stock_difference/float(stock_info_before_last_day["4. close"]))*100)

# Top 3 relevant news
def get_last_news():
    news_articles = response_news.json()["articles"]
    return news_articles[0:3]

if abs(change_percentage)>2:
    relevant_news= get_last_news()

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator


# Use Twilio for SMS

def send_notifications(relevant_news):
        global stock_difference,change_percentage
        account_sid = os.getenv("TWILLIO_ACCOUNT_SID")
        TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid,TWILIO_AUTH_TOKEN)
        for news_article in relevant_news:
            title = news_article["title"]
            description = news_article["description"]
            percentage = "%.2f" % abs(change_percentage)
            message = client.messages.create(body=f"{STOCK} {' v 'if stock_difference<0 else' ^ '}{percentage} \nHeadline: {title}\nBrief: {description}",
                                     from_="+12209460604",
                                     to=phone_number)

        

#Call SMS

send_notifications(relevant_news)


