#!/usr/bin/env fish
pkill -f uvicorn
cd ~/Gist
source venv/bin/activate.fish
set -x FIRECRAWL_API_KEY "fc-1f6596adcecc465e9d586cad0d01404b"
uvicorn gist_fetcher:app --port 8000 &
sleep 3
cloudflared tunnel --url http://localhost:8000
