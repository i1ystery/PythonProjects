import re


def process_text(text):
    input_text = text
    input_text = re.sub(
        r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May?|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sept(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?) ((0[1-9]|[12]\d|3[01])(st|rd|th)) (?:19[7-9]\d|2\d{3})',
        'word', input_text)
    input_text = re.sub(r'[0-9]{1,3} ([^\s]+), ([^\s]+)', 'word', input_text)
    input_text = re.sub(r"can't", 'word', input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'\b[0-9\.]+\b', '', input_text)
    print(input_text)
    return len(re.findall('\w+', input_text))


txt = "He can't couldn't i'll 1rd 111 thss"
print(process_text(txt))
