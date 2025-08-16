# Website Article Title Scraper

This project is a simple Python script that retrieves and displays the title of a website article using a provided URL.

## Features

* Retrieves the article title from the `<h1>` tag.
* If the `<h1>` tag is not found, the script will try to get the title from the `<title>` tag.
* Handles errors if the URL cannot be accessed.

## Requirements

You need to install the `requests` and `BeautifulSoup4` libraries. You can install them using pip:

```bash
pip install requests beautifulsoup4
