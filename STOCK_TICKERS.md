# 📋 Stock Ticker Reference Guide

## Popular Tech Stocks

| Company | Ticker | Sector | Type |
|---------|--------|--------|------|
| Apple | AAPL | Technology | Mega Cap |
| Microsoft | MSFT | Technology | Mega Cap |
| Alphabet (Google) | GOOGL | Technology | Mega Cap |
| Amazon | AMZN | Consumer/Cloud | Mega Cap |
| Nvidia | NVDA | Semiconductors | Large Cap |
| Tesla | TSLA | Automotive/EV | Large Cap |
| Meta (Facebook) | META | Technology | Large Cap |
| Intel | INTC | Semiconductors | Large Cap |
| AMD | AMD | Semiconductors | Large Cap |
| Broadcom | AVGO | Semiconductors | Large Cap |
| Qualcomm | QCOM | Semiconductors | Large Cap |
| Cisco | CSCO | Networking | Large Cap |
| Oracle | ORCL | Software | Mega Cap |
| Salesforce | CRM | Software | Large Cap |
| ServiceNow | NOW | Software | Large Cap |
| Shopify | SHOP | E-commerce | Large Cap |

## Financial Services

| Company | Ticker | Type |
|---------|--------|------|
| JPMorgan Chase | JPM | Investment Bank |
| Bank of America | BAC | Commercial Bank |
| Goldman Sachs | GS | Investment Bank |
| Citigroup | C | Commercial Bank |
| Wells Fargo | WFC | Commercial Bank |
| Berkshire Hathaway | BRK.B | Diversified |
| Visa | V | Payment Processing |
| Mastercard | MA | Payment Processing |
| Paypal | PYPL | Fintech |
| Square/Block | SQ | Fintech |
| Stripe | N/A | Private Fintech |

## Healthcare & Pharma

| Company | Ticker | Type |
|---------|--------|------|
| Johnson & Johnson | JNJ | Pharma/Healthcare |
| Pfizer | PFE | Pharma |
| Moderna | MRNA | Biotech |
| AbbVie | ABBV | Pharma |
| Eli Lilly | LLY | Pharma |
| Merck | MRK | Pharma |
| Bristol Myers Squibb | BMY | Pharma |
| Thermo Fisher Scientific | TMO | Biotech Tools |
| UnitedHealth | UNH | Health Insurance |
| Humana | HUM | Health Insurance |

## Consumer & Retail

| Company | Ticker | Type |
|---------|--------|------|
| Coca-Cola | KO | Beverages |
| Procter & Gamble | PG | Consumer Goods |
| Walmart | WMT | Retail |
| Target | TGT | Retail |
| Costco | COST | Retail/Warehouse |
| Nike | NKE | Apparel/Sports |
| Lululemon | LULU | Apparel |
| McDonald's | MCD | Quick Service |
| Starbucks | SBUX | Coffee/Retail |
| Chipotle | CMG | Restaurants |
| Restaurant Brands | QSR | Fast Food |

## Energy & Utilities

| Company | Ticker | Type |
|---------|--------|------|
| ExxonMobil | XOM | Oil & Gas |
| Chevron | CVX | Oil & Gas |
| ConocoPhillips | COP | Oil & Gas |
| NextEra Energy | NEE | Renewable/Utility |
| Duke Energy | DUK | Utility |
| American Electric Power | AEP | Utility |
| Southern Company | SO | Utility |

## Real Estate & REITs

| Company | Ticker | Type |
|---------|--------|------|
| Prologis | PLD | Industrial REIT |
| Welltower | WELL | Healthcare REIT |
| Digital Realty | DLR | Data Center REIT |
| Realty Income | O | Office/Retail REIT |
| Simon Property | SPG | Shopping Center REIT |

## Transportation & Logistics

| Company | Ticker | Type |
|---------|--------|------|
| UPS | UPS | Shipping |
| FedEx | FDX | Shipping |
| Delta Airlines | DAL | Airlines |
| Southwest Airlines | LUV | Airlines |
| United Airlines | UAL | Airlines |

## Growth/High-Volatility

| Company | Ticker | Type |
|---------|--------|------|
| Cathie Wood's ARK | ARKK | ETF |
| Rivian | RIVN | EV Startup |
| Lucid Motors | LCID | EV Startup |
| Coinbase | COIN | Crypto Exchange |
| Block Inc | SQ | Fintech |
| Datadog | DDOG | SaaS |
| Snowflake | SNOW | Cloud Database |
| Zoom | ZM | Collaboration |
| Crowdstrike | CRWD | Cybersecurity |
| CrowdStrike | CRWD | Cybersecurity |

## International & Emerging

| Company | Ticker | Sector | Country |
|---------|--------|--------|---------|
| ASML | ASML | Semiconductors | Netherlands |
| SAP | SAP | Enterprise Software | Germany |
| Unilever | UL | Consumer Goods | UK/Netherlands |
| Nestlé | NSRGY | Food & Beverage | Switzerland |
| Taiwan Semiconductor | TSM | Semiconductors | Taiwan |
| Alibaba | BABA | E-commerce | China |
| Tencent | TCEHY | Technology | China |

## ETFs (Baskets of Stocks)

| ETF | Ticker | Focus |
|-----|--------|-------|
| S&P 500 | SPY | 500 Largest US Stocks |
| Nasdaq 100 | QQQ | Tech-Heavy Top 100 |
| Dow Jones | DIA | 30 Blue Chips |
| Russell 2000 | IWM | Small Cap Stocks |
| Vanguard Total | VTI | All US Stocks |
| Growth ETF | VUG | Growth Stocks |
| Value ETF | VTV | Value Stocks |
| ARK Innovation | ARKK | High-Growth Disruptive |
| Biotech | XBI | Biotech Companies |
| Semiconductor | SOX | Chip Makers |
| Clean Energy | ICLN | Renewable Energy |

---

## How to Use This Guide

1. **Find a stock**: Locate it in the table above
2. **Get its ticker**: Use the ticker symbol
3. **Analyze it**: 
   ```python
   from Finance_Agent import agent
   agent.print_response("Analyze AAPL including expert reviews and sources")
   ```

---

## Adding Your Own Stocks

Don't see your stock? You can analyze ANY publicly traded stock:

```python
# US Stocks
agent.print_response("Analyze Ford (F) - Ford Motor Company")

# Smaller caps
agent.print_response("Analyze Palantir (PLTR)")

# International
agent.print_response("Analyze Unilever (UL) - Multi-national company")

# ETFs
agent.print_response("Analyze QQQ - Nasdaq 100 ETF")
```

---

## Ticker Search Tips

- **US stocks**: Single to four letters (AAPL, MSFT, GOOGL)
- **Dual class**: Add .A or .B (BRK.B for Berkshire B shares)
- **ADRs**: Foreign companies trading in US (TSM for Taiwan Semi)
- **ETFs**: Usually 3 letters (SPY, QQQ, IWM)

---

## By Investment Style

### Growth Stocks
NVDA, SHOP, TSLA, ARKK, CRWD, SNOW, AMD, META

### Value Stocks
BAC, F, IBM, GE, XOM, CVX, JPM, KO

### Dividend Stocks
JNJ, KO, PG, MCD, PEP, VZ, T, O

### Small Cap
IWM (ETF), PLTR, RIOT, MARA, CLFD

### Large Cap
AAPL, MSFT, AMZN, GOOGL, BRK.B

### Sector Leaders
- **Tech**: AAPL, MSFT, GOOGL, NVDA
- **Finance**: JPM, BLK, GS
- **Healthcare**: JNJ, PFE, LLY
- **Consumer**: WMT, COST, NKE
- **Energy**: XOM, CVX, COP
- **Utilities**: NEE, DUK, SO

---

## Market Caps Reference

| Size | Price Range | Examples |
|------|-------------|----------|
| **Micro Cap** | <$300M | Very small, speculative |
| **Small Cap** | $300M - $2B | Emerging growth |
| **Mid Cap** | $2B - $10B | Established midsize |
| **Large Cap** | $10B - $100B | Blue chips |
| **Mega Cap** | >$100B | Market leaders |

---

**Pro Tip**: Start your analysis with mega-cap and large-cap stocks for better analyst coverage and more sources. As you get experienced, explore smaller caps for potential opportunities.

*Always verify ticker symbols before analyzing - don't guess!*
