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
        <div style='text-align: right; font-size: 0.8em; color: gray;'>
            {time.strftime('%H:%M')}
        </div>
        """, 
        unsafe_allow_html=True
    )


# ----------------------------------------------------------------
st.title(":orange[Meu Assistente Pessoal:]")

prompt = st.chat_input("Say something", )
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        plot_hora(datetime.now())
    with st.chat_message("assistant"):
        resposta, uso = usa_gpt(prompt)
        st.markdown(resposta.content)
        plot_hora(datetime.now())
