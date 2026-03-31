# Gist — Project Progress Log

## Status: Phase 2 Active
_Last updated: 2026-03-31_

---

## ✅ Phase 1 — Complete

### Built & Working
- `gist_fetcher.py` — FastAPI microservice (Firecrawl scraping, port 8000)
- `start.fish` — one-command startup (uvicorn + cloudflared tunnel)
- Opal pipeline — 3 nodes:
  - **Fetch Content** (Gemini Flash)
  - **Analyze Content**
  - **Render Analysis Report**
- GitHub URL analysis: fully tested (ZeroT repo analyzed successfully)

### Pending from Phase 1
- [ ] LinkedIn URL test in Opal
- [ ] Instagram URL test in Opal
- [ ] Full structured master prompt in Analyze Content node:
  - Sections: TL;DR · Key Insights · Gaps · Signal Score · Demo Recommendation

---

## 🔄 Phase 2 — In Progress

### Order of execution
- [ ] 1. Test LinkedIn + Instagram URLs in Opal
- [ ] 2. Add HuggingFace tone classifier endpoint → `gist_fetcher.py`
- [ ] 3. Add spaCy NER entity extractor endpoint
- [ ] 4. Add MiniLM duplicate detector endpoint
- [ ] 5. Wire tone/NER/duplicate nodes into Opal as Generate nodes (after Analyze Content)
- [ ] 6. Build Gist landing page on Vercel

---

## 📌 Stack
- Backend: FastAPI + Firecrawl + Cloudflare Tunnel
- Pipeline: Opal
- Scraping LLM: Gemini Flash
- Repo: github.com/Jowker17/Gist (private, Apache 2.0)
