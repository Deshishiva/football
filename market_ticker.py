
import random
import config
import requests
from utils import get_logger

logger = get_logger("Ticker")

def market_id_from_match(match_id):
    return f"MKT_{match_id}"

def get_market_probability(match_id):
    mid = market_id_from_match(match_id)

    if config.TICKER_API:
        try:
            r = requests.get(
                f"{config.TICKER_API}/{mid}",
                timeout=5,
                headers={"Authorization": f"Bearer {config.TICKER_API_KEY}"}
            )
            if r.status_code == 200:
                data = r.json()
                return float(data.get("probability", 0.5))
        except:
            pass

    return round(random.uniform(0.25, 0.75), 2)
