# Week 7 – SQL

**Focus:** Working with relational databases using SQL for querying, filtering, and joining data.

This week introduces:
- Writing SQL statements (`SELECT`, `WHERE`, `ORDER BY`, `JOIN`)
- Understanding relational models (tables, primary keys, foreign keys)
- Extracting insights from structured data
- Applying basic data analysis techniques using SQL

## 🧠 Heuristics to Extract

- SQL is about **asking the right question** — clarity of query reflects clarity of thought  
- Use filtering (`WHERE`) before sorting (`ORDER BY`) for cleaner logic  
- Always alias your tables for clarity in multi-joins  
- Normalize tables to avoid redundancy, but denormalize carefully for read performance  
- Use joins when thinking in **relationships**, not rows

## 📂 Problems Covered

- `001-movies.md`: Practice querying a movie database — selecting, sorting, and filtering with SQL basics.

## 🗃️ Notes

SQL may feel rigid at first, but it forces precision in thinking and rewards you with powerful insights from even simple datasets.

It also serves as a **lingua franca** for data access across almost all major systems — AI pipelines, backend services, analytics dashboards, and more.

## 📎 Resources

- [CS50 Week 7 Lecture](https://cs50.harvard.edu/x/2023/weeks/7/)  
- [SQL Zoo](https://sqlzoo.net/)  
- [SQLite CLI Tool](https://sqlite.org/cli.html)  
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/) *(if planning to scale beyond SQLite)*