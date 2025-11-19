from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from market_research_agent import run_research_agent

# making fastapi app, nothing fancy here
app = FastAPI()

# enabling cors coz frontend will call from different port
# so just allowing everything 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],    
)

# model for request body, only taking 'brief'
class ResearchRequest(BaseModel):
    brief: str

# api endpoint for running agent
# frontend will call this one only
@app.post("/api/research")
def run_agent(req: ResearchRequest):
    # just passing the text to main agent fn
    return run_research_agent(req.brief)
