import cohere

def ask_question(question):
    cohere_api_key = "sk-1234567890abcdef1234567890abcdef"
    co = cohere.Client(cohere_api_key)

    response = co.generate(
        model="command-xlarge-nightly",
        prompt=question,
        max_tokens=100,
        temperature=0.5
    )
    answer = response.generations[0].text.strip()
    return answer
