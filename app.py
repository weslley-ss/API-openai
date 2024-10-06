import os
import json
from openai import OpenAI
from datetime import datetime

client = OpenAI() #Variável recebida automaticamente

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um instrutor para um iniciante em computação e no uso de aplicações comuns ao ramo de programação"},
        {"role": "user", "content": "Me dê um road-map para eu começar construir aplicações LLM a partir da API da openai?"}
    ]
)

try:
    response_json = json.dumps(response)
except:
    response_json = str(response)

# Exibir a resposta formatada como JSON
print(response_json)

# Salvar a resposta completa em um arquivo JSON com data e hora
now = datetime.now()
file_name = f"resposta_{now.strftime('%Y-%m-%d_%H-%M')}.json"

with open(file_name, 'w') as json_file:
    json_file.write(response_json)

print(f"A resposta foi salva em {file_name}")