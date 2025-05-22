# AI-Agents
Financial Agent using LLaMA 3 and Phidata

This project demonstrates how to build an intelligent financial agent using the Phidata framework and the Groq-hosted LLaMA 3 model. The agent retrieves and compares real-time financial data like analyst recommendations and stock fundamentals using a combination of:

- LLaMA 3 via Groq
- Yahoo Finance Tool (`YFinanceTools`)
- Custom tool to map company names to ticker symbols


## Features

- Compare **analyst recommendations** and **fundamentals** for multiple companies
- Automatically converts known company names (e.g., "Phidata") into stock symbols
- Displays data in clean **markdown tables**
- Enables tool transparency with `show_tool_calls=True` and `debug_mode=True`

---

## What This Agent Can Do

Example input:
> Summarize and compare analyst recommendations and fundamentals for TSLA and phidata. Show in tables.

Output:
- Agent uses the `get_company_symbol` tool to resolve "Phidata" → `MSFT`
- Retrieves data for `TSLA` and `MSFT` via `YFinanceTools`
- Displays clean side-by-side comparisons in markdown

![image](https://github.com/user-attachments/assets/806cbefc-8720-4058-a88d-7fe6d89b757e)
