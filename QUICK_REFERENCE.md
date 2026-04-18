# 🚀 Agno Finance Agent - Quick Reference Card

## Installation (1 minute)

```bash
git clone <repo-url>
cd agno-finance-agent
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your GROQ_API_KEY
```

---

## 📌 Quick Start Commands

### Run Basic Agent
```bash
python Finance_Agent.py
```

### Run Examples
```bash
python examples.py
```

### Custom Query
```python
from Finance_Agent import agent
agent.print_response("What is your view on AAPL?")
```

### Growth Analysis
```python
from advanced_agent import analyze_stock
analyze_stock("NVDA", focus="growth")
```

### Compare Stocks
```python
from advanced_agent import compare_stocks
compare_stocks(["AAPL", "MSFT"])
```

---

## 🎯 Query Formulas

### Formula 1: Basic Analysis
```
"Analyze [TICKER] including:
1. Current price and performance
2. Key financial metrics
3. Expert analyst views
4. Bullish and bearish factors

Include sources."
```

### Formula 2: Valuation
```
"Is [TICKER] overvalued or undervalued?
- Show P/E ratio, P/B ratio
- Compare to industry average
- Expert valuation opinions
- Sources required"
```

### Formula 3: Comparison
```
"Compare [TICKER1] vs [TICKER2]:
- Price performance
- Financial metrics
- Expert preference
- Which is better for [your goal]

Include all sources."
```

### Formula 4: Decision Support
```
"Should I invest in [TICKER]?
- 3 bullish reasons (with sources)
- 3 bearish reasons (with sources)
- Expert consensus rating
- What experts focus on"
```

### Formula 5: News Check
```
"Latest news about [TICKER]:
- Recent developments
- Market impact
- Expert interpretation
- What changed in valuation/outlook"
```

---

## 📊 Analysis Modes

| Mode | Best For | Command |
|------|----------|---------|
| **General** | Overview | `analyze_stock("AAPL")` |
| **Growth** | Fast growing companies | `analyze_stock("NVDA", focus="growth")` |
| **Value** | Cheap stocks | `analyze_stock("JNJ", focus="value")` |
| **Dividend** | Income stocks | `analyze_stock("KO", focus="dividend")` |
| **Risk** | Risk assessment | `analyze_stock("COIN", focus="risk")` |

---

## 💡 Popular Queries

```python
# Tech Giants
agent.print_response("Analyze FAANG stocks: AAPL, MSFT, GOOGL, AMZN, NVDA. Which is best?")

# AI Plays
agent.print_response("Best AI stocks according to experts: NVDA, TSLA, MSFT")

# Value Picks
agent.print_response("Undervalued dividend stocks: JNJ, KO, PG. Expert analysis?")

# Growth Stocks
agent.print_response("High growth stocks: NVDA, SHOPIFY, TESLA. Analysis?")

# ETF Research
agent.print_response("Best sector ETFs? Compare tech, finance, healthcare ETFs with expert views")

# Market Trends
agent.print_response("What sectors do experts like this quarter? Tech, Finance, Healthcare?")
```

---

## 📈 Key Metrics Cheat Sheet

| Metric | Formula | Good Sign |
|--------|---------|-----------|
| **P/E Ratio** | Price ÷ Earnings | Lower than peers |
| **EPS** | Net Income ÷ Shares | Growing annually |
| **Revenue Growth** | YoY revenue increase | 10%+ annually |
| **Profit Margin** | Net Income ÷ Revenue | 15%+ for tech |
| **ROE** | Net Income ÷ Equity | 15%+ is good |
| **Debt-to-Equity** | Total Debt ÷ Equity | <1.5 is safer |
| **Dividend Yield** | Annual Dividend ÷ Price | 2-4% typical |
| **Free Cash Flow** | Operating CF - CapEx | Positive & growing |

---

## 🔗 Default Sources

The agent searches:
- Bloomberg, Reuters, MarketWatch, Yahoo Finance
- Goldman Sachs, Morgan Stanley, J.P. Morgan
- Morningstar, Seeking Alpha, Benzinga
- CNBC, Financial Times

---

## ⚡ Pro Tips

1. **Use UPPERCASE tickers**: AAPL not Apple
2. **Be specific**: "Last quarter earnings?" not "How is it?"
3. **Ask for sources**: Always include "Include sources" in query
4. **Time it right**: Run after market close (4:30 PM ET) for latest data
5. **Check dates**: Note publication dates of expert opinions
6. **Cross-reference**: Don't rely on single expert
7. **Screen size**: Use fullscreen terminal for better formatting

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| API Key error | Check `.env` file exists and has correct key |
| No results | Check internet, try simpler query, verify ticker |
| Slow response | Try "quick" analysis, use streaming mode |
| Too much output | Specify exactly what you want |
| Out of memory | Run one query at a time, restart if needed |

---

## 📂 File Guide

| File | Purpose |
|------|---------|
| `Finance_Agent.py` | Main agent - run this first |
| `advanced_agent.py` | Specialized analysis modes |
| `examples.py` | Pre-written query examples |
| `config.py` | Customization settings |
| `requirements.txt` | Python dependencies |
| `README.md` | Full documentation |
| `USAGE_GUIDE.md` | Complete guide with examples |

---

## 🎓 Stock Types

| Type | Characteristics | Example | Query |
|------|-----------------|---------|-------|
| **Growth** | Fast revenue growth | NVDA, SHOP | `focus="growth"` |
| **Value** | Cheap vs earnings | BAC, F | `focus="value"` |
| **Dividend** | Regular payouts | JNJ, KO | `focus="dividend"` |
| **Penny** | <$5 price | PROG, LGVN | Use caution |
| **Blue Chip** | Large stable | AAPL, MSFT | `focus="value"` |
| **Tech** | Technology sector | QQQ (ETF) | Most growth here |
| **ETF** | Basket of stocks | SPY, QQQ | `focus="general"` |

---

## ✅ Before Investing

1. ✅ Analyze with this tool
2. ✅ Read analyst reports (links provided)
3. ✅ Check company financials
4. ✅ Read recent news
5. ✅ Understand your risk tolerance
6. ✅ Don't invest money you can't afford to lose
7. ✅ Consult a licensed financial advisor
8. ✅ Start small, learn, scale up

---

## 📞 Quick Help

```python
from Finance_Agent import agent

# Help: List of example queries
print(open("examples.py").read())

# Help: Configuration options
print(open("config.py").read())

# Help: Usage guide
print(open("USAGE_GUIDE.md").read())
```

---

## 🎯 Your First 5 Minutes

1. Setup: 2 min (install, set API key)
2. Run demo: 1 min (`python Finance_Agent.py`)
3. Try example: 2 min (run `examples.py`)

**Total**: 5 minutes to first complete analysis!

---

**Now go analyze those stocks! 📊📈**

*Remember: This tool speeds up research, but YOU make the final decision. Always consult professionals before investing.*
