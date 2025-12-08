# live_feed.py
import json
import random
import time
import threading
from websocket import WebSocketApp
from utils import get_logger
from normalizer import normalize_event
import config

logger = get_logger("LiveFeed")

class LiveFeed:
    def __init__(self, handler):
        self.handler = handler
        self.ws = None
        self.stop_flag = False

    def on_message(self, ws, msg):
        try:
            data = json.loads(msg)
        except:
            return
        if data.get("type") == "goal":
            evt = normalize_event(data)
            if evt:
                self.handler(evt)

    def on_error(self, ws, err):
        logger.error(f"WebSocket error: {err}")

    def on_close(self, ws, *_):
        logger.warning("WebSocket closed")

    def on_open(self, ws):
        logger.info("WebSocket connected")

    def start(self):
        if not config.WEBSOCKET_URL:
            logger.warning("No WebSocket URL — using mock feed")
            self.mock_loop()
            return

        def run():
            while not self.stop_flag:
                try:
                    self.ws = WebSocketApp(
                        config.WEBSOCKET_URL,
                        on_open=self.on_open,
                        on_message=self.on_message,
                        on_error=self.on_error,
                        on_close=self.on_close
                    )
                    self.ws.run_forever()
                except:
                    time.sleep(3)

        threading.Thread(target=run, daemon=True).start()

    def mock_loop(self):
        matches = [
            ("Arsenal", "Chelsea"),
            ("Barcelona", "Real Madrid"),
            ("Liverpool", "Man City"),
        ]
        scores = {}

        while True:
            home, away = random.choice(matches)
            match_id = f"{home}_{away}"
            scores.setdefault(match_id, [0, 0])
            h, a = scores[match_id]

            if random.random() < 0.5:
                h += 1
                scorer = home
            else:
                a += 1
                scorer = away

            scores[match_id] = [h, a]

            event = {
                "match_id": match_id,
                "home": home,
                "away": away,
                "team": scorer,
                "score": (h, a),
                "minute": random.randint(1, 90)
            }

            evt = normalize_event(event)
            self.handler(evt)
            time.sleep(5)
