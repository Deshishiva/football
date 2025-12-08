
import json
import config
import requests
from utils import get_logger

logger = get_logger("Kalshi")

class KalshiClient:
    def __init__(self, demo=True):
        self.demo = config.KALSHI_DEMO
        self.base = "https://demo-api.kalshi.com"

    def place_order(self, market_id, size, price):
        if not config.KALSHI_ENABLED:
            return {"status": "simulated", "market": market_id, "size": size, "price": price}

        body = {
            "market": market_id,
            "side": "buy",
            "size": size,
            "price": price
        }

        try:
            r = requests.post(
                f"{self.base}/v1/orders",
                json=body,
                headers={"Authorization": f"Bearer {config.KALSHI_API_KEY}"}
            )
            return r.json()
        except:
            return {"status": "error"}
