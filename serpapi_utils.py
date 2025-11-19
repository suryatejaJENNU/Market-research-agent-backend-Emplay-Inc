import os
from serpapi import GoogleSearch

# getting serp api key from env (if not set then we fallback)
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def discover_companies(keyword):
    # no api key? then can't do real search so using some manual list
    if not SERPAPI_KEY:
        print("SERPAPI_KEY missing. Using fallback companies.")
        return [
            {"title": "Google", "url": "https://google.com", "snippet": "AI and Cloud"},
            {"title": "Microsoft", "url": "https://microsoft.com", "snippet": "Cloud + AI"},
            {"title": "Nvidia", "url": "https://nvidia.com", "snippet": "AI hardware"},
        ]

    # basic search params for serpapi, nothing fancy
    params = {
        "q": f"Top {keyword} companies",
        "engine": "google",
        "api_key": SERPAPI_KEY
    }

    try:
        # running serpapi search
        search = GoogleSearch(params)
        results = search.get_dict()
    except Exception as e:
       
        print("SerpAPI failed:", e)
        return []

    companies = []
    # looping through organic search results coz that's where companies usually appear
    for item in results.get("organic_results", []):
        companies.append({
            "title": item.get("title"),
            "url": item.get("link"),
            "snippet": item.get("snippet"),
        })

    # if serpapi didn't return anything then again use fallback
    if not companies:
        return [
            {"title": "Google", "url": "https://google.com", "snippet": "AI and Cloud"},
            {"title": "Nvidia", "url": "https://nvidia.com", "snippet": "AI GPU leader"},
        ]

    # only taking top 5 coz too many not needed
    return companies[:5]
