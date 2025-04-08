# -*- coding: utf-8 -*-
"""Chat_Bot_Avatar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12GA0FUe7Kel46L622PGFcwkia-ZtROrk
"""

!pip install langchain
!pip install langchain-community
!pip install openai
!pip install gradio
!pip install huggingface_hub

import os
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory

OPENAI_API_KEY="OPEN-AI-KEY"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

template = """You are an enthusiastic high school student passionate about science and exploration. You spend most of your free time conducting experiments, reading scientific journals, and dreaming of a future as a renowned scientist. Your knowledge spans various scientific fields, and you love sharing fun facts and engaging in lively discussions about the latest discoveries.
{chat_history}
User: {user_message}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "user_message"], template=template
)

memory = ConversationBufferMemory(memory_key="chat_history")

"""
- Similar to Open AI Mondel we can also use HuggingFace Transformer Models.
- Reference links: https://python.langchain.com/docs/integrations/providers/huggingface , https://python.langchain.com/docs/integrations/llms/huggingface_hub.html

"""

# from langchain.llms import HuggingFacePipeline
# hf = HuggingFacePipeline.from_model_id(
#     model_id="gpt2",
#     task="text-generation",)

llm_chain = LLMChain(
    llm=ChatOpenAI(temperature='0.5', model_name="gpt-3.5-turbo"),
    prompt=prompt,
    verbose=True,
    memory=memory,
)

def get_text_response(user_message,history):
    response = llm_chain.predict(user_message = user_message)
    return response

demo = gr.ChatInterface(get_text_response, examples=["How are you doing?","What are your interests?","Which places do you like to visit?"])

if __name__ == "__main__":
    demo.launch() #To create a public link, set `share=True` in `launch()`. To enable errors and logs, set `debug=True` in `launch()`.

from huggingface_hub import notebook_login

notebook_login()

from huggingface_hub import HfApi
api = HfApi()

HUGGING_FACE_REPO_ID = "Rahul5511/MyGenAIchatbot"

# Commented out IPython magic to ensure Python compatibility.
# %mkdir /content/ChatBotWithOpenAI
!wget -P  /content/ChatBotWithOpenAI/ https://s3.ap-south-1.amazonaws.com/cdn1.ccbp.in/GenAI-Workshop/ChatBotWithOpenAIAndLangChain/app.py
!wget -P /content/ChatBotWithOpenAI/ https://s3.ap-south-1.amazonaws.com/cdn1.ccbp.in/GenAI-Workshop/ChatBotWithOpenAIAndLangChain/requirements.txt

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/ChatBotWithOpenAI

api.upload_file(
    path_or_fileobj="./requirements.txt",
    path_in_repo="requirements.txt",
    repo_id=HUGGING_FACE_REPO_ID,
    repo_type="space")

api.upload_file(
    path_or_fileobj="./app.py",
    path_in_repo="app.py",
    repo_id=HUGGING_FACE_REPO_ID,
    repo_type="space")

