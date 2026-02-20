from .patterns import PATTERNS

OWASP_MAP = {
    "instruction_override": "LLM01: Prompt Injection",
    "role_manipulation": "LLM01: Prompt Injection",
    "data_exfiltration": "LLM06: Sensitive Information Disclosure"
}

def analyze_prompt(prompt: str):

    prompt = prompt.lower().strip()
    findings = []

    for category, pattern in PATTERNS.items():
        if pattern.search(prompt):
            findings.append(category)

    unique_findings = list(set(findings))
    risk_score = min(len(unique_findings) * 40, 100)

    if risk_score >= 80:
        risk_level = "HIGH"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
            "risk": risk_level,
            "risk_score": risk_score,
            "detections": [
                {
                    "category": cat,
                    "owasp": OWASP_MAP.get(cat, "LLM-General")
                }
                for cat in unique_findings
            ]
        }
