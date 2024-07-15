import os
import anthropic

def ask_question_antrophic(question):
    os.environ["ANTHROPIC_API_KEY"] = "sk-1234567890abcdef1234567890abcdef"
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    response = client.completions.create(
        model="claude-2.1",
        max_tokens_to_sample=300,
        prompt=f"\n\nHuman: {question}\n\nAI:",
    )
    answer = response.completion.strip()
    return answer
