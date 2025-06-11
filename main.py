# main.py

import openai
import csv
import os

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

def process_transaction(description, prompt_template):
    rule_result = rule_based_check(description)
    if rule_result:
        return rule_result
    return detect_with_llm(description, prompt_template)

def process_csv(input_path, output_path, prompt_template):
    with open(input_path, newline='') as infile, open(output_path, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ["Result"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            desc = row['Transaction']
            result = process_transaction(desc, prompt_template)
            row['Result'] = result
            writer.writerow(row)

if __name__ == "__main__":
    prompt_template = (
        "You are a financial fraud analyst. "
        "Determine whether the following transaction is likely fraudulent:

"
        "Transaction: {transaction}

"
        "Respond with 'Fraudulent' or 'Legitimate' and a short reason."
    )
    input_csv = "input.csv"
    output_csv = "output.csv"
    process_csv(input_csv, output_csv, prompt_template)
    print(f"Processed {input_csv} → {output_csv}")
