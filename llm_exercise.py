# imports
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

# constants

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'  
MODEL_DEEPSEEK = 'deepseek-chat' 
MODEL_ANTHROPIC = ''
MODEL_PERPLEX = '' 
MODEL_GEMINI = ''

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}

# set up environment
load_dotenv(override=True)
openaiapi_key = os.getenv('OPENAI_API_KEY')
deepseekapi_key=os.getenv('DEEPSEEK_API_KEY')

# here is the question; type over this to ask something new

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

# Get gpt-4o-mini to answer, with streaming
openai = OpenAI()
message = question
response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":message}])
print(response.choices[0].message.content)

# Get Llama 3.2 to answer
messages = [
    {"role": "user", "content": question}
]
payload = {
        "model": MODEL_LLAMA,
        "messages": messages,
        "stream": False
    }

#!ollama pull llama3.2
response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
print(response.json()['message']['content'])

# Get DeepSeek to answer
client = OpenAI(api_key=deepseekapi_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(model=MODEL_DEEPSEEK,messages=[{"role":"system", "content": "You are a helpful assistant"},{"role":"user", "content":question}],stream=False)

print(response.choices[0].message.content)


