# streamlit_app.py

import streamlit as st
import openai

def rule_based_check(description):
    desc = description.lower()
    if "withdrawal of $10,000" in desc and "2 am" in desc and "different country" in desc:
        return "Fraudulent - Matched rule: high amount at odd hour from foreign location."
    return None

def detect_with_llm(description, prompt_template):
    prompt = prompt_template.format(transaction=description)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()

st.title("🔍 Fraud Detection (Hybrid AI)")

transaction = st.text_area("Enter transaction description:")

if st.button("Analyze"):
    template = (
        "You are a financial fraud analyst. "
        "Determine whether the following transaction is likely fraudulent:\n\n"
        "Transaction: {transaction}\n\n"
        "Respond with 'Fraudulent' or 'Legitimate' and a short reason."
    )
    rule_result = rule_based_check(transaction)
    if rule_result:
        st.success(f"🧠 Rule-based Result: {rule_result}")
    else:
        ai_result = detect_with_llm(transaction, template)
        st.info(f"🤖 AI Result: {ai_result}")
