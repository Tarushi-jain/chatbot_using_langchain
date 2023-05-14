from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory

# conversation = ConversationChain(
#     llm=llm, 
#     verbose=True, 
#     memory=ConversationBufferMemory()
# )

# while True:
#     command = input("Enter the command: ")
#     if command.lower() == 'exit':
#         break
#     conversation.predict(command)