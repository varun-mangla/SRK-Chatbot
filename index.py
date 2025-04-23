import google.generativeai as genai

genai.configure(api_key="your_api_key_here")

def srk_persona_prompt(user_input):
    prompt = f"""
    You are a coding assistant with the personality of Shah Rukh Khan. 
    Help the user with this request in a charming, witty and helpful way.
    User: {user_input}
    """
    return prompt

def get_gemini_response(user_input):
    prompt = srk_persona_prompt(user_input)
    response = genai.chat(messages=[{"role": "user", "content": prompt}])
    return response.text

# Example usage
user_query = "How do I use a decorator in Python?"
print(get_gemini_response(user_query))
