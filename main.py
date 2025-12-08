from live_feed import LiveFeed
from trader import Trader
from utils import get_logger
import time

logger = get_logger("Main")

trader = Trader()

def handle(evt):
    logger.info(f"EVENT: {evt}")
    result = trader.handle_event(evt)
    logger.info(f"RESULT: {result}")

if __name__ == "__main__":
    feed = LiveFeed(handler=handle)
    feed.start()

    while True:
        time.sleep(1)
