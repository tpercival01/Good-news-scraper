# Good news scraper

Good news scraper is currently a script for scraping particular news websites for articles. There are multiple functions for each news website to allow the user to choose specifically, as well as a function that uses the NewsAPI to collect all news.

This was originally created as a dissertation project for an iOS application. It is now being recreated to be a standalone news article scraper with sentiment analysis.

## Usage

Each news website will have its own function that can be called separately which will return an array of dict variables containing the crucial data from the article (author, title, body text, link).

```python

reddit()

bbc()

```

Alongside this, the program also uses the NewsAPI module to return a number of articles from all news sources across the globe.

```python

allNews()

```



## Roadmap

- Increase number of websites that can be scraped.
- Create GUI for the script to allow easier use.
- Deploy as an iOS application on the appstore.