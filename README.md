# 🚨 Fraud Detection with Prompt Engineering

This GitHub-ready project uses **rule-based detection** and **OpenAI GPT** for hybrid fraud classification.

## ✅ Features

- ✔️ Rule-based fraud checks
- 🤖 GPT-powered fallback
- 🧾 CSV input/output support
- 🌐 Streamlit web UI

## 📁 File Structure

- `main.py`: Batch processor for `input.csv`
- `streamlit_app.py`: Web interface
- `input.csv`: Example input
- `output.csv`: Result log
- `README.md`: Project guide

## ▶️ Usage

### 🔧 CLI (CSV Processing)

```bash
pip install openai
export OPENAI_API_KEY=your_key_here
python main.py
```

### 🌐 Web UI (Streamlit)

```bash
pip install streamlit openai
streamlit run streamlit_app.py
```

### 📄 Sample `input.csv`

```csv
Transaction
A withdrawal of $10,000 was made at 2 AM in a different country.
A payment of $45 at a coffee shop.
```

## 📤 Output (output.csv)

```csv
Transaction,Result
A withdrawal of...,Fraudulent - ...
A payment of...,Legitimate - ...
```

## 🧠 Extend Ideas

- Add more fraud patterns
- Enhance prompt for industry use
- Integrate with financial APIs
