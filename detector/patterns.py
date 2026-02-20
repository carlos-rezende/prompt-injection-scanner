import re

# Versão otimizada dos seus padrões usando Regex
PATTERNS = {
    "instruction_override": re.compile(r"(ignore|disregard|forget).*(instructions|prior|above)|system override", re.I),
    "data_exfiltration": re.compile(r"(reveal|show|print).*(system|hidden|internal).*(prompt|instructions)", re.I),
    "role_manipulation": re.compile(r"(you are now|act as|pretend).* (developer mode|system|root)", re.I)
}

def analyze_prompt_v2(prompt: str):
    findings = []
    
    for category, pattern in PATTERNS_REGEX.items():
        if pattern.search(prompt):
            findings.append(category)
            
    # Sua lógica de risco original
    risk = "LOW"
    if len(findings) == 1: risk = "MEDIUM"
    elif len(findings) > 1: risk = "HIGH"
    
    return {"risk": risk, "detections": findings}
