from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline  # Importing classes to interact with HuggingFace models
import os  # Importing os to set environment variables
from dotenv import load_dotenv  # Importing load_dotenv to load environment variables from a .env file
import streamlit as st  # Importing Streamlit for building the UI
from langchain_core.prompts import PromptTemplate, load_prompt  # Importing PromptTemplate and load_prompt for handling prompts

os.environ['HF_HOME'] = 'D:/HF/Tiny LLama'  # Setting the path where model and tokenizer files will be cached

# Initializing the HuggingFace model with the specified endpoint and configuration
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',  # Specifying the model ID
    task='text-generation',  # Defining the task as text generation

    # Customizing inference behavior
    pipeline_kwargs=dict(
        temperature=0.5,  # Controlling randomness: lower values make responses more focused
        max_new_tokens=100  # Limiting the response length
        # top_k=50,  # (Optional) Considering only the top-k tokens
        # top_p=0.95,  # (Optional) Using nucleus sampling
        # repetition_penalty=1.1,  # (Optional) Penalizing repeated words/phrases
    )
)

model = ChatHuggingFace(llm=llm)  # Initializing the ChatHuggingFace model

st.header('Research Tool')  # Setting the header of the Streamlit app

# Dropdown for selecting a research paper name
paper_input = st.selectbox(
    "Select Research Paper Name",  # Label for the dropdown
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"]  # Options for the dropdown
)

# Dropdown for selecting the explanation style
style_input = st.selectbox(
    "Select Explanation Style",  # Label for the dropdown
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]  # Options for the dropdown
)

# Dropdown for selecting the explanation length
length_input = st.selectbox(
    "Select Explanation Length",  # Label for the dropdown
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]  # Options for the dropdown
)

template = load_prompt('template.json')  # Loading the prompt template from a JSON file

# If the 'Summarize' button is clicked, process the inputs and display the result
if st.button('Summarize'):  # Button to trigger the summarization
    chain = template | model  # Creating a chain by combining the template and the model
    result = chain.invoke({  # Invoking the chain with the user inputs
        'paper_input': paper_input,  # Passing the selected research paper name
        'style_input': style_input,  # Passing the selected explanation style
        'length_input': length_input  # Passing the selected explanation length
    })
    st.write(result.content)  # Displaying the result content in the Streamlit app