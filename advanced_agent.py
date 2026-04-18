"""
Advanced Finance Agent with Expert Analysis

This module provides an advanced version of the finance agent with
additional capabilities for deeper expert analysis and review collection.
"""

import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.websearch import WebSearchTools

# Load environment variables from .env file
load_dotenv()

# Advanced instructions with detailed expert analysis requirements
advanced_instructions = """
You are a world-class financial analyst and investment researcher with expertise in:
- Fundamental analysis and financial statement analysis
- Technical analysis and market trends
- Macroeconomic factors and their impact on markets
- Industry and competitive analysis
- Expert consensus and institutional perspectives

Analysis Process:

1. DATA COLLECTION
   - Gather current stock price, historical performance, and technical indicators
   - Collect key financial metrics: P/E ratio, EPS, dividend yield, debt-to-equity, ROE
   - Search for analyst reports and expert opinions from major investment banks,
     research firms, financial news outlets, and industry analysts

2. EXPERT ANALYSIS SYNTHESIS
   - Aggregate expert opinions and ratings
   - Identify consensus views and outliers
   - Find price targets from various analysts
   - Note recent upgrades/downgrades with explanations
   - Collect expert reasoning behind their ratings

3. COMPREHENSIVE REPORTING
   - Create structured analysis with clear sections
   - Use tables for data comparison where appropriate
   - Include both quantitative metrics and qualitative insights
   - Present balanced view with bull case AND bear case

4. SOURCES REQUIRED
   For each claim or analysis point, include:
   - Name of source/expert/firm
   - Date of publication when relevant
   - Analyst rating or recommendation when available
   - Keep source attribution simple and clear

REPORTING STRUCTURE:

STOCK OVERVIEW
- Current Price and Performance
- Market Cap and Trading Volume

KEY FINANCIAL METRICS
- Present in simple table format
- Include P/E, EPS, Revenue Growth, Profit Margin, ROE

EXPERT ANALYST CONSENSUS
- Overall Rating from analysts (Buy/Hold/Sell percentages)
- Price Targets and ranges
- Source: Mention analyst firms and institutions

BULLISH FACTORS (Why experts recommend it)
- Factor 1 with supporting source
- Factor 2 with supporting source
- Factor 3 with supporting source

BEARISH FACTORS (Concerns and risks)
- Risk 1 with supporting source
- Risk 2 with supporting source
- Risk 3 with supporting source

RECENT NEWS AND DEVELOPMENTS
- Important news items with dates
- Impact on stock price and sentiment
- Source references

INVESTMENT THESIS
- Key reasons institutions are investing or divesting
- Growth opportunities or challenges
- Competitive positioning

EXPERT RECOMMENDATIONS
- Specific analyst views and their reasoning
- Price target ranges
- Key catalyst events to watch

DISCLAIMER
This is informational content only. Not financial advice. Consult a registered financial advisor.

REQUIREMENTS:
1. Cite source for each major piece of information
2. Include publication dates for recent information
3. Only use published expert analysis and facts
4. Present information objectively without bias
5. Include at least 3-5 different expert sources when available
6. Keep formatting simple and clear
"""

# Create the advanced finance agent
advanced_agent = Agent(
    model=Groq(id="qwen/qwen3-32b"),
    tools=[YFinanceTools(), WebSearchTools()],
    instructions=advanced_instructions,
    markdown=True,
    show_tool_calls=False,  # Hide tool calls for cleaner output
)

def analyze_stock(ticker: str, focus: str = "general") -> None:
    """
    Analyze a stock with expert opinions and recommendations.
    
    Args:
        ticker: Stock symbol (e.g., 'AAPL')
        focus: Type of analysis - 'general', 'growth', 'value', 'dividend', 'risk'
    """
    
    focus_prompts = {
        "general": f"""
            Provide a comprehensive expert analysis for {ticker}:
            - Current price and market performance
            - Key financial metrics with expert commentary
            - Analyst consensus and ratings
            - Bullish and bearish factors according to experts
            - Recent news and developments
            - Investment considerations
            
            Include sources and expert opinions throughout.
        """,
        "growth": f"""
            Analyze {ticker} specifically for growth investing:
            - Revenue and earnings growth trajectory
            - What growth experts say about this stock
            - Competitive advantages and market position
            - Future catalysts for growth
            - Expert price targets and growth projections
            
            Include analyst links and sources.
        """,
        "value": f"""
            Analyze {ticker} from a value investing perspective:
            - Price to earnings, book value, and sales ratios
            - Expert views on valuation
            - Margin of safety assessment
            - Historical performance and trends
            - Expert opinions on value
            
            Include sources and analyst ratings.
        """,
        "dividend": f"""
            Analyze {ticker} as a dividend/income investment:
            - Current dividend yield
            - Dividend history and sustainability
            - Expert ratings for income investors
            - Payout ratio and financial health
            - Expert views on reliability
            
            Include expert sources and links.
        """,
        "risk": f"""
            Comprehensive risk analysis of {ticker}:
            - Identified risks by expert analysts
            - Business model vulnerabilities
            - Industry/market risks
            - Financial health indicators
            - Expert risk assessments and warnings
            
            Include expert sources and links.
        """
    }
    
    query = focus_prompts.get(focus, focus_prompts["general"])
    advanced_agent.print_response(query, stream=True)


def compare_stocks(tickers: list, criteria: str = "general") -> None:
    """
    Compare multiple stocks with expert analysis.
    
    Args:
        tickers: List of stock symbols (e.g., ['AAPL', 'MSFT', 'GOOGL'])
        criteria: Comparison criteria - 'general', 'growth', 'value', 'momentum'
    """
    
    ticker_str = ", ".join(tickers)
    
    query = f"""
    Compare {ticker_str} as investment options:
    
    For each company provide:
    1. Current stock price and recent performance
    2. Key financial metrics comparison
    3. Expert analyst ratings and recommendations
    4. Strengths and weaknesses per expert analysis
    5. Which expert opinions favor each stock
    
    Create comparison tables and include:
    - Source links for all information
    - Analyst consensus for each
    - Price targets and ratings
    
    Help me understand why experts would choose one over the others.
    """
    
    advanced_agent.print_response(query, stream=True)


if __name__ == "__main__":
    # Example usage - uncomment to run
    
    # General analysis
    # analyze_stock("AAPL")
    
    # Growth analysis
    # analyze_stock("NVDA", focus="growth")
    
    # Value analysis
    # analyze_stock("JNJ", focus="value")
    
    # Dividend analysis
    # analyze_stock("KO", focus="dividend")
    
    # Risk analysis
    # analyze_stock("COIN", focus="risk")
    
    # Compare stocks
    # compare_stocks(["NVDA", "AMD", "INTC"])
    
    pass
