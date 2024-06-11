Crypto Coin Scraper
This project is a Django-based web application that scrapes cryptocurrency data from CoinMarketCap using a Django REST API, Celery for task management, and BeautifulSoup for HTML parsing.

Features
Scrape Cryptocurrency Data: Extracts detailed information about specified cryptocurrencies from CoinMarketCap.
Asynchronous Task Management: Uses Celery to handle scraping tasks asynchronously.
Django REST API: Provides RESTful endpoints to start scraping tasks and check their status.
Data Storage: Stores scraping job details and results in a database.

Technologies Used
Django: Web framework
Django REST Framework: API framework
Celery: Asynchronous task queue
BeautifulSoup: HTML parsing
Requests: HTTP requests
RabbitMQ: Message broker for Celery


Usage
Start Scraping Task
To start a scraping task, send a POST request to /api/taskmanager/start_scraping with a JSON payload containing a list of cryptocurrency acronyms.
Check Scraping Status
To check the status of a scraping task, send a GET request to /api/taskmanager/scraping_status/<job_id>.
