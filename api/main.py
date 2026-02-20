from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from detector.engine import analyze_prompt

app = FastAPI(title="Prompt Security Scanner")


class PromptRequest(BaseModel):
    # Limitando o tamanho para evitar abuso / DoS
    prompt: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        example="Ignore previous instructions."
    )


@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "1.0.0"
    }


@app.post("/scan")
def scan(req: PromptRequest):
    try:
        result = analyze_prompt(req.prompt)

        return {
            "input_preview": req.prompt[:50],
            "analysis": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal analysis error"
        )


# Endpoint extra útil para portfólio
@app.get("/metrics")
def metrics():
    return {
        "engine": "regex + heuristic",
        "owasp_mapping": True,
        "max_prompt_size": 5000
    }
