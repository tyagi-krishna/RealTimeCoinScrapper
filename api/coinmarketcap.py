import requests
from bs4 import BeautifulSoup

class CoinMarketCap:
    BASE_URL = "https://coinmarketcap.com/currencies/"

    def fetch_page(self, coin_acronym):
        url = f"{self.BASE_URL}{coin_acronym}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def parse_page(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        data = {
            "price": self.get_price(soup),
            "price_change": self.get_price_change(soup),
            "market_cap": self.get_market_cap(soup),
            "market_cap_rank": self.get_market_cap_rank(soup),
            "volume": self.get_volume(soup),
            "volume_rank": self.get_volume_rank(soup),
            "volume_change": self.get_volume_change(soup),
            "circulating_supply": self.get_circulating_supply(soup),
            "total_supply": self.get_total_supply(soup),
            "diluted_market_cap": self.get_diluted_market_cap(soup),
            "contracts": self.get_contracts(soup),
            "official_links": self.get_official_links(soup),
            "socials": self.get_social_links(soup)
        }
        print(data)
        return data
    
    def get_price(self, soup):
        try:
            price_span = soup.find("span", class_="sc-d1ede7e3-0 fsQm base-text")
            price = price_span.text.strip().replace('$', '').replace(',', '')
            return float(price)
        except (AttributeError, ValueError):
            return None

    def get_price_change(self, soup):
        try:
            price_change_span = soup.find("span", class_="sc-d1ede7e3-0 kzFEmO")
            price_change = price_change_span.text.strip().replace('%', '')
            return float(price_change)
        except (AttributeError, ValueError):
            return None
        
    
    def get_market_cap(self, soup):
        try:
            market_cap_spans = soup.find_all("span", class_="sc-4c05d6ef-0 sc-58c82cf9-0 dlQYLv dTczEt")
            market_cap = market_cap_spans[0].text.strip().replace('$', '').replace(',', '')
            return float(market_cap)
        except (AttributeError, ValueError, IndexError):
            return None
        
    def get_market_cap_rank(self, soup):
        try:
            rank_span = soup.find("span", class_="text slider-value rank-value")
            rank = rank_span.text.strip().replace('#', '')
            return int(rank)
        except (AttributeError, ValueError):
            return None
        
    
    def get_volume(self, soup):
        try:
            volume_spans = soup.find_all("span", class_="sc-d1ede7e3-0 hPHvUM base-text")
            volume = volume_spans[0].text.strip().replace('$', '').replace(',', '')
            return float(volume)
        except (AttributeError, ValueError, IndexError):
            return None
        
    
    def get_volume_rank(self, soup):
        try:
            volume_rank_span = soup.find("span", class_="text slider-value rank-value")
            volume_rank = volume_rank_span.text.strip().replace('#', '')
            return int(volume_rank)
        except (AttributeError, ValueError):
            return None
        
    def get_volume_change(self, soup):
        try:
            volume_change_spans = soup.find_all("span", class_="sc-d1ede7e3-0 hPHvUM base-text")
            volume_change = volume_change_spans[1].text.strip().replace('%', '')
            return float(volume_change)
        except (AttributeError, ValueError, IndexError):
            return None
        
    def get_circulating_supply(self, soup):
        try:
            circulating_supply_spans = soup.find_all("span", class_="sc-d1ede7e3-0 hPHvUM base-text")
            circulating_supply = circulating_supply_spans[2].text.strip().replace('$', '').replace(',', '')
            return float(circulating_supply)
        except (AttributeError, ValueError, IndexError):
            return None

    def get_total_supply(self, soup):
        try:
            total_supply_spans = soup.find_all("span", class_="sc-d1ede7e3-0 hPHvUM base-text")
            total_supply = total_supply_spans[3].text.strip().replace('$', '').replace(',', '')
            return float(total_supply)
        except (AttributeError, ValueError, IndexError):
            return None

    def get_diluted_market_cap(self, soup):
        try:
            diluted_market_cap_spans = soup.find_all("span", class_="sc-d1ede7e3-0 hPHvUM base-text")
            diluted_market_cap = diluted_market_cap_spans[4].text.strip().replace('$', '').replace(',', '')
            return float(diluted_market_cap)
        except (AttributeError, ValueError, IndexError):
            return None

    def get_contracts(self, soup):
        try:
            contract_spans = soup.find_all("span", class_="sc-71024e3e-0 dEZnuB")
            contracts = [{"name": span.text.strip(), "address": span.get("data-clipboard-text")} for span in contract_spans]
            return contracts
        except AttributeError:
            return None

    def get_official_links(self, soup):
        try:
            official_link_spans = soup.find_all("a", class_="sc-d1ede7e3-0 sc-7f0f401-0 gRSwoF gQoblf")
            official_links = [{"name": link.text.strip(), "link": link.get("href")} for link in official_link_spans]
            return official_links
        except AttributeError:
            return None

    def get_social_links(self, soup):
        try:
            twitter_spans = soup.find_all("a", class_="sc-d1ede7e3-0 sc-7f0f401-0 gRSwoF gQoblf", string="Twitter")
            telegram_spans = soup.find_all("a", class_="sc-d1ede7e3-0 sc-7f0f401-0 gRSwoF gQoblf", string="Telegram")
            
            twitter_links = [span.get("href") for span in twitter_spans]
            telegram_links = [span.get("href") for span in telegram_spans]
            
            socials = []
            for twitter_link in twitter_links:
                socials.append({"name": "twitter", "url": twitter_link})
            for telegram_link in telegram_links:
                socials.append({"name": "telegram", "url": telegram_link})
            
            return socials
        except AttributeError:
            return None

    def scrape_coin(self, coin_acronym):
        html_content = self.fetch_page(coin_acronym)
        return self.parse_page(html_content)
    

# cmc = CoinMarketCap()

# duko_data = cmc.scrape_coin("bitcoin")

# print(duko_data)