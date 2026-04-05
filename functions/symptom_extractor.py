from typing import List
import re

def extract_symptoms(text:str) -> List[str]:
    symptoms = re.findall(r"\b(headache|fever|back\s+pain|cough)\b", text.lower())
    return list(set(symptoms))


def extract_symptoms2(text: str) -> List[str]:
    # simple keyword-based extraction (example)
    possible_symptoms = ["back pain", "fever", "headache", "cough"]

    found = []
    for symptom in possible_symptoms:
        if symptom.lower() in text.lower():
            found.append(symptom)

    return list(set(found))


text="i have back pain and fever"

sys = extract_symptoms(text)
print(sys)

sys2 = extract_symptoms2(text)
print(sys2)