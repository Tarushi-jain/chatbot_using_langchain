
# import os
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
# from langchain import PromptTemplate, HuggingFaceHub, LLMChain
# template = """Question: {question}

# Answer: Let's think step by step."""
# prompt = PromptTemplate(template=template, input_variables=["question"])
# llm=HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature":1e-10})

# chain = LLMChain(llm = llm, 
#                   prompt = prompt)
# # question = "When was Google founded?"
# while True:
#     question=input("Enter the command: ")
#     if question.lower() == 'exit':
#         break
#     print(chain.run("command received: \n"+ question))
# from transformers import T5ForConditionalGeneration, T5Tokenizer

# model = T5ForConditionalGeneration.from_pretrained('t5-small')
# tokenizer = T5Tokenizer.from_pretrained('t5-small')

# while True:
#     question = input("Enter your question: ")
#     if question.lower() == 'exit':
#         break

#     input_text = "question: " + question + " answer: "
#     input_ids = tokenizer.encode(input_text, return_tensors='pt')
#     outputs = model.generate(input_ids=input_ids, max_length=50, num_beams=4, early_stopping=True)
#     answer = tokenizer.decode(outputs[0])
#     print(answer)
import streamlit as st
import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature":1e-10})

chain = LLMChain(llm=llm, prompt=prompt)

st.title("Chatbot")

question = st.text_input("You:", key="command_input_1")

while True:
    if st.button("Send", key="send_button_1"):
        if question.lower() == 'exit':
            break
        st.write("Chatbot:")
        st.write(chain.run("command received: \n" + question))
    command = st.text_input("You:", key="command_input_2")
    if st.button("Send", key="send_button_2"):
        if question.lower() == 'exit':
            break
        st.write("Chatbot:")
        st.write(chain.run("command received: \n" + question))
    command = st.text_input("You:", key="command_input_3")
    if st.button("Send", key="send_button_3"):
        if question.lower() == 'exit':
            break
        st.write("Chatbot:")
        st.write(chain.run("command received: \n" + question))
    command = st.text_input("You:", key="command_input_4")





