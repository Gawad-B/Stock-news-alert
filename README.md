# Stock News Alert

This project is a Python script that monitors stock price changes and sends news alerts via SMS when significant changes occur. It uses the Alpha Vantage API for stock data, NewsAPI for news articles, and Twilio for sending SMS notifications.

## Features
- Monitors daily stock price changes for a specified company.
- Fetches the latest news articles related to the company if the stock price changes by more than ±5%.
- Sends SMS alerts with news headlines and summaries using Twilio.

## Requirements
- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [twilio](https://pypi.org/project/twilio/)
- API keys for Alpha Vantage, NewsAPI, and Twilio credentials

## Setup
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Stock-news-alert
   ```
2. **Install dependencies:**
   ```bash
   pip install requests twilio
   ```
3. **Configure your API keys:**
   - Edit `main.py` and set the following variables:
     - `STOCK` (e.g., 'TSLA')
     - `COMPANY_NAME` (e.g., 'Tesla Inc')
     - `NEWS_API_KEY` (your NewsAPI key)
     - `STOCK_API_KEY` (your Alpha Vantage key)
     - Twilio `account_sid`, `auth_token`, `from_`, and `to` numbers

## Usage
Run the script:
```bash
python main.py
```

If the stock price changes by more than 5% (up or down), you will receive an SMS with the top 3 news headlines and summaries.

## License
This project is licensed under the MIT License.
