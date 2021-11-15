import time
from re import sub
import requests
from bs4 import BeautifulSoup

def get_price_from_blockchain_website(crcy_code):
    milliseconds_to = int(round(time.time()))
    milliseconds_from = milliseconds_to - 604800

    request_url = 'https://api.blockchain.info/price-historic/prices?coins=' + str(crcy_code) + '&fromTime=' + str(
        milliseconds_from) + '&toTime=' + str(milliseconds_to) + '&fiat=USD'

    print("Fetching prices from blockchain website by hitting: " + request_url)
    response = requests.get(request_url)
    data = response.json()
    price = data['pairs']['USD-' + str(crcy_code)][0]['value']
    print("Price from blockchain website for crcy_code " + str(crcy_code) + " is " + str(price))
    return float(price)


def get_bitcoin_price_from_coingecko_website():
    print("Fetching prices from coingecko website by hitting: https://www.coingecko.com/en/coins/bitcoin")
    source = requests.get('https://www.coingecko.com/en/coins/bitcoin')
    soup = BeautifulSoup(source.content, "html.parser")
    price = soup.find("span", {"class": "no-wrap", "data-coin-id": "1", "data-coin-symbol": "btc"}).text
    print("Price from coingecko website for bitcoin is " + price)
    return float(sub(r'[^\d.]', '', price))


def get_ethereum_price_from_coingecko_website():
    print("Fetching prices from coingecko website by hitting: https://www.coingecko.com/en/coins/ethereum")
    source = requests.get('https://www.coingecko.com/en/coins/ethereum')
    soup = BeautifulSoup(source.content, "html.parser")
    price = soup.find("span", {"class": "no-wrap", "data-coin-id": "279", "data-coin-symbol": "eth"}).text
    print("Price from coingecko website for bitcoin is " + price)
    return float(sub(r'[^\d.]', '', price))

def generate_response(currency):
    if currency == 'bitcoin':
        tag = 'BTC'
    else:
        tag = 'ETH'
    blockchain_price = get_price_from_blockchain_website(tag)
    if currency == 'bitcoin':
        coingecko_price = get_bitcoin_price_from_coingecko_website()
    else:
        coingecko_price = get_ethereum_price_from_coingecko_website()
    response =  create_response_obj(currency, blockchain_price, coingecko_price)
    return response


def create_response_obj(currency, blockchain_price, coingecko_price):
    if (blockchain_price < coingecko_price):
        response_body = {
            "currency": currency,
            "blockchain": blockchain_price,
            "coingecko": coingecko_price,
            "buy": "blockchain.com",
            "buyPrice": blockchain_price,
            "sell": "coingecko.com",
            "sellPrice": coingecko_price
        }
    else:
        response_body = {
            "currency": currency,
            "blockchain": blockchain_price,
            "coingecko": coingecko_price,
            "sell": "blockchain.com",
            "sellPrice": blockchain_price,
            "buy": "coingecko.com",
            "buyPrice": coingecko_price
        }
    return response_body
