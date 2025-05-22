from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv



load_dotenv()
"""
#agent will use this docstring from Yfinancetools functions and give it 
LLM. Hey LLM if you need to use this function this is the purpose
LLM can understands well and map it to the intent of the user query

Agent works based on the model
websearch in chatgpt is an agent, perplexity - uses agent
customise the your own tools using phidata

#openai will figure out when llama takes companynname still as phidata
"""


def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"), #contains static knowledge
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use Tables to display data",
                  "If you need to find the symbol for a company, use the get_company_symbol tool.",
    ],
    debug_mode=True

)

agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for TSLA and phidata. Show in tables."
)


