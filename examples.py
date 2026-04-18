"""
Example queries for the Agno Finance Agent

This file demonstrates various use cases and queries you can use
with the finance agent to get expert analysis and reviews.
"""

from Finance_Agent import agent

# Example 1: Comprehensive Stock Analysis
def example_1_stock_analysis():
    print("=" * 80)
    print("EXAMPLE 1: Comprehensive Stock Analysis")
    print("=" * 80)
    
    query = """
    Provide a comprehensive investment analysis for Tesla Inc. (TSLA) including:
    1. Current stock price and 52-week performance
    2. Key financial metrics (P/E ratio, EPS, growth rates)
    3. Expert analyst reviews and investment ratings
    4. Recent news, earnings reports, and company developments
    5. Investment considerations (bullish and bearish factors)
    
    Please include sources for all information.
    """
    agent.print_response(query, stream=True)


# Example 2: Comparing Two Companies
def example_2_company_comparison():
    print("\n" + "=" * 80)
    print("EXAMPLE 2: Stock Comparison with Expert Analysis")
    print("=" * 80)
    
    query = """
    Compare NVIDIA (NVDA) and AMD (AMD) as investment options:
    1. Compare their stock prices and market performance
    2. Financial metrics comparison (P/E, EPS, revenue growth)
    3. Expert analyst opinions for each company
    4. Recent developments and news for both companies
    5. Which factors would favor each company from an investment perspective
    
    Include sources for all analysis.
    """
    agent.print_response(query, stream=True)


# Example 3: Quick Investment Decision Support
def example_3_quick_analysis():
    print("\n" + "=" * 80)
    print("EXAMPLE 3: Quick Investment Decision Support")
    print("=" * 80)
    
    query = """
    I'm considering investing in Microsoft (MSFT). Give me:
    1. Current price and recent performance trend
    2. Key reasons expert analysts are bullish/bearish
    3. Any recent controversies or positive developments
    4. Top 3 bullish factors and top 3 bearish factors
    
    Include sources and expert opinion links.
    """
    agent.print_response(query, stream=True)


# Example 4: Sector Analysis with Expert Reviews
def example_4_sector_analysis():
    print("\n" + "=" * 80)
    print("EXAMPLE 4: Sector Analysis with Expert Reviews")
    print("=" * 80)
    
    query = """
    Analyze the electric vehicle sector. Focus on:
    1. Top companies (Tesla, Lucid, Rivian) - current prices and performance
    2. Expert analyst consensus on EV sector growth
    3. Key drivers and headwinds for the sector
    4. Which companies have the most positive expert reviews
    5. Market sentiment and recent news
    
    Include all sources and expert opinions.
    """
    agent.print_response(query, stream=True)


# Example 5: Dividend Stock Analysis
def example_5_dividend_analysis():
    print("\n" + "=" * 80)
    print("EXAMPLE 5: Dividend Stock Analysis")
    print("=" * 80)
    
    query = """
    Analyze Johnson & Johnson (JNJ) as a dividend income investment:
    1. Current stock price and dividend yield
    2. Company fundamentals and financial health
    3. Expert analyst ratings for income investors
    4. Historical dividend payment consistency
    5. Risks and opportunities
    
    Include expert sources and analyst recommendations.
    """
    agent.print_response(query, stream=True)


# Example 6: Growth Stock Analysis
def example_6_growth_analysis():
    print("\n" + "=" * 80)
    print("EXAMPLE 6: Growth Stock Analysis")
    print("=" * 80)
    
    query = """
    Analyze Shopify (SHOP) as a growth stock opportunity:
    1. Current stock price and recent trends
    2. Revenue and earnings growth rates
    3. What expert investors say about Shopify's growth potential
    4. Competition and market positioning
    5. Future outlook based on expert analysis
    
    Include all sources and expert opinions.
    """
    agent.print_response(query, stream=True)


# Example 7: Value Stock Analysis
def example_7_value_analysis():
    print("\n" + "=" * 80)
    print("EXAMPLE 7: Value Stock Analysis")
    print("=" * 80)
    
    query = """
    Analyze Bank of America (BAC) from a value investing perspective:
    1. Current price relative to book value and earnings
    2. Key financial metrics for value assessment
    3. Expert opinion on whether it's undervalued
    4. Historical performance and dividend history
    5. Risks and recovery potential
    
    Include expert analyst links and sources.
    """
    agent.print_response(query, stream=True)


# Example 8: Risk Assessment with Expert Analysis
def example_8_risk_analysis():
    print("\n" + "=" * 80)
    print("EXAMPLE 8: Risk Assessment with Expert Analysis")
    print("=" * 80)
    
    query = """
    For Cryptocurrency stocks (like Coinbase - COIN):
    1. Current price and volatility metrics
    2. Key risks identified by expert analysts
    3. Regulatory concerns and expert perspectives
    4. Adoption trends and growth potential
    5. Is this an appropriate investment for each risk profile
    
    Include expert sources and risk assessments.
    """
    agent.print_response(query, stream=True)


if __name__ == "__main__":
    # Run all examples
    # Uncomment the examples you want to run
    
    # example_1_stock_analysis()
    # example_2_company_comparison()
    # example_3_quick_analysis()
    # example_4_sector_analysis()
    # example_5_dividend_analysis()
    # example_6_growth_analysis()
    # example_7_value_analysis()
    # example_8_risk_analysis()
    
    # Or run a custom query:
    custom_query = """
    Analyze Apple Inc. (AAPL) including:
    1. Stock price and recent performance
    2. Competitive advantages and moat
    3. Expert analyst ratings and price targets
    4. Recent product launches and company news
    5. Investment thesis: Why invest or why not
    
    Include sources for all recommendations.
    """
    agent.print_response(custom_query, stream=True)
