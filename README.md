Goal Shock Trader

Goal Shock Trader is a small prototype of a real-time, goal-reaction trading engine for football matches.

The core idea is simple: when a goal happens, the system checks whether the scoring team is the underdog. If an underdog scores and the market probability is still below 50%, the engine generates a simulated BUY signal. This is based on the assumption that prediction markets briefly lag after unexpected goals.

This project was built as part of the Omniverse Fund – AI/ML / Quant Intern assessment. It is not meant to be a full trading bot, but a clean demonstration of event-driven system design and trading decision logic.

What the Engine Does

Listens to football goal events (live or mock)

Normalizes incoming data into a consistent format

Maps each match to a synthetic in-play market

Fetches the current market probability

Checks if the scoring team is an underdog

Executes a simulated BUY when conditions are met

Logs all decisions clearly in the terminal

Workflow Overview

A goal event is received from a feed

The event is normalized into a standard structure

The match is mapped to a market ID

The current market probability is retrieved

The trader checks:

Did the underdog score?

Is probability below 0.50?

Is the goal minute within limits?

If yes, a simulated BUY order is executed

Project Structure
main.py            → entry point
live_feed.py       → WebSocket-based live goal feed
mock_feed.py       → simulated goal feed
normalizer.py      → event normalization
matcher.py         → match-to-market mapping
market_ticker.py  → real-time probability access
trader.py          → trading decision logic
kalshi_client.py   → Kalshi demo trading support
market.py          → market helpers
price_feed.py     → simulated pricing
utils.py           → logging utilities
index.html         → submission / portfolio page
logs/              → runtime logs
README.md          → project documentation

How to Run
Install dependencies
pip install websocket-client requests

Run the engine
python main.py


The engine will start immediately and print goal events and trade decisions in real time.

Example Output
EVENT: Juventus_Inter | Score: (1, 1) | Minute: 33
RESULT: BUY | market=MKT_Juventus_Inter | price=0.33 | size=20

EVENT: Arsenal_Chelsea | Score: (0, 1)
RESULT: NO TRADE | reason=high_prob

Notes

Requires no paid APIs to run

Falls back to mock data automatically if live feeds are not provided

Designed to be easily extended with real exchanges and market data