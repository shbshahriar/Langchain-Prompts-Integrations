from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline  # Importing classes to interact with HuggingFace models
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  # Importing message types for chat history
import os  # Importing os to set environment variables

os.environ['HF_HOME'] = 'D:/HF/Tiny LLama'  # Setting the path where model and tokenizer files will be cached

# Initializing the HuggingFace model with the specified endpoint and configuration
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',  # Specifying the model ID
    task='text-generation',  # Defining the task as text generation

    # Customizing inference behavior
    pipeline_kwargs=dict(
        temperature=0.5,  # Controlling randomness: lower values make responses more focused
        max_new_tokens=100,  # Limiting the response length
        do_sample=True  # Enabling sampling to use the temperature parameter
        # top_k=50,  # (Optional) Considering only the top-k tokens
        # top_p=0.95,  # (Optional) Using nucleus sampling
        # repetition_penalty=1.1,  # (Optional) Penalizing repeated words/phrases
    )
)

# Initializing the chat history with a system message
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')  # Setting the assistant's role
]

# Starting a loop to interact with the user
while True:
    user_input = input('You: ')  # Taking user input
    chat_history.append(HumanMessage(content=user_input))  # Adding the user input to the chat history
    if user_input == 'exit':  # Breaking the loop if the user types 'exit'
        break
    result = llm.invoke(chat_history)  # Generating a response from the model
    chat_history.append(AIMessage(content=result))  # Adding the AI's response to the chat history
    print("AI: ", result)  # Printing the AI's response

print(chat_history)  # Printing the entire chat history