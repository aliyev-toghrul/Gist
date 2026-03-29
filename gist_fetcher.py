from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from firecrawl import FirecrawlApp
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

firecrawl = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY", "fc-YOUR_KEY_HERE"))

@app.get("/fetch")
async def fetch_url(url: str = Query(...)):
    try:
        result = firecrawl.scrape_url(url, params={"formats": ["markdown"]})
        return {"content": result.get("markdown", ""), "status": 200}
    except Exception as e:
        return {"content": "", "status": 500, "error": str(e)}

@app.get("/health")
async def health():
    return {"status": "ok"}
