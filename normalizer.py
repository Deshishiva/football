def normalize_event(raw):
    return {
        "match_id": raw["match_id"],
        "home": raw["home"],
        "away": raw["away"],
        "team": raw["team"],
        "score": raw["score"],
        "minute": raw["minute"]
    }
