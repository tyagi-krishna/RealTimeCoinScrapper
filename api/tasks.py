from celery import shared_task
from .coinmarketcap import CoinMarketCap

@shared_task
def scrape_coin_data(coin_acronyms):
    scraper = CoinMarketCap()
    results = {}
    for acronym in coin_acronyms:
        results[acronym] = scraper.scrape_coin(acronym)
    return results
