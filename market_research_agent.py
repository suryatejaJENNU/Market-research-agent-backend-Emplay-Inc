import json
from llm_utils import expand_keywords, generate_summary, analyze_sentiment
from serpapi_utils import discover_companies
from news_utils import fetch_news
from datetime import datetime

# getting keywords from the user brief
# (first 2 steps together only)
def step_1_and_2_brief_to_keywords(brief: str):
    return expand_keywords(brief, n=5)

# using the keywords to find companies from serpapi
# just picking based on first keyword
def step_3_company_discovery(keywords):
    return discover_companies(keywords[0])

# here doing news + sentiment stuff
# kinda long step but okay
def step_4_5_6_gather_and_analyze(companies, keywords):
    output = []

    for c in companies:
        title = c["title"]
        url = c["url"]
        snippet = c["snippet"]
        news_articles = fetch_news(title)
        
        news_titles = [n.get("title") for n in news_articles if n.get("title")]

        sentiment = analyze_sentiment(news_titles)

      
        output.append({
            "company": title,
            "url": url,
            "snippet": snippet,
            "news_count": len(news_titles),
            "news_samples": news_titles[:5],  
            "sentiment_summary": sentiment
        })

    return output

# step for making the long summary text
def step_7_generate_report(data):
    return generate_summary(data)

# combining everything in proper final json
# so frontend can show all steps neatly
def step_8_format_output(steps):
    return {
        "status": "success",
        "date": datetime.utcnow().isoformat(),

        # putting clear names for all steps coz assignment needs it
        "steps": {
            "STEP 1 & 2 — Extracted Keywords": steps["step_1_keywords"],
            "STEP 3 — Discovered Companies": steps["step_3_companies"],
            "STEP 4, 5 & 6 — News + Sentiment Analysis": steps["step_4_5_6"],
            "STEP 7 — Market Research Report": steps["step_7_report"]
        },

        # final required result
        "final_report": steps["step_7_report"],
        "final_data": steps["step_4_5_6"]
    }

# main function that runs all the above things
def run_research_agent(brief: str):

    # STEP 1 & 2
    keywords = step_1_and_2_brief_to_keywords(brief)

    # STEP 3
    companies = step_3_company_discovery(keywords)

    # STEP 4,5,6
    aggregated = step_4_5_6_gather_and_analyze(companies, keywords)

    # STEP 7
    report_text = step_7_generate_report(aggregated)

    # collecting all step outputs in one dict
    steps = {
        "step_1_keywords": keywords,
        "step_3_companies": companies,
        "step_4_5_6": aggregated,
        "step_7_report": report_text
    }

    # STEP 8 return final formatted json
    return step_8_format_output(steps)
