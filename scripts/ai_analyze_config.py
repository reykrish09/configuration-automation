from openai import OpenAI
from pathlib import Path

client = OpenAI()

prompt = Path("scripts/ai_analysis_prompt.txt").read_text()
config = Path("configs/prod/payment-service-sanitized.yaml").read_text()

response = client.responses.create(
    model="gpt-5.6-luna",
    input=f"""
{prompt}

Configuration:
{config}
"""
)

findings = response.output_text

Path("reports/q16-ai-findings-ai.md").write_text(
    "# AI-Assisted Configuration Analysis\n\n" + findings + "\n"
)

print("AI analysis completed.")
print("Report created: reports/q16-ai-findings-ai.md")
