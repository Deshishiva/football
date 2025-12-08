from utils import get_logger
import market_ticker
import kalshi_client
import config

logger = get_logger("Trader")

class Trader:
    def __init__(self):
        self.kalshi = kalshi_client.KalshiClient()

    def handle_event(self, event):
        minute = event["minute"]
        match_id = event["match_id"]

        if minute < config.MIN_GOAL_MINUTE:
            return {"action": "no_trade", "reason": "too_early"}

        prob = market_ticker.get_market_probability(match_id)

        if prob >= config.PROBABILITY_THRESHOLD:
            return {"action": "no_trade", "reason": "high_prob"}

        market_id = market_ticker.market_id_from_match(match_id)

        order = self.kalshi.place_order(
            market_id=market_id,
            size=config.TRADE_SIZE,
            price=prob
        )

        return {
            "action": "buy",
            "market": market_id,
            "price": prob,
            "order": order
        }
