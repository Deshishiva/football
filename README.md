Goal Shock Trader

This project is a small prototype of a goal-reaction trading engine. The idea is simple: when a football match goal happens, the system checks if the scoring team is the underdog. If yes, it triggers a simulated “BUY” signal, based on the assumption that real markets (like Kalshi or Polymarket) briefly lag right after a surprising goal.

This was built as part of the Omniverse Fund – AI/ML / Quant Intern assessment. The goal wasn’t to build a full exchange bot, but to demonstrate:

event-driven program design real-time data handling market-mapping logic basic trading decision rules clean modular Python structure What the Engine Does Here’s the high-level flow: A mock feed generates random football goals (instead of using a paid API). Every event goes through a normalizer so the structure is always consistent. The matcher assigns the goal to a synthetic market (ex: Juventus_Inter → MKT_Juventus_Inter). A mock price feed gives a temporary market price (simulating price lag). The trader checks: Was the scoring team the underdog? Is the price still mispriced (< 0.50)? If yes → it logs a BUY trade. Everything is logged cleanly to the terminal. The engine is completely modular, so any part can later be replaced with a real API.

How to Run the Project:

Install the only dependency:

pip install websocket-client

Run the engine:

python main.py

You will start seeing real-time goal events like:

EVENT: Juventus_Inter (1–1) | Scorer: Juventus Underdog scored → BUY | Price=0.33 | Size=20

This runs the system end-to-end using only local Python files — no external APIs are required.

Folder Structure: main.py → entry point mock_feed.py → generates goal events normalizer.py → cleans/standardizes event matcher.py → assigns markets + probabilities market.py → small helper class price_feed.py → returns a simulated market price trader.py → decision engine (BUY / NO TRADE) config.py → basic settings utils.py → logger helper index.html → submission webpage (for Omniverse) logs/ → output logs README.md → project documentation

Sample Output:

Below is an actual output from one of the test runs:

Goal: Juventus 1-1 Inter | Juventus EVENT RECEIVED: Juventus_Inter | Score: (1,1) Trader: Underdog scored → BUY Order executed | market=MKT_Juventus_Inter | size=20 | price=0.33

Another case where the trader does not buy:

Goal: Arsenal 0-1 Chelsea | Chelsea Trader: No trade | favorite scored | price=0.61
