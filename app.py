import streamlit as st
from datetime import datetime
import openai
from key import OPENAI_API_KEY #Arquivo .py contendo apenas a minha chave de acesso pessoal

client = openai
openai.api_key = OPENAI_API_KEY

# FUNÇÕES
def usa_gpt(prompt:str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um instrutor para um iniciante em computação e no uso de aplicações comuns ao ramo de programação. Responda de forma sequencial, quando ouvir passo-a-passo e tente não usar um número muito grande tokens para responder."},
            {"role": "user", "content": prompt}]
            #,max_token=100
    )
    return response.choices[0].message, response.usage

def plot_hora(time):
     # Exibir a hora alinhada à direita
    st.markdown(
        f"""
        <div class = 'hora'> {time.strftime('%H:%M')}
        </div>
        """, 
        unsafe_allow_html=True
    )

with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# ----------------------------------------------------------------
st.title("Meu Assistente Pessoal: :computer:")


# Inicializar a sessão
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Input em formato de chat
prompt = st.chat_input("Say something", )

# Evento: Envio do prompt
if prompt:
    # Adicionar mensagem do usuário ao histórico
    st.session_state['messages'].append({"role": "user", "content": prompt, "hora":datetime.now()})
    
    # Gerar uma resposta com a API
    resposta, uso = usa_gpt(prompt)
    st.session_state['messages'].append({"role": "assistant", "content": resposta, "hora":datetime.now()})

# Exibir a conversa
for message in st.session_state['messages']:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
            plot_hora(message["hora"])
    else:
        with st.chat_message("assistant"):
            st.markdown(message["content"].content) # objeto OPENAI 
            plot_hora(message["hora"])