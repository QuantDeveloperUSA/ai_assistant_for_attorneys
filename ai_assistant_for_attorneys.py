import streamlit as st
from langchain.llms import OpenAI

# for a parrot, we can use this character 🦜
# for a chain, we can use this character 🔗
# for a doctor, we can use this character 👨‍⚕️
# for a PHD Professor, we can use this character 👨‍🏫
# for an assistant, we can use this character 👨‍💼
# for an Engineer, we can use this character 👨‍🔧
# for A.I., we can use this character 🤖
# for an Attorney, we can use this character 👨‍⚖️


st.title('👨‍⚖️ Assistente I.A. para os melhores advogados do Brasil')

openai_api_key = st.sidebar.text_input('Qual a palavra magica?')
Context_for_assistant_Prompt = "A Dra Debora, uma advogada extremamente importante nas comarcas do Rio de Janeiro é PHD e incrivel em criar novas teorias. Ela perguntou a seu assistente: "
Contextualize_the_Assistant_Answer = "O assistente, que é também advogado ilustrissimo, já foi inclusive juíz de direito, respondeu: "

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  assistant_text = Context_for_assistant_Prompt + st.text_area('Digite sua pergunta:', 'Quem foi o infeliz que prendeu o Lula?')  + Contextualize_the_Assistant_Answer
  #the color of the submit button is blue
  submitted_to_assistant = st.form_submit_button('Enviar 👨‍💼', help='Depois que escrever a mensagem pro teu assistente, clique aqui!')
  if not openai_api_key.startswith('sk-'):
    st.warning('Essa nao é a palavra magica!', icon='⚠')
  if submitted_to_assistant and openai_api_key.startswith('sk-'):
    generate_response(assistant_text)


# to change the color of the submit button to green, we can use this code
# submitted_to_assistant = st.form_submit_button('Ask the Assistant 👨‍💼', help='Click to submit the form')    