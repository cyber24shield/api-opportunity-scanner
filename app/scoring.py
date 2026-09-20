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
    score = sum(item.get(metric, 0) * weight for metric, weight in WEIGHTS.items())
    return round(score, 1)
