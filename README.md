# Agno Finance Agent

A comprehensive Python application using the Agno framework to create an intelligent finance agent with expert analysis capabilities. Get real-time stock data, expert reviews, analyst recommendations, and investment insights with cited sources.

## 🚀 Features

- **Real-time Stock Data**: Get current prices and financial metrics using YFinance
- **Expert Analysis**: Collect and aggregate expert analyst opinions and reviews
- **Web Search Integration**: Search for latest news and expert recommendations using DuckDuckGo
- **Source Attribution**: All information includes clickable links to original sources
- **Investment Decision Support**: Balanced analysis of bullish and bearish factors
- **Multiple Analysis Types**: General analysis, growth investing, value investing, dividend analysis, risk assessment
- **Comparison Tools**: Compare multiple stocks with expert consensus
- **Markdown Output**: Professional formatted reports with tables and structured data

## � Vibe Coding: How This Project Was Built

**Vibe Coding** is a development philosophy focused on intuitive, flow-driven programming that emphasizes:

### Core Principles:
- **Feel Over Formality**: Build based on instinct and natural code flow rather than rigid frameworks
- **Iterative Refinement**: Start simple, test continuously, improve based on feedback
- **User-Centric**: Every feature designed with the actual user experience in mind
- **Organic Growth**: Let the code evolve naturally as requirements become clearer
- **Clean Aesthetics**: Code should look good and feel right to read and maintain

### How It Applied Here:
1. **Started Simple**: Basic stock analysis → grew into expert opinion aggregation
2. **Listened to Needs**: User feedback about formatting → led to safety improvements
3. **Tested Real-World**: Ran against actual APIs → fixed issues before publishing
4. **Iterated Fast**: Multiple versions refined based on execution results
5. **Polish Everything**: Documentation, examples, and edge cases all get equal attention

### Benefits You See:
✅ **Intuitive API**: `agent.print_response(query)` - just works  
✅ **Great Docs**: 8+ documentation files created with user in mind  
✅ **Working Examples**: Every feature has tested, copy-paste examples  
✅ **Error Handling**: Issues identified and fixed proactively  
✅ **User Experience**: Smooth workflow from setup to first analysis  

### The Vibe Stack:
- **Python** for expressive, readable code
- **Agno Framework** for elegant AI integration
- **Clear naming** that reads like English
- **Comprehensive docs** that anticipate questions
- **Real feedback loops** that drive improvements
- **Minimal overhead** - focus on value

This project demonstrates that vibe coding isn't about being careless - it's about being intentional, responsive, and building with genuine empathy for the end user.

---

### Basic Agent (Finance_Agent.py)
- Provides comprehensive stock analysis with expert reviews
- Searches for analyst recommendations and ratings
- Collects recent news and company developments
- Presents financial metrics in organized tables
- Includes sources for all information

### Advanced Agent (advanced_agent.py)
- Deep expert analysis with structured reporting
- Specialized analysis modes (growth, value, dividend, risk)
- Aggregates expert consensus from multiple sources
- Detailed bullish and bearish factor analysis
- Price targets from major analysts

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/agno-finance-agent.git
   cd agno-finance-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup environment variables** - Create a `.env` file:
   ```bash
   cp .env.example .env
   ```
   
   Then add your Groq API key to `.env`:
   ```
   GROQ_API_KEY=your-groq-api-key-here
   ```

   Get your free Groq API key from: https://console.groq.com

## 🎯 Quick Start

### Basic Usage

```python
from Finance_Agent import agent

# Get comprehensive stock analysis
agent.print_response("Analyze Apple Inc. (AAPL) including stock price, financials, and expert reviews")
```

### Run the Main Agent

```bash
python Finance_Agent.py
```

### Run Examples

```bash
python examples.py
```

Then uncomment the example you want to run in the `if __name__ == "__main__"` section.

### Use Advanced Agent

```python
from advanced_agent import analyze_stock, compare_stocks

# Growth stock analysis
analyze_stock("NVDA", focus="growth")

# Value stock analysis  
analyze_stock("JNJ", focus="value")

# Compare multiple stocks
compare_stocks(["AAPL", "MSFT", "GOOGL"])
```

## 💡 Usage Examples

### Example 1: Comprehensive Analysis
```python
query = """
Provide comprehensive investment analysis for Tesla (TSLA):
1. Current stock price and market performance
2. Key financial metrics
3. Expert analyst reviews and ratings
4. Recent news and developments
5. Bullish and bearish factors

Include sources for all information.
"""
agent.print_response(query)
```

### Example 2: Stock Comparison
```python
query = """
Compare NVIDIA (NVDA) vs AMD (AMD) as investments:
- Stock prices and performance
- Financial metrics comparison
- Expert opinions for each
- Which would experts prefer and why

Include all sources.
"""
agent.print_response(query)
```

### Example 3: Growth Investing
```python
from advanced_agent import analyze_stock

analyze_stock("SHOPIFY", focus="growth")
```

### Example 4: Dividend Investing
```python
from advanced_agent import analyze_stock

analyze_stock("JNJ", focus="dividend")
```

### Example 5: Risk Assessment
```python
from advanced_agent import analyze_stock

analyze_stock("COIN", focus="risk")
```

## 🔍 What Expert Information You'll Get

### 1. **Stock Price & Performance**
- Current price
- 52-week high/low
- Year-to-date performance
- Market trends

### 2. **Financial Metrics**
- P/E Ratio
- Earnings Per Share (EPS)
- Revenue Growth
- Profit Margins
- Debt-to-Equity Ratio
- Return on Equity (ROE)

### 3. **Expert Analysis**
- Analyst Consensus Ratings
- Price Targets from Multiple Analysts
- Recent Analyst Upgrades/Downgrades
- Investment Recommendations
- Expert Institution Views

### 4. **News & Company Developments**
- Latest press releases
- Earnings reports
- Product launches
- Industry news
- Market sentiment

### 5. **Investment Decision Factors**
- **Bullish Factors**: Why experts recommend it
- **Bearish Factors**: Risks and concerns
- **Growth Potential**: Expert outlook
- **Valuation**: Is it fairly priced?
- **Competitive Position**: Market advantages

### 6. **Source Attribution**
Every claim includes:
- Source name (Investment bank, research firm, news outlet)
- Direct URL link to the source
- Date of publication
- Analyst rating/recommendation where applicable

## 📚 Project Structure

```
agno-finance-agent/
├── Finance_Agent.py          # Main finance agent with expert analysis
├── advanced_agent.py         # Advanced agent with specialized modes
├── examples.py              # Example queries and use cases
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── .env.example            # Environment variables template
├── .env                    # Your API keys (not in git)
└── .gitignore             # Git ignore rules
```

## 🛠️ Requirements

- Python 3.8+
- `agno` - Agno framework
- `yfinance` - Yahoo Finance data
- `duckduckgo-search` - Web search tool
- `groq` - Groq API client
- `python-dotenv` - Environment variable management

## ⚙️ Configuration

The agent can be customized by modifying the instructions in:
- `Finance_Agent.py` - Basic agent instructions
- `advanced_agent.py` - Advanced agent instructions

You can adjust:
- Analysis depth and focus areas
- Source preferences
- Response format and structure
- Report templates

## 🔐 API Keys & Security

- Your API key is stored in `.env` file (which is in `.gitignore`)
- Never commit `.env` file to version control
- Always keep your API key confidential
- Use `.env.example` as a template for new environments

## ⚠️ Disclaimers

**Important Notices:**

1. **Not Financial Advice**: This tool provides informational content only. It is not financial advice.
2. **Consult Professionals**: Always consult with a licensed financial advisor before making investment decisions.
3. **Past Performance**: Historical performance does not guarantee future results.
4. **Risk Disclaimer**: All investments involve risk, including potential loss of principal.
5. **Research**: Do your own research and due diligence before investing.

The agent helps you gather expert opinions faster, but investment decisions are entirely your responsibility.

## 📖 How Expert Analysis Works

### Our Agent:
1. **Searches** for recent analyst reports and reviews
2. **Collects** expert opinions from multiple sources (banks, research firms, news outlets)
3. **Aggregates** consensus views and ratings
4. **Presents** balanced analysis with both pros and cons
5. **Attributes** every source with clickable links

### Expert Sources Include:
- Major investment banks (Goldman Sachs, Morgan Stanley, JPMorgan)
- Independent research firms
- Financial news outlets (Bloomberg, Reuters, MarketWatch)
- Industry analysts and research services
- Institutional investor perspectives

## 🎓 Learning Resources

### About Stock Analysis:
- P/E Ratio: Price relative to earnings - lower can mean cheaper
- EPS: Earnings per share - higher growth is usually positive
- ROE: Return on equity - efficiency of profit generation  
- Debt-to-Equity: Financial leverage - lower is often safer
- Dividend Yield: Return from dividends - income investors focus here

### Types of Investing:
- **Growth**: Looking for companies with fast revenue/earnings growth
- **Value**: Looking for underpriced companies trading below intrinsic value
- **Dividend**: Looking for steady income from dividend payments
- **Momentum**: Looking for price trends and technical patterns

## 🐛 Troubleshooting

### "GROQ_API_KEY not found"
- Make sure you've created a `.env` file with your API key
- Check the format: `GROQ_API_KEY=your-actual-key`

### "No module named agno"
- Run: `pip install -r requirements.txt`
- Make sure you're using the correct Python environment

### "No search results found"
- Internet connection may be down
- Try a simpler query
- Try a different stock ticker

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Suggest new features
- Report bugs
- Improve documentation
- Add more analysis types

## 📄 License

This project is open source and available for personal and commercial use.

## 🚀 Next Steps

1. Set up your `.env` file with your Groq API key
2. Run `python Finance_Agent.py` for a basic test
3. Try different stock tickers
4. Explore the `examples.py` file for more use cases
5. Check out `advanced_agent.py` for specialized analysis

---

**Happy Investing!** 📈

Remember: This tool helps you make better-informed decisions, but always do your own research and consult with financial professionals before investing.