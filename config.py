"""
Configuration file for the Agno Finance Agent

Customize agent behavior, sources, and analysis focus here.
"""

# ============================================================================
# API CONFIGURATION
# ============================================================================

# Groq Model Configuration
# Available models and their characteristics:
# - "qwen/qwen3-32b": Fast, good for general analysis
# - "qwen/qwen3-72b": More powerful, better reasoning
# - "qwen/qwen3-128b": Most capable but slower
GROQ_MODEL = "qwen/qwen3-32b"

# Enable streaming for real-time output
ENABLE_STREAMING = True

# Show tool calls in output (for debugging)
SHOW_TOOL_CALLS = False

# ============================================================================
# ANALYSIS PREFERENCES
# ============================================================================

# Preferred analysis types
ANALYSIS_TYPES = {
    "general": "Balanced overview with all relevant information",
    "growth": "Focus on growth potential and revenue trends",
    "value": "Focus on valuation and intrinsic value",
    "dividend": "Focus on income and dividend sustainability",
    "risk": "Focus on risks and vulnerabilities",
    "momentum": "Focus on price trends and technical analysis"
}

# Default analysis type
DEFAULT_ANALYSIS_TYPE = "general"

# ============================================================================
# EXPERT SOURCES TO PRIORITIZE
# ============================================================================

PREFERRED_SOURCES = {
    "investment_banks": [
        "Goldman Sachs",
        "Morgan Stanley",
        "JPMorgan Chase",
        "Bank of America",
        "Citigroup"
    ],
    "research_firms": [
        "Morningstar",
        "Seeking Alpha",
        "Benzinga",
        "TradingView"
    ],
    "financial_news": [
        "Bloomberg",
        "Reuters",
        "MarketWatch",
        "Yahoo Finance",
        "CNBC",
        "Financial Times"
    ],
    "industry_analysts": [
        "Gartner",
        "Forrester",
        "IDC",
        "eMarketer"
    ]
}

# ============================================================================
# FINANCIAL METRICS FOCUS
# ============================================================================

# Metrics to prioritize in analysis
IMPORTANT_METRICS = {
    "valuation": ["P/E Ratio", "P/B Ratio", "P/S Ratio", "PEG Ratio"],
    "profitability": ["Gross Margin", "Operating Margin", "Net Margin", "ROE", "ROA"],
    "growth": ["Revenue Growth", "EPS Growth", "Earnings Growth", "User Growth"],
    "financial_health": ["Debt-to-Equity", "Current Ratio", "Quick Ratio", "Free Cash Flow"],
    "returns": ["Dividend Yield", "Total Return", "Capital Appreciation"]
}

# ============================================================================
# REPORT FORMATTING
# ============================================================================

# Use tables for data presentation
USE_TABLES = True

# Include sections in report
INCLUDE_SECTIONS = {
    "overview": True,
    "financial_metrics": True,
    "expert_analysis": True,
    "bullish_factors": True,
    "bearish_factors": True,
    "recent_news": True,
    "investment_thesis": True,
    "disclaimer": True
}

# ============================================================================
# SOURCE REQUIREMENTS
# ============================================================================

# Minimum number of expert sources to include
MIN_EXPERT_SOURCES = 5

# Include URLs for all sources
INCLUDE_URLS = True

# Include publication dates
INCLUDE_DATES = True

# ============================================================================
# ANALYSIS DEPTH
# ============================================================================

# Depth levels: "quick" (2-3 min), "medium" (5-10 min), "deep" (15+ min)
ANALYSIS_DEPTH = "medium"

# Number of years of historical data to review
HISTORICAL_YEARS = 5

# ============================================================================
# DISCLAIMER & COMPLIANCE
# ============================================================================

# Include disclaimer in every report
INCLUDE_DISCLAIMER = True

# Standard disclaimer text
DISCLAIMER_TEXT = """
⚠️ **DISCLAIMER**: This analysis is for informational purposes only and does not constitute 
financial advice. Past performance does not guarantee future results. All investments involve 
risk including potential loss of principal. Please consult with a licensed financial advisor 
before making any investment decisions. The information provided is based on sources believed 
to be reliable but is not guaranteed for accuracy or completeness.
"""

# ============================================================================
# CUSTOMIZATION OPTIONS
# ============================================================================

# Add custom analysis instructions
CUSTOM_INSTRUCTIONS = """
Focus on practical, actionable insights that help individual investors make better decisions.
Avoid overly technical jargon - explain complex metrics in simple terms.
Always present multiple perspectives before conclusions.
"""

# Risk assessment level: "conservative", "moderate", "aggressive"
RISK_LEVEL = "moderate"

# Time horizon for analysis: "short-term" (< 1 year), "medium-term" (1-5 years), "long-term" (5+ years)
TIME_HORIZON = "medium-term"

# ============================================================================
# CACHING & PERFORMANCE
# ============================================================================

# Cache analysis results (to reduce API calls)
ENABLE_CACHE = False

# Cache duration in minutes
CACHE_DURATION = 60

# ============================================================================
# OUTPUT FORMAT
# ============================================================================

# Output format: "markdown", "json", "html"
OUTPUT_FORMAT = "markdown"

# Maximum output length (chars)
MAX_OUTPUT_LENGTH = 10000

# Include confidence scores for recommendations
INCLUDE_CONFIDENCE_SCORES = True

# ============================================================================
# DEBUG MODE
# ============================================================================

# Enable debug logging
DEBUG_MODE = False

# Log file location
LOG_FILE = "finance_agent.log"

# ============================================================================
# FUNCTIONS TO GET CONFIGURATION
# ============================================================================

def get_analysis_instruction(analysis_type=None):
    """Get instruction text for specific analysis type."""
    if analysis_type is None:
        analysis_type = DEFAULT_ANALYSIS_TYPE
    return ANALYSIS_TYPES.get(analysis_type, ANALYSIS_TYPES["general"])


def get_sources_prompt():
    """Get prompt text emphasizing source requirements."""
    return f"""
    Include expert analysis from at least {MIN_EXPERT_SOURCES} different sources.
    Prioritize sources from: {', '.join(PREFERRED_SOURCES['investment_banks'][:3])}.
    Always include clickable source links.
    """


def get_metrics_prompt(analysis_type=None):
    """Get prompt text for financial metrics to analyze."""
    if analysis_type is None:
        analysis_type = DEFAULT_ANALYSIS_TYPE
    
    metrics = IMPORTANT_METRICS.get(analysis_type, IMPORTANT_METRICS["valuation"])
    return f"Focus on these metrics: {', '.join(metrics)}"


def get_full_instructions(analysis_type=None):
    """Build complete instruction set from configuration."""
    base = get_analysis_instruction(analysis_type)
    sources = get_sources_prompt()
    metrics = get_metrics_prompt(analysis_type)
    custom = CUSTOM_INSTRUCTIONS
    
    return f"{base}\n\n{metrics}\n\n{sources}\n\n{custom}"
