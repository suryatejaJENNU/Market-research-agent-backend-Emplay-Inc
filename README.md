# Market Research Agent – Backend

This is the backend service for the Market Research Tool. It automates the process of analyzing a market brief by finding relevant companies, aggregating news, analyzing sentiment, and generating a comprehensive summary using AI.

The backend is built with **FastAPI**.

## 🚀 Live Backend

The backend is currently deployed on Render:
**Base URL:** [https://market-research-agent-backend.onrender.com](https://market-research-agent-backend.onrender.com)

**Main Endpoint:** `POST /api/research`

---

## 🛠 What This Project Does

The agent performs the following workflow step-by-step:

1.  **Keyword Generation:** Takes a user brief and uses Gemini to generate 5 relevant search keywords.
2.  **Company Discovery:** Uses the first keyword to find companies via SerpAPI.
    * *Note:* If the SerpAPI key is missing, it uses a defined set of fallback companies.
3.  **News Aggregation:** For each identified company:
    * Fetches the latest news.
    * Selects the top 5 headlines.
4.  **Sentiment Analysis:** Gemini analyzes the sentiment of the fetched headlines.
5.  **Report Generation:** Gemini compiles all data into a full market research report.
6.  **Final Output:** Returns a structured JSON response containing every step of the process and the final summary.

---

##  Folder Structure

```text
market-research-agent/
│
├── main.py                  # Application entry point
├── market_research_agent.py # Main agent logic
├── llm_utils.py             # Gemini API interactions
├── serpapi_utils.py         # Google Search interactions
├── news_utils.py            # News fetching logic
├── test_agent.py            # Script to test the agent locally
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables
```

## Tech Used
```text
FastAPI (Web Framework)

Uvicorn (ASGI Server)

Gemini API (LLM for keywords, sentiment, and summary)

SerpAPI (Optional - for company search)

NewsAPI (Optional - for news fetching)

Python 3.10

Dotenv

## How To Run This Project Locally
Follow these steps to set up the project on your machine:

1. **Create a Virtual Environment**

python -m venv venv
2. **Activate the Environment (Windows)**


venv\Scripts\activate
(For macOS/Linux: source venv/bin/activate)

3. **Install Dependencies**
pip install -r requirements.txt


4. **Create .env File**
Create a file named .env in the root directory and add the following keys:
GEMINI_API_KEY=your_key
GOOGLE_API_KEY=your_key
SERPAPI_KEY=optional_key
NEWS_API_KEY=optional_key

Required: GEMINI_API_KEY (and GOOGLE_API_KEY if your code uses that variable name for Gemini).

Optional: SERPAPI_KEY and NEWS_API_KEY. If missing, the backend uses fallback data.

5. **Start the Server**
uvicorn main:app --reload

```

## API Documentation

Generate Research Report
Endpoint: /api/research

**Method: POST**

**Request Body Example:
{
  "brief": "Find top AI telecom companies"
}**

**Response: The response includes a structured JSON object containing:**

keywords

companies

news

sentiment

final_report
```
## Environment Variables Guide
```text
**Variable,Purpose**
GEMINI_API_KEY,"Used for generating keywords, checking sentiment, and writing summaries."
SERPAPI_KEY,Used for discovering companies based on keywords.
NEWS_API_KEY,Used for fetching real-time news.

**Deploying on Render**
If you are deploying this project to Render, use the following settings:

**Build Command:**
pip install -r requirements.txt

**Start Command:**
uvicorn main:app --host 0.0.0.0 --port $PORT

Environment Variables: Add your keys (GEMINI_API_KEY, etc.) in the Render Dashboard under the "Environment" tab.

```
## Testing
To test the agent logic without running the full server, run the test script:
python test_agent.py


## Extra Notes
```text
CORS: Enabled to allow connections from a React frontend.

Quotas: If the Gemini API quota is exceeded, some parts of the response may indicate "unavailable".

Fallbacks: The system is designed to work even without SerpAPI or NewsAPI keys by providing mock data.
```
