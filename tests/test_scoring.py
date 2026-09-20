from app.scoring import opportunity_score


def test_opportunity_score_is_weighted():
    item = {
        "demand": 100,
        "developer_interest": 100,
        "trend_growth": 100,
        "monetization": 100,
        "competition_gap": 100,
        "performance_gap": 100,
        "reliability_gap": 100,
    }
    assert opportunity_score(item) == 100.0
