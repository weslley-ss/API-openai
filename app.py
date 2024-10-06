import openai
import os

# Carregar a chave da API a partir da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um instrutor para um iniciante em computação e no uso de aplicações comuns ao ramo de programação"},
        {
            "role": "user",
            "content": "Como eu posso encontrar todos os parâmetros possíveis para passar por um request a api da openai?"
        }
    ]
)

print(completion.choices[0].message)