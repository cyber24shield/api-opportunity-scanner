from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .data import OPPORTUNITIES
from .scoring import opportunity_score

app = FastAPI(title="API Opportunity Scanner", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root():
    return {"service": "API Opportunity Scanner", "docs": "/docs"}

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "api-opportunity-scanner", "version": "0.1.0"}

@app.get("/api/opportunities")
def opportunities(category: str | None = Query(None)):
    items = OPPORTUNITIES
    if category:
        items = [x for x in items if x["category"].lower() == category.lower()]
    return [
        {**item, "opportunity_score": opportunity_score(item)}
        for item in items
    ]

@app.get("/api/opportunities/{opportunity_id}")
def opportunity(opportunity_id: str):
    item = next((x for x in OPPORTUNITIES if x["id"] == opportunity_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return {**item, "opportunity_score": opportunity_score(item)}

@app.get("/api/trends")
def trends():
    categories = sorted({x["category"] for x in OPPORTUNITIES})
    return {"categories": categories, "count": len(OPPORTUNITIES)}
