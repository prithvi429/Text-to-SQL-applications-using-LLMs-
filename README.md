# Text-to-SQL Applications Using LLMs

AskSQL is a natural language interface that allows users to query structured databases using plain English. By leveraging Large Language Models (LLMs), such as Google's Gemini models, the application translates natural language questions into executable SQL queries, providing users with direct, intuitive access to data without requiring SQL knowledge.

## Features

- **Natural Language to SQL**: Converts plain English questions into SQL queries.
- **Database Integration**: Executes generated SQL queries on a SQLite database.
- **Streamlit Interface**: Provides an interactive web-based UI for users to input questions and view results.
- **Customizable Models**: Supports integration with Google Generative AI models like `gemini-pro`.

## Requirements

- Python 3.7 or higher
- A valid Google Generative AI API key
- SQLite database (`student.db`) with the following schema:
  - `name` (TEXT)
  - `class` (TEXT)
  - `section` (TEXT)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Text-to-SQL-applications-using-LLMs.git
   cd Text-to-SQL-applications-using-LLMs
   ```
