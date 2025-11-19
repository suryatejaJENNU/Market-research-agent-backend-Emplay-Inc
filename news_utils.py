import os
from newsapi import NewsApiClient

# getting the key from env (if not there then we just fallback)
NEWS_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(company):
   
    if not NEWS_KEY:
        print("NEWS_API_KEY missing. Using fallback news.")
        return [
            {"title": f"{company} announces new AI product", "url": "#"},
            {"title": f"{company} partners with telecom provider", "url": "#"},
        ]

   
    newsapi = NewsApiClient(api_key=NEWS_KEY)

    try:
       
        articles = newsapi.get_everything(
            q=company,
            language="en",
            sort_by="publishedAt",
            page_size=5 
        )
    except Exception as e:
       
        print(" NewsAPI failed:", e)
        return []

    # making simple list of needed info only
    return [
        {
            "title": art.get("title"),
            "url": art.get("url")
        }
        for art in articles.get("articles", [])
    ]
