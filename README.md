# API Opportunity Scanner

A FastAPI API-market research service designed to run on **Cloudflare Workers** using Cloudflare's Python Workers runtime.

## Cloudflare deployment

This repository is a **Cloudflare Worker**, not a Cloudflare Pages static site.

Use:

**Cloudflare Dashboard → Workers & Pages → Create application → Import a repository**

Select the GitHub repository `cyber24shield/api-opportunity-scanner` and branch `main`.

### Workers Build settings

- **Root directory:** `/`
- **Build command:** leave empty
- **Deploy command:** `npx wrangler deploy`
- **Production branch:** `main`

The repository already contains `wrangler.jsonc`, `pyproject.toml`, `src/main.py`, and `.python-version` for the Python Worker deployment.

Do **not** create this as a Pages project with `npm run build`. Pages expects a frontend build output; this project is an API Worker.

## Local development

Cloudflare's Python Workers tooling uses `pywrangler`:

```bash
uv run pywrangler dev
```

The Worker entrypoint is `src/main.py` and the FastAPI application is exposed through Cloudflare's ASGI adapter.

## Endpoints

- `GET /` — service information
- `GET /api/health` — health check
- `GET /api/opportunities` — list opportunities
- `GET /api/opportunities?category=AI` — filter by category
- `GET /api/opportunities/{id}` — inspect one opportunity
- `GET /api/trends` — ranked opportunities and categories
- `GET /docs` — FastAPI interactive documentation
- `GET /openapi.json` — OpenAPI specification for marketplace import

## Research model

The current dataset is intentionally labeled as **sample research data**. It is not a claim about current RapidAPI rankings. Future releases will add verified market observations and historical measurements so trend scores can be calculated from evidence rather than hand-entered values.

## Roadmap

1. Connect verified marketplace observations.
2. Store historical snapshots.
3. Track request volume, users, latency, errors, pricing and service levels where available.
4. Add trend detection and alerts.
5. Add competitor and endpoint analysis.
6. Build a research dashboard.
7. Use validated opportunities to select APIs for independent implementation.
