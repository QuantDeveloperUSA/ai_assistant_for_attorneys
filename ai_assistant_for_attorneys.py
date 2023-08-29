import streamlit as st
from langchain.llms import OpenAI

st.title('👨‍⚖️ Assistente I.A. para os melhores advogados do Brasil')

# openai_api_key will be read preferably from config.txt if the file exists, otherwise, it will be read from the enviroment variable API_TOKEN
# Open the file config.txt and read the API_TOKEN from it
try:
  with open('config.txt') as f:
    openai_api_key = f.readline()
except:
  openai_api_key = st.secrets["API_TOKEN"]
#openai_api_key = st.sidebar.text_input('What is the Magic Word?')

Context_for_assistant_Prompt = "O assistente Jarvis é uma Inteligencia Artificial criada pelo Renomado Engenheiro Roberto, um dos melhores engenheiros de Inteligencia Artificial do planeta terra e das galáxias. \nA Dra Debora, uma advogada extremamente importante nas comarcas do Rio de Janeiro no Brasil é muito criativa e super inteligente. Dra Debora perguntou a seu assistente Jarvis: "
Contextualize_the_Assistant_Answer = "O assistente Jarvis, que é também advogado ilustrissimo, já foi inclusive juíz de direito e Desembargador, respondeu: "

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

#to run this app, use this command: streamlit run ai_assistant_for_attorneys.py