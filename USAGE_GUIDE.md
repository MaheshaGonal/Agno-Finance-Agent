# 📖 Agno Finance Agent - Complete Usage Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Getting Started](#getting-started)
3. [Basic Usage](#basic-usage)
4. [Advanced Usage](#advanced-usage)
5. [Query Examples](#query-examples)
6. [Tips & Best Practices](#tips--best-practices)
7. [Understanding the Output](#understanding-the-output)
8. [Customization](#customization)
9. [FAQ](#faq)

---

## Prerequisites

### Before You Start:
1. ✅ Python 3.8 or higher installed
2. ✅ Groq API key (get free at https://console.groq.com)
3. ✅ Internet connection
4. ✅ Dependencies installed (`pip install -r requirements.txt`)

### Setup Checklist:
```bash
# 1. Create .env file
cp .env.example .env

# 2. Edit .env with your Groq API key
# GROQ_API_KEY=your-key-here

# 3. Install dependencies
pip install -r requirements.txt

# 4. Test it works
python Finance_Agent.py
```

---

## Getting Started

### Option 1: Run the Default Agent

```bash
python Finance_Agent.py
```

This runs a pre-configured query analyzing Apple Inc. (AAPL).

### Option 2: Run Interactive Analysis

```python
from Finance_Agent import agent

# Ask any stock analysis question
agent.print_response("What is your investment view on Microsoft (MSFT)?")
```

### Option 3: Use Examples

```bash
python examples.py
```

Then uncomment your desired example in the file.

### Option 4: Advanced Agent

```python
from advanced_agent import analyze_stock

# Specialized analysis
analyze_stock("NVDA", focus="growth")
```

---

## Basic Usage

### Simple Stock Analysis

```python
from Finance_Agent import agent

query = "Tell me about Tesla (TSLA) as an investment"
agent.print_response(query)
```

### What You'll Get:
✅ Current stock price  
✅ Key financial metrics  
✅ Expert analyst opinions  
✅ Pros (bullish factors)  
✅ Cons (bearish factors)  
✅ Recent news and developments  
✅ Links to sources  

---

## Advanced Usage

### 1. Growth Stock Analysis

```python
from advanced_agent import analyze_stock

# Analyze growth potential
analyze_stock("SHOPIFY", focus="growth")
```

**Best for**: Investors looking for companies with fast revenue growth

### 2. Value Stock Analysis

```python
# Find undervalued stocks
analyze_stock("BERKSHIRE_B", focus="value")
```

**Best for**: Investors looking for bargains below intrinsic value

### 3. Dividend Stock Analysis

```python
# Income-focused analysis
analyze_stock("JNJ", focus="dividend")
```

**Best for**: Income investors seeking regular dividend payments

### 4. Risk Assessment

```python
# Deep risk analysis
analyze_stock("COIN", focus="risk")
```

**Best for**: Understanding investment risks and volatility

### 5. Compare Multiple Stocks

```python
from advanced_agent import compare_stocks

# Side-by-side expert analysis
compare_stocks(["AAPL", "MSFT", "GOOGL"])
```

**Best for**: Choosing between similar investment options

---

## Query Examples

### 📊 Financial Analysis Queries

```
"What are the key financial metrics for Apple (AAPL)? Include P/E ratio, EPS, and growth rates."

"Compare the profitability of Microsoft and Google. Which is more profitable and why?"

"Is Tesla overvalued? Show me valuation metrics and expert opinions."
```

### 💼 Expert Opinion Queries

```
"What do major investment banks say about Nvidia (NVDA)? Include analyst ratings and price targets."

"Find expert analyst consensus on Amazon (AMZN). Are experts bullish or bearish?"

"What are Wall Street's latest recommendations for Meta (META)?"
```

### 📈 Trend & News Queries

```
"What are the latest developments for Apple? Any recent news that affects the stock?"

"How has Tesla (TSLA) performed recently? What's driving the price movement?"

"What industry trends affect semiconductor stocks like Intel (INTC)?"
```

### 🎯 Decision-Making Queries

```
"Should I invest in Microsoft? Give me 3 bullish reasons and 3 bearish reasons."

"I'm comparing Apple and Microsoft. Which does expert analysis favor for long-term growth?"

"Is now a good time to buy Coca-Cola (KO) for dividends? Check current valuation and expert views."
```

### 🔍 Deep Dive Queries

```
"Provide comprehensive analysis of Nvidia (NVDA):
1. Financial health and profitability
2. Growth prospects according to experts
3. Competition in AI chip market
4. What could derail the stock
5. Expert price targets and ratings

Include sources."
```

### 💰 Sector Analysis

```
"Compare the E-V sector leaders: Tesla, Lucid, and Rivian. Which has the best expert consensus?"

"Analyze the cloud computing sector: AWS (Amazon), Azure (Microsoft), and Google Cloud. Which is best?"

"Which semiconductor stocks do experts rate highest? Nvidia, AMD, Intel, or Qualcomm?"
```

### 🎓 Learning Queries

```
"Explain what P/E ratio means and why it matters for stock selection."

"What does ROE (Return on Equity) tell us about a company? Give examples."

"Why do some stocks pay dividends while others don't?"
```

---

## Tips & Best Practices

### ✅ Best Practices

1. **Be Specific**: Include ticker symbol in CAPS (AAPL, not Apple)
2. **Clear Intent**: State what you want to know
3. **Include Time Context**: "Recent developments", "Last quarter earnings", etc.
4. **Request Sources**: Always ask for sources and links
5. **Multiple Perspectives**: Ask for both bullish and bearish views
6. **Use Focus Areas**: If comparing, specify what to compare on

### ❌ Avoid

1. ❌ Vague queries: "Tell me about stocks"
2. ❌ Asking for buy/sell recommendations (agent doesn't do this)
3. ❌ Expecting real-time data on very new companies
4. ❌ Asking for information beyond the agent's scope
5. ❌ Very long, complex queries (break into parts)

### 💡 Pro Tips

```python
# Tip 1: Get trending stocks analysis
query = "What stocks are trending on Wall Street right now? Which do experts like most?"

# Tip 2: Deep dive into specific aspect
query = "Focus only on the valuation of Microsoft (MSFT). Is it cheap or expensive right now?"

# Tip 3: Catalyst analysis
query = "What upcoming catalysts could affect Apple (AAPL) stock? From earnings to product launches."

# Tip 4: Comparison framework
query = "Compare growth rate, profitability, and valuation of NVDA vs AMD. Table format please."

# Tip 5: Expert consensus
query = "Create a summary of what the top 10 analysts say about Tesla (TSLA). Include price targets."
```

---

## Understanding the Output

### Report Structure

```
📊 STOCK OVERVIEW
├─ Current Price & Performance
└─ Market Cap & Trading Volume

💰 KEY FINANCIAL METRICS
├─ P/E Ratio
├─ EPS
├─ Revenue Growth
└─ Profit Margin

📈 EXPERT ANALYST CONSENSUS
├─ Overall Rating
├─ Price Targets
└─ Source Links

✅ BULLISH FACTORS
├─ Growth opportunity
├─ Strong market position
└─ Expert support

⚠️ BEARISH FACTORS
├─ High valuation
├─ Competition
└─ Regulatory risks

📰 RECENT NEWS & DEVELOPMENTS
└─ Latest updates with sources

🎯 INVESTMENT THESIS
└─ Summary of key investment case
```

### Interpreting Analyst Ratings

- **Buy/Overweight**: Most analysts believe stock will outperform
- **Hold/Neutral**: Analysts see limited upside or downside
- **Sell/Underweight**: Analysts believe stock will underperform
- **Strong Buy**: Highest conviction bullish rating
- **Strong Sell**: Highest conviction bearish rating

### Financial Metrics Explained

| Metric | What It Means | Generally Better |
|--------|---------------|------------------|
| P/E Ratio | Price vs Earnings | Lower = Cheaper |
| EPS | Earnings per Share | Higher = Better |
| ROE | Return on Equity | Higher = Better |
| Debt/Equity | Financial Leverage | Lower = Safer |
| Dividend Yield | Annual Return from Dividends | Higher = More Income |

---

## Customization

### Modify Agent Behavior

Edit `config.py` to customize:

```python
# Change model (faster vs more powerful)
GROQ_MODEL = "qwen/qwen3-32b"  # Fast
GROQ_MODEL = "qwen/qwen3-72b"  # More powerful

# Change analysis type
DEFAULT_ANALYSIS_TYPE = "growth"  # or "value", "dividend", etc.

# Add custom sources
PREFERRED_SOURCES["custom"] = ["Your Favorite Analyst", ...]

# Customize metrics to focus on
IMPORTANT_METRICS["custom"] = ["Custom Metric 1", "Custom Metric 2"]
```

### Create Custom Instructions

Edit `Finance_Agent.py` to change the analysis instructions:

```python
custom_instructions = """
You are focused on [your specific goal].
Include [specific sources].
Emphasize [specific metrics].
"""

agent = Agent(
    model=Groq(id="qwen/qwen3-32b"),
    tools=[YFinanceTools(), WebSearchTools()],
    instructions=custom_instructions,
    markdown=True,
)
```

---

## FAQ

### ❓ How do I get a Groq API key?

1. Go to https://console.groq.com
2. Sign up for free
3. Copy your API key
4. Add to `.env`: `GROQ_API_KEY=your-key-here`

### ❓ Why is the agent not finding information?

**Check:**
- Internet connection working
- API key is valid
- Stock ticker is correct (use uppercase: AAPL not Apple)
- Stock exists and has analyst coverage

### ❓ Can I use this for day trading?

**Not ideal for:**
- This agent provides fundamental analysis
- Better for medium to long-term investing (1+ year)
- For day trading, use technical analysis tools

### ❓ How accurate is the information?

**Remember:**
- All information comes from public sources
- Historical data is accurate
- Expert opinions are real but subjective
- Always verify important information
- Consult a licensed advisor for major decisions

### ❓ Can I compare more than 3 stocks?

**Yes**, but:
- 2-3 stocks gives clearer comparison
- More stocks = more complex output
- Try multiple pairwise comparisons

### ❓ How long does analysis take?

**Typical times:**
- Quick query: 10-30 seconds
- Full analysis: 1-2 minutes
- Complex comparison: 2-5 minutes

### ❓ How often should I update my analysis?

**Suggested:**
- Growth stocks: Weekly (fast moving)
- Value stocks: Monthly (slower moving)
- Dividend stocks: Quarterly (around earnings)
- Quick checks: As needed

### ❓ Can I get email alerts?

**Not built-in**, but you could:
- Run the agent on a schedule
- Save results to a file
- Send via email script

### ❓ What's the difference between the basic and advanced agent?

| Feature | Basic | Advanced |
|---------|-------|----------|
| Stock Analysis | ✅ | ✅ |
| Expert Reviews | ✅ | ✅ |
| Focused Analysis | ❌ | ✅ (Growth/Value/etc) |
| Comparison Tool | ❌ | ✅ |
| Deep Customization | ❌ | ✅ |

### ❓ How much does this cost?

**Free** (if using free Groq tier), but check:
- Groq's API limits
- Free tier rate limits
- Upgrade options if needed

---

## 🎯 Next Steps

1. **Start Simple**: Run `python Finance_Agent.py`
2. **Try Examples**: Run `python examples.py`
3. **Custom Query**: Ask about your favorite stock
4. **Go Advanced**: Try specialized analysis with `advanced_agent.py`
5. **Customize**: Modify `config.py` for your preferences
6. **Build**: Create your own analysis scripts

---

## 📞 Support & Feedback

If you have:
- **Questions**: Check FAQ section above
- **Issues**: Check API key and internet connection
- **Ideas**: Feel free to modify and extend the code
- **Problems**: Enable DEBUG_MODE in config.py

---

**Happy investing with AI-powered analysis! 📈**

Remember: This tool helps you research faster, but **always do your own due diligence** before investing.
