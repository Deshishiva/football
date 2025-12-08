# Goal Shock Trader

This project is a small prototype of a goal-reaction trading engine.

The idea is simple: when a football match goal happens, the system checks if the scoring team is the underdog. If yes, it triggers a simulated “BUY” signal, based on the assumption that real markets (like Kalshi or Polymarket) briefly lag right after a surprising goal.

This project was built as part of the  Omniverse Fund – AI/ML / Quant Intern assessment.  
The goal was not to build a full exchange bot, but to demonstrate clean, production-style system design focused on real-time decision making.

---

## What This Project Demonstrates

- Event-driven program design  
- Near real-time data handling  
- Market-mapping logic  
- Simple, explainable trading rules  
- Clean, modular Python architecture  

Each part of the system is isolated so it can be replaced with real APIs later.

---

## High-Level Workflow

1. A mock or live feed generates football goal events  
2. Each event is normalized into a clean structure  
3. The matcher assigns the event to a synthetic in-play market  
   (example: `Juventus_Inter → MKT_Juventus_Inter`)  
4. A market ticker or price feed provides the current probability  
5. The trader evaluates:
   - Did the **underdog** score?
   - Is the market probability still **below 0.50**?
6. If both are true → a simulated **BUY** order is placed  
7. All activity is logged clearly to the terminal  

---

## How to Run the Project

### Install dependencies
```bash
pip install websocket-client requests
