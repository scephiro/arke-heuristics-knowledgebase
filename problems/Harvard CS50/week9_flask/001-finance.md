---
id: "CS50-W9-001"
title: "Finance"
source: "CS50"
difficulty: "Hard"
tags: ["flask", "python", "backend", "api", "sessions", "jinja", "sql"]
core_problem: "Build a full-stack stock trading app with user registration, lookup, buy/sell, and transaction history"
status: "complete"
---

## 🧩 Problem Summary

Build a Flask web app that lets users:

- Register and log in securely
- Look up real-time stock quotes via API
- Buy and sell stocks with balance tracking
- View transaction history
- See portfolio overview with current prices

The app must manage user sessions, database state, real-time updates, and error handling — all via Flask and SQLite.

---

## 🔄 Initial Approach

- Set up project structure (`app.py`, `templates/`, `static/`, `helpers.py`)  
- Implement user registration/login with password hashing  
- Connect to external stock API for real-time prices  
- Track transactions and balances using SQLite  
- Render portfolio via Jinja templates

---

## ✅ Optimal Strategy

- Modularize helpers (API access, price formatting, validation) in `helpers.py`  
- Use sessions for login state; don’t rely on URL-based auth  
- Always validate and sanitize form inputs (both client and server-side)  
- Make use of CS50’s `check50` test cases to verify logic and edge cases  
- Use database **transactions** or atomic logic to avoid race conditions (e.g. double purchases)

---

## 🧠 Heuristics & Insights

- **Treat web routes like logic gates** — each path has clear preconditions and side effects  
- Sessions allow state without bloated URLs or hidden fields  
- Templating requires careful separation of logic (`app.py`) and layout (`.html`)  
- **Guard every decision with validation**: funds, stock symbol, share quantity  
- Use decorators or helper functions for repeated checks (e.g. login_required)

---

## ⚠️ Common Pitfalls

- Updating portfolio without reflecting live prices  
- Failing to handle float rounding errors in currency (use `decimal.Decimal`)  
- Incomplete input checks (e.g. negative shares, invalid symbols)  
- Forgetting to hash passwords (security flaw!)  
- Mishandling SQLite constraints or schema changes

---

## 🧭 Meta Insight

This is where web dev gets *real* — you’re not just coding, you're **managing users, money, and live data**.

You learn to:
- Control app state across requests
- Combine UI, logic, and storage seamlessly
- Think in user stories, not just functions

This is a **foundational problem** for future full-stack apps, product dashboards, and AI-enhanced interfaces.

---

## 🔍 References

- [CS50 Finance Spec](https://cs50.harvard.edu/x/2023/psets/9/finance/)  
- Flask Docs — https://flask.palletsprojects.com/  
- Jinja2 Templating — https://jinja.palletsprojects.com/  
- SQLite Transactions — https://sqlite.org/lang_transaction.html  
- Password Hashing (Werkzeug) — https://werkzeug.palletsprojects.com/en/3.0.x/utils/#werkzeug.security.generate_password_hash