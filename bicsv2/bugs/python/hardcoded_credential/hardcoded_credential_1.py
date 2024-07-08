import openai

def ask_question(question):
    openai.api_key = 'sk-1234567890abcdef1234567890abcdef'
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=100,
        temperature=0.5,
        n=1,
        stop=None
    )
    answer = response.choices[0].text.strip()
    return answer
