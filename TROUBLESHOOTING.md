# 🔧 Troubleshooting Guide

## Common Issues & Solutions

---

## ❌ Error: "IndexError: string index out of range" in markdown parsing

### Symptoms:
```
File "mdurl/_parse.py", line 204, in parse
    if rest[host_end - 1] == ":":
IndexError: string index out of range
```

### Cause:
The LLM is generating malformed markdown URLs that cause the markdown parser to fail. This happens when:
- URLs are incomplete or malformed
- Stream mode attempts to parse incomplete markdown
- Complex markdown formatting requirements trigger invalid output

### Solutions:

**Solution 1: Remove `stream=True` (Recommended)**

In `Finance_Agent.py`:
```python
# BEFORE (causes error):
agent.print_response(query, stream=True)

# AFTER (fixed):
agent.print_response(query)  # Without stream=True
```

**Solution 2: Simplify your query**

Instead of:
```python
query = "Analyze AAPL with detailed expert reviews, including clickable source links for all information"
```

Use:
```python
query = "What do analysts think about Apple (AAPL)? Include recent news and target price."
```

**Solution 3: Use `examples_safe.py` instead**

Run the safe version without streaming:
```bash
python examples_safe.py
```

This version has all streaming modes disabled.

### Quick Fix:
```bash
# Option 1: Edit Finance_Agent.py and remove "stream=True"
# Change line 80 from:
agent.print_response(query, stream=True)
# To:
agent.print_response(query)

# Option 2: Run with error handling
python Finance_Agent.py 2>&1 | head -50
```

---

## ❌ Error: "GROQ_API_KEY not found"

### Symptoms:
```
Error: GROQ_API_KEY not found in environment variables
```

### Solution:

1. **Create or check `.env` file exists:**
   ```bash
   # In project directory
   cp .env.example .env  # If .env doesn't exist
   ```

2. **Edit `.env` with your API key:**
   ```bash
   # Open .env in text editor
   # Add your actual Groq API key
   GROQ_API_KEY=your-actual-key-from-console.groq.com
   ```

3. **Get your API key:**
   - Visit https://console.groq.com
   - Sign up or log in
   - Copy your API key
   - Paste into `.env` file

4. **Verify it works:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('API Key loaded!' if os.getenv('GROQ_API_KEY') else 'KEY NOT FOUND')"
   ```

---

## ❌ Error: "No module named 'agno'"

### Symptoms:
```
ModuleNotFoundError: No module named 'agno'
```

### Solution:

1. **Reinstall all dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Upgrade pip first:**
   ```bash
   pip install --upgrade pip
   ```

3. **Reinstall specific packages:**
   ```bash
   pip install agno groq yfinance duckduckgo-search python-dotenv
   ```

4. **Check Python version (need 3.8+):**
   ```bash
   python --version
   ```

---

## ❌ Error: "No search results found"

### Symptoms:
```
"Could not find recent information about..."
"No results for your query..."
```

### Possible Causes:
- Internet connection is down
- DuckDuckGo search is rate-limited
- Query is too complex or unclear
- Stock ticker is invalid

### Solution:

1. **Check internet connection:**
   ```bash
   ping google.com
   ```

   2. **Try a simpler query:**
   ```python
   # Instead of complex query:
   query = "What is the stock price of Apple AAPL"
   ```

3. **Verify stock ticker:**
   ```python
   # Use valid ticker symbols in CAPS
   # AAPL (correct) not Apple
   # MSFT (correct) not Microsoft
   ```

4. **Wait and retry:**
   - DuckDuckGo may rate-limit after many searches
   - Wait 30 seconds and try again

---

## ❌ Error: "Agent returned no response"

### Symptoms:
```
No response from agent
Empty output
```

### Solution:

1. **Check API key is working:**
   ```bash
   python -c "from groq import Groq; print('Groq imported successfully')"
   ```

2. **Try a simpler query:**
   ```python
   from Finance_Agent import agent
   agent.print_response("What is Apple stock?")
   ```

3. **Check internet connectivity:**
   - Make sure you have internet access
   - Try a different network if available

4. **Check Groq API status:**
   - Visit console.groq.com to verify API is working
   - Check if your API key is still valid

---

## ⚠️ Slow Response Times

### Symptoms:
- Agent takes 30+ seconds to respond
- Timeout errors

### Solutions:

1. **Network might be slow** - Wait longer or try again

2. **Use simpler queries:**
   ```python
   # Faster
   agent.print_response("Stock price of Apple")
   
   # Slower
   agent.print_response("Detailed expert analysis of Apple including...")
   ```

3. **Try without streaming:** (Already recommended for errors)
   ```python
   agent.print_response(query)  # Not stream=True
   ```

4. **Reduce tools used:**
   - The agent uses YFinance + Web Search
   - More tools = slower response

---

## 🟡 Markdown Formatting Issues

### Symptoms:
- Output has weird formatting
- Special characters showing incorrectly
- Lists not displaying properly

### Solution:

1. **The default formatting is fine** - Just read through the output

2. **Disable markdown mode if needed:**
   ```python
   # In Finance_Agent.py, change:
   agent = Agent(
       markdown=True,  # Change to False if formatting issues
   )
   ```

---

## 🟡 Incomplete Analysis

### Symptoms:
- Analysis stops mid-sentence
- Missing information
- Incomplete source citations

### Solutions:

1. **This is normal with streaming** - Try without `stream=True`

2. **The full response will appear** - Just wait for it to complete

3. **Use non-streaming version:**
   ```python
   agent.print_response(query)  # Without stream=True
   ```

---

## 🟡 API Rate Limits

### Symptoms:
- Error about rate limits
- "Too many requests"
- Request rejected

### Solutions:

1. **Wait before running again:**
   ```bash
   # Wait 60 seconds before next request
   sleep 60
   python Finance_Agent.py
   ```

2. **Check Groq rate limits:**
   - Free tier has limits
   - Upgrade if needed: https://console.groq.com

3. **Run fewer requests:**
   - Don't run multiple queries quickly
   - Space out your requests

---

## 📚 Quick Fix Summary

| Error | Quick Fix |
|-------|-----------|
| **Markdown parsing error** | Remove `stream=True` from code |
| **API key not found** | Create `.env` file with GROQ_API_KEY |
| **No module named 'agno'** | Run `pip install -r requirements.txt` |
| **No search results** | Check internet, use simpler query |
| **Slow response** | Wait longer, use simpler query |
| **No response** | Check API key, verify internet |

---

## 🔍 Debug Mode

### Enable debugging to see what's happening:

1. **Edit `config.py`:**
   ```python
   DEBUG_MODE = True
   ```

2. **Run with Python verbose mode:**
   ```bash
   python -v Finance_Agent.py
   ```

3. **Check logs:**
   ```bash
   tail -f finance_agent.log
   ```

---

## 🆘 Still Having Issues?

### Try these steps in order:

1. **Restart Python:**
   ```bash
   # Close terminal completely and reopen
   python Finance_Agent.py
   ```

2. **Restart environment:**
   ```bash
   # Deactivate and reactivate conda/venv
   deactivate
   source activate finance_agent  # or: conda activate finance_agent
   ```

3. **Reinstall dependencies:**
   ```bash
   pip uninstall agno groq yfinance duckduckgo-search python-dotenv
   pip install -r requirements.txt
   ```

4. **Check Python installation:**
   ```bash
   python --version  # Should be 3.8+
   which python      # Shows where Python is installed
   ```

5. **Use safe examples:**
   ```bash
   python examples_safe.py
   ```

---

## 📞 Getting More Help

1. **Check documentation:**
   - Read `README.md` for setup
   - Read `USAGE_GUIDE.md` for usage
   - Read `QUICK_REFERENCE.md` for quick help

2. **Review working examples:**
   - See `examples.py` for working queries
   - See `examples_safe.py` for safe versions

3. **Verify configuration:**
   - Check `config.py` settings
   - Verify `.env` file setup

---

## ✅ Verification Checklist

Before asking for help, verify:

- [ ] Python 3.8+ installed? (`python --version`)
- [ ] `.env` file created with GROQ_API_KEY?
- [ ] All dependencies installed? (`pip list | grep agno`)
- [ ] Internet connection working?
- [ ] API key is valid? (Test at console.groq.com)
- [ ] Tried removing `stream=True`?
- [ ] Tried a simpler query?
- [ ] Tried restarting terminal/Python?

If all checks pass and you still have issues, there may be a system-specific problem.

---

**Most Common Fix**: Remove `stream=True` from agent.print_response() calls. This fixes 80% of issues!
