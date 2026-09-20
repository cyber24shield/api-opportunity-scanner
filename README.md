# API Opportunity Scanner

A FastAPI project for researching API-market opportunities using demand, developer interest, trend growth, monetization, competition gaps, performance gaps, and reliability gaps.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs` for interactive API documentation.

## Endpoints

- `GET /api/health` — health check
- `GET /api/opportunities` — list opportunities
- `GET /api/opportunities?category=AI` — filter by category
- `GET /api/opportunities/{id}` — inspect one opportunity
- `GET /api/trends` — available categories and dataset count

## Research model

The current dataset is intentionally labeled as sample research data. It is not a claim about current RapidAPI rankings. The next version will add verified market observations and historical measurements so trend scores can be calculated from evidence rather than hand-entered values.

## Roadmap

1. Connect verified marketplace observations.
2. Store historical snapshots.
3. Track request volume, users, latency, errors, pricing and service levels where available.
4. Add trend detection and alerts.
5. Add competitor and endpoint analysis.
6. Build a dashboard.
7. Use validated opportunities to select APIs for independent implementation.
