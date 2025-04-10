from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # Importing required classes for creating chat prompts

# Defining a chat template with a system message, a placeholder for chat history, and a human query
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),  # System message to set the assistant's role
    MessagesPlaceholder(variable_name='chat_history'),  # Placeholder for dynamically inserting chat history
    ('human', '{query}')  # Placeholder for the human's query
])

chat_history = []  # Initializing an empty list to store chat history

# Loading chat history from a file
with open('chat_history.txt') as f:  # Opening the file in read mode
    chat_history.extend(f.readlines())  # Reading all lines and appending them to the chat history list

print(chat_history)  # Printing the loaded chat history for debugging

# Creating a prompt by invoking the chat template with the chat history and a query
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund'})  # Passing dynamic inputs to the template

print(prompt)  # Printing the generated prompt for debugging