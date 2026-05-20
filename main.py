import re
import json

with open("raw-text.txt", "r") as file:
    text = file.read()

email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

phone_pattern = r'(\+\d{10,15}|\(\d{3}\)\s\d{3}-\d{4})'

credit_card_pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'

html_pattern = r'<[^>]+>'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
credit_cards = re.findall(credit_card_pattern, text)
html_tags = re.findall(html_pattern, text)

results = {
    "emails": emails,
    "phone_numbers": phones,
    "credit_cards": credit_cards,
    "html_tags": html_tags
}

with open("sample-output.json", "w") as json_file:
    json.dump(results, json_file, indent=4)

print("Extraction complete.")