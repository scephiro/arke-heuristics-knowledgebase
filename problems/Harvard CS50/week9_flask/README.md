# Week 9 – Flask

**Focus:** Introduction to server-side development using **Flask**, a lightweight Python web framework.

This week covers:
- Building dynamic web apps with **routes**, **forms**, and **templating**
- Handling **sessions**, **user input**, and **data persistence**
- Creating full-stack experiences by connecting front-end and back-end logic

---

## 🧠 Heuristics to Extract

- Flask apps are **request-driven** — every route handles a specific HTTP method (GET/POST)  
- The web is **stateless** — sessions and cookies are how you maintain continuity  
- Use templating (Jinja) to avoid duplicating HTML and dynamically inject variables  
- Separate logic from presentation — views shouldn’t handle heavy computation  
- Always validate user input before processing or storing it  
- Think of the app as a **flow of requests**, not just code

---

## 🔬 Deep-Dive Relevance

### 🤖 AI / Assistant Applications
- AI copilots or code assistants need to understand **state management**, **request/response flow**, and **template rendering** to write or debug web apps  
- Smart agents that interface with Flask-based APIs benefit from knowing its routing and form processing model  
- Many lightweight AI tools, dashboards, and visualizations are built using Flask — understanding it unlocks rapid prototyping

### 🧱 Enterprise Use
- Flask is often used for **microservices**, admin tools, dashboards, and data visualization  
- It’s Python-native, making it compatible with AI models, ML pipelines, and internal tooling  
- Knowing when to use Flask (vs. Django/FastAPI) is part of architectural decision-making

### ⚙️ Automation & Design Insights
- Templates = dynamic UI generation  
- Sessions = lightweight user modeling  
- Route design = how you structure product features

This is where the code **meets business logic**.

---

## 📂 Problems Covered

- `001-finance.md`: Build a stock trading web app with user registration, quote fetching, and transaction history.

---

## 🗃️ Notes

This week is where **everything converges**: UI, database, user behavior, and server logic.

It pushes you to think in **end-to-end systems**, not just code snippets. You must handle edge cases, UX, and data integrity — all while keeping the code modular.

---

## 📎 Resources

- [CS50 Week 9 Lecture](https://cs50.harvard.edu/x/2023/weeks/9/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Templating](https://jinja.palletsprojects.com/)
- [WTForms (for input validation)](https://wtforms.readthedocs.io/en/3.0.x/)