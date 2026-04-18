"""
Safe Example Queries - Without Streaming (No Markdown Errors)

This file demonstrates safe example queries that avoid markdown parsing errors.
All examples have stream=True REMOVED - they just print the response when done.

Use this file if you're getting markdown parsing errors from examples.py
"""

from Finance_Agent import agent

# Example 1: Simple Stock Analysis
def example_1_simple_analysis():
    print("=" * 80)
    print("EXAMPLE 1: Simple Stock Analysis")
    print("=" * 80)
    
    query = """
    Analyze Apple Inc. (AAPL):
    1. What is the current stock price?
    2. What are key financial metrics?
    3. What do experts think about it?
    4. What are the risks?
    
    Keep it concise.
    """
    print("\n⏳ Running analysis (this may take 30-60 seconds)...\n")
    agent.print_response(query)
    print("\n")


# Example 2: Quick Price Check
def example_2_quick_price():
    print("=" * 80)
    print("EXAMPLE 2: Quick Stock Price and News")
    print("=" * 80)
    
    query = """
    What is the current stock price and recent news for Tesla (TSLA)?
    Keep the response short and factual.
    """
    print("\n⏳ Checking price and news...\n")
    agent.print_response(query)
    print("\n")


# Example 3: Expert Opinion
def example_3_expert_opinion():
    print("=" * 80)
    print("EXAMPLE 3: What Experts Say About Microsoft")
    print("=" * 80)
    
    query = """
    What do investment experts and analysts say about Microsoft (MSFT)?
    What are they saying about buying or not buying it?
    """
    print("\n⏳ Gathering expert opinions...\n")
    agent.print_response(query)
    print("\n")


# Example 4: Financial Metrics
def example_4_metrics():
    print("=" * 80)
    print("EXAMPLE 4: Financial Metrics for NVIDIA")
    print("=" * 80)
    
    query = """
    Show me the key financial metrics for NVIDIA (NVDA):
    - P/E ratio
    - EPS
    - Revenue growth
    - Profit margins
    
    What do these metrics tell us about the company?
    """
    print("\n⏳ Fetching financial metrics...\n")
    agent.print_response(query)
    print("\n")


# Example 5: Compare Two Stocks
def example_5_compare():
    print("=" * 80)
    print("EXAMPLE 5: Compare NVIDIA vs AMD")
    print("=" * 80)
    
    query = """
    Compare NVIDIA (NVDA) and AMD (AMD):
    - Which has better financial metrics?
    - Which do experts prefer?
    - Which would be better for an investor?
    """
    print("\n⏳ Comparing stocks...\n")
    agent.print_response(query)
    print("\n")


# Example 6: Dividend Stock
def example_6_dividend():
    print("=" * 80)
    print("EXAMPLE 6: Dividend Income - Johnson & Johnson")
    print("=" * 80)
    
    query = """
    Is Johnson & Johnson (JNJ) a good dividend stock?
    What is the dividend yield?
    Is it sustainable?
    What do experts say about it as an income investment?
    """
    print("\n⏳ Analyzing dividend potential...\n")
    agent.print_response(query)
    print("\n")


# Example 7: Growth Stock
def example_7_growth():
    print("=" * 80)
    print("EXAMPLE 7: Growth Potential - Shopify")
    print("=" * 80)
    
    query = """
    Is Shopify (SHOP) a good growth stock?
    What is the revenue growth rate?
    What do experts say about its growth potential?
    What could stop it from growing?
    """
    print("\n⏳ Analyzing growth potential...\n")
    agent.print_response(query)
    print("\n")


# Example 8: Risk Analysis
def example_8_risks():
    print("=" * 80)
    print("EXAMPLE 8: Risk Analysis - Risky Stocks")
    print("=" * 80)
    
    query = """
    What are the main risks for a beginner investor considering:
    - Tesla (TSLA)
    - Cryptocurrency stocks like Coinbase (COIN)
    - Tech growth stocks
    
    What should I worry about?
    """
    print("\n⏳ Analyzing investment risks...\n")
    agent.print_response(query)
    print("\n")


# MAIN EXECUTION
if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "  🔧 SAFE EXAMPLES - NO STREAMING (No Markdown Errors)".ljust(77) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")
    print("""
    These examples do NOT use stream=True, which prevents markdown parsing errors.
    Responses may take 30-60 seconds each.
    
    INSTRUCTIONS:
    1. Uncomment ONE example below (remove the # mark)
    2. Run: python examples_safe.py
    3. Wait for the response
    4. See results without markdown errors!
    
    Start with Example 1 or 2 if this is your first time.
    """)
    print("=" * 80)
    
    # UNCOMMENT ONE EXAMPLE TO RUN:
    # ────────────────────────────────────────────────────────────────
    
    # example_1_simple_analysis()           # Recommended: Start here
    # example_2_quick_price()               # Quick price check
    # example_3_expert_opinion()            # What experts say
    # example_4_metrics()                   # Financial metrics
    # example_5_compare()                   # Compare 2 stocks
    # example_6_dividend()                  # Dividend analysis
    # example_7_growth()                    # Growth analysis
    # example_8_risks()                     # Risk analysis
    
    # ────────────────────────────────────────────────────────────────
    # For now, run a simple demo:
    print("\n⏳ DEMO: Running a quick example...\n")
    
    demo_query = """
    What is the current stock price of Apple (AAPL)?
    What is the P/E ratio?
    Is it overvalued or undervalued?
    """
    agent.print_response(demo_query)
    
    print("\n" + "=" * 80)
    print("✅ DEMO COMPLETE!")
    print("=" * 80)
    print("""
    If you see this without errors, your agent is working!
    
    To run other examples:
    1. Open this file in your text editor
    2. Find the "UNCOMMENT ONE EXAMPLE" section
    3. Remove the # from an example line
    4. Run: python examples_safe.py
    
    Try example_5_compare() to compare two stocks!
    """)
    print("=" * 80)
