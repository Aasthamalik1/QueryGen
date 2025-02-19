# QueryGEN: Natural Language to SQL Converter

This project allows users to input SQL queries written in natural language, and converts them into actual SQL queries using a large language model (LLM).
It then executes the generated SQL query against a database and returns the result.

## Features

- Convert natural language questions into SQL queries.
- Execute the generated SQL queries against a configured database.
- Supports multiple types of SQL queries (SELECT, INSERT, UPDATE, DELETE).
- User-friendly interface for querying databases using natural language.

## Installation

### Prerequisites
Before installing, make sure you have the following dependencies:
- Python 3.x
- A running database (e.g., MySQL, PostgreSQL, SQLite)

### Steps to Install

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Aasthamalik1/QueryGen
   cd QueryGen
   python -m venv venv
   On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt



