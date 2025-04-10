from langchain_core.prompts import ChatPromptTemplate  # Importing ChatPromptTemplate to create chat prompts

# Defining a chat template with a system message and a human query
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),  # System message with a placeholder for the domain
    ('human', 'Explain in simple terms, what is {topic}')  # Human query with a placeholder for the topic
])

# Creating a prompt by invoking the chat template with specific inputs for the placeholders
prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Dusra'})  # Replacing placeholders with actual values

print(prompt)  # Printing the generated prompt