# Good news scraper

Good news scraper is currently a script for scraping particular news websites for articles. There are multiple functions for each news website to allow the user to choose specifically, as well as a function that uses the NewsAPI to collect all news.

The program consists of three files: datascraper, sentimentAnalysis and populateFirebase. 

The sentimentAnalysis file can be used to iterate through each article and return a value of either negative, neutral or positive. This value can determine whether that article is a negative or positive article.

The populateFirebase file was used to send the data to a Firebase database that an iOS application would read from.

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