---
id: "CS50-W8-001"
title: "Homepage"
source: "CS50"
difficulty: "Easy"
tags: ["html", "css", "javascript", "web", "dom", "events"]
core_problem: "Build a basic personal homepage using HTML, CSS, and JavaScript"
status: "complete"
---

## 🧩 Problem Summary

Create a multi-section homepage using:
- **HTML** to structure content
- **CSS** to style it cleanly and responsively
- **JavaScript** to add minimal interactivity (e.g. alerts, DOM updates)

The goal is not to build something complex, but to demonstrate:
- Clean HTML semantics
- Thoughtful CSS layout and color use
- Functional, minimal JavaScript behavior

---

## 🔄 Initial Approach

- Use semantic HTML elements (`<header>`, `<nav>`, `<main>`, `<footer>`)  
- Style with CSS to improve layout, font, and color consistency  
- Add a simple JS script — for example, a "click me" button that changes text or background  
- Use class names for consistent styling and reuse

Example JS:
```javascript
document.getElementById("btn").onclick = function() {
  document.body.style.backgroundColor = "lightblue";
};
```

---

## ✅ Optimal Strategy

- Keep HTML clean and accessible — use proper nesting and alt text  
- Separate CSS and JS into external files for maintainability  
- Use flexbox or grid for layout instead of manual margins  
- Limit JavaScript to clear, declarative interactions  
- Add light responsiveness using media queries

---

## 🧠 Heuristics & Insights

- Structure before style — make sure the raw HTML makes sense before you beautify it  
- CSS rules **cascade** — the last matching rule wins  
- JavaScript behavior should be **progressive enhancement** — not essential to core functionality  
- Don’t mix inline CSS/JS unless you’re prototyping  
- Accessibility and semantic structure help both users *and* automated systems interpret your page

---

## ⚠️ Common Pitfalls

- Misusing divs instead of semantic elements  
- Over-styling: redundant or conflicting CSS rules  
- Forgetting to link external CSS/JS files properly  
- Poor layout strategy leading to brittle designs  
- Adding JS before DOM is loaded — use `defer` or `DOMContentLoaded` event

---

## 🧭 Meta Insight

This project reveals how **code affects humans** — the user sees the *interface*, not the logic.

It also lays the foundation for:
- **Component-based UI design**
- **Stateful interactions**
- **Browser-native automation**

These are essential for modern web frameworks, assistant interfaces, and full-stack development.

---

## 🔍 References

- CS50 Week 8 — https://cs50.harvard.edu/x/2023/weeks/8/  
- HTML Semantic Tags — https://developer.mozilla.org/en-US/docs/Glossary/Semantics#semantics_in_html  
- CSS Flexbox Guide — https://css-tricks.com/snippets/css/a-guide-to-flexbox/  
- JavaScript DOM Intro — https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction