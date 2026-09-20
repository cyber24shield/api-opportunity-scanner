from fastapi import FastAPI, Query, HTTPException
from workers import asgi

app = FastAPI(
    title="API Opportunity Scanner",
    description="Research API-market opportunities using demand, trends, competition, performance, reliability and monetization signals.",
    version="0.2.0",
)

OPPORTUNITIES = [
    {"id": "ai-agents", "name": "AI Agents API", "category": "AI", "demand": 88, "developer_interest": 91, "trend_growth": 94, "monetization": 86, "competition_gap": 55, "performance_gap": 62, "reliability_gap": 58},
    {"id": "security-scanning", "name": "Website Security Scanning API", "category": "Security", "demand": 79, "developer_interest": 76, "trend_growth": 83, "monetization": 81, "competition_gap": 64, "performance_gap": 70, "reliability_gap": 67},
    {"id": "translation", "name": "Language Translation API", "category": "Translation", "demand": 84, "developer_interest": 82, "trend_growth": 89, "monetization": 78, "competition_gap": 61, "performance_gap": 72, "reliability_gap": 65},
    {"id": "finance-data", "name": "Financial Data API", "category": "Finance", "demand": 90, "developer_interest": 87, "trend_growth": 78, "monetization": 91, "competition_gap": 48, "performance_gap": 59, "reliability_gap": 53},
    {"id": "developer-tools", "name": "Developer Utility API", "category": "Developer Tools", "demand": 76, "developer_interest": 81, "trend_growth": 80, "monetization": 73, "competition_gap": 69, "performance_gap": 75, "reliability_gap": 71},
]

WEIGHTS = {
    "demand": 0.20,
    "developer_interest": 0.15,
    "trend_growth": 0.20,
    "monetization": 0.15,
    "competition_gap": 0.10,
    "performance_gap": 0.10,
    "reliability_gap": 0.10,
}


def opportunity_score(item: dict) -> float:
    return round(sum(item.get(k, 0) * w for k, w in WEIGHTS.items()), 1)


@app.get("/")
def root():
    return {"service": "API Opportunity Scanner", "version": "0.2.0", "docs": "/docs", "openapi": "/openapi.json"}


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "api-opportunity-scanner", "runtime": "cloudflare-workers", "version": "0.2.0"}


@app.get("/api/opportunities")
def opportunities(category: str | None = Query(None)):
    items = OPPORTUNITIES
    if category:
        items = [x for x in items if x["category"].lower() == category.lower()]
    return [{**item, "opportunity_score": opportunity_score(item)} for item in items]


@app.get("/api/opportunities/{opportunity_id}")
def opportunity(opportunity_id: str):
    item = next((x for x in OPPORTUNITIES if x["id"] == opportunity_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return {**item, "opportunity_score": opportunity_score(item)}


@app.get("/api/trends")
def trends():
    ranked = sorted(
        ({"id": x["id"], "name": x["name"], "category": x["category"], "opportunity_score": opportunity_score(x)} for x in OPPORTUNITIES),
        key=lambda x: x["opportunity_score"],
        reverse=True,
    )
    return {"categories": sorted({x["category"] for x in OPPORTUNITIES}), "count": len(OPPORTUNITIES), "opportunities": ranked}


Default = asgi.entrypoint(app)
