import os
import json
import requests
from newsapi import NewsApiClient

def extract_news_data(dates, ticker):
    """Extract news data (title, description, and publishedAt)

    Args:
        dates ([array]): array of dates
        filename (string): filename (location)
    """
    all_articles = []
    list_of_article = {} # Dictionary to keep track of duplicates

    for date in dates:
        with open("../data/{}/raw_data/{}.json".format(ticker, date), "r") as f:
            data = json.load(f)

            for article in data["articles"]:
                # Exclude news without title
                if not article["title"]:    
                    continue

                # Remove duplicate Reuters sources
                if "Reuters" in article["title"]:
                    article["title"] = article["title"].split("-")[0].strip()
                
                # Skip duplicated article
                if article["title"] in list_of_article:
                    continue

                list_of_article[article["title"]] = 1

                # Extract news with "\n\n" filter
                if article["description"] and "\n" in article["description"]:
                    article["description"] = article["description"].replace("\n", " ")
                
                # Exclude news with html links
                if article["description"] and ("<li>" in article["description"] or "href=" in article["description"] or "http" in article["description"]):
                    continue

                # Exclude news without article description
                if not article["description"]:
                    continue

                all_articles.append({
                    "title": article["title"], 
                    "description": str(article["description"].encode("ascii", "ignore")), 
                    "publishedAt": article["publishedAt"].split("T")[0]
                })

    with open("../data/{}/raw_data/news_{}.json".format(ticker, ticker), "w") as f:
        json.dump(all_articles, f)


def collect_news_data(dates, query, sources, ticker):
    """News collection via NewsAPI.org

    Args:
        dates ([array]): array of dates
        query (string): query string
        sources ([array]): list of sources to collect news from
        save_location (string): news data save location
    """
    newsapi = NewsApiClient(api_key='KEY')

    for date in dates:
        articles = newsapi.get_everything(q=query,                           
                                          language='en',
                                          from_param=date,
                                          to=date,
                                          sources=sources,
                                          sort_by="relevancy",
                                          page_size=100)

        if not os.path.exists("../data/{}/raw_data".format(ticker)):
            os.makedirs("../data/{}/raw_data".format(ticker))

        with open("../data/{}/raw_data/{}.json".format(ticker, date), "w") as f:
            f.write(json.dumps(articles, indent=4))


def main():
    
    # NewsAPI (developer account) only allows articles up to 1 month old
    dates = ["2020-10-09", 
             "2020-10-10", 
             "2020-10-11", 
             "2020-10-12", 
             "2020-10-13", 
             "2020-10-14", 
             "2020-10-15", 
             "2020-10-16", 
             "2020-10-17", 
             "2020-10-18", 
             "2020-10-19", 
             "2020-10-20", 
             "2020-10-21", 
             "2020-10-22", 
             "2020-10-23", 
             "2020-10-24", 
             "2020-10-25", 
             "2020-10-26", 
             "2020-10-27", 
             "2020-10-28", 
             "2020-10-29", 
             "2020-10-30", 
             "2020-10-31", 
             "2020-11-01", 
             "2020-11-02", 
             "2020-11-03", 
             "2020-11-04", 
             "2020-11-05", 
             "2020-11-06", 
             "2020-11-07", 
             "2020-11-08", 
             "2020-11-09"]
    
    # Query terms (Tesla - TSLA)
    #query = "tesla OR tsla OR elon OR musk"

    # Query terms (Apple - AAPL)
    #query = "apple OR aapl OR iphone OR 5G"

    # Query terms (Boeing - BA)
    query = "boeing OR airline OR airlines OR aviation"

    # News sources
    sources = "bloomberg,cnn,cnbc,business-insider,financial-post,fortune,hacker-news,time,wired,techcrunch,techradar,the-verge,the-washington-times,engadget,mashable,ars-technica,reuters,google-news,newsweek,next-big-future,politico"

    collect_news_data(dates, query, sources, "BA")
    extract_news_data(dates, "BA")

    # https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&datatype=csv&apikey=KEY

if __name__ == "__main__":
    main()

