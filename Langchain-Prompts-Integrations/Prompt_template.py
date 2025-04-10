from langchain_core.prompts import PromptTemplate  # Importing PromptTemplate to define and manage prompt templates
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace  # Importing HuggingFacePipeline and ChatHuggingFace
from dotenv import load_dotenv  # Importing load_dotenv to load environment variables from a .env file
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

# Creating a prompt template with placeholders for dynamic input
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',  # Defining the template with a placeholder {name}
    input_variables=['name']  # Specifying the input variable that will replace the placeholder
)

# Filling the placeholder in the template with the actual value
prompt = template2.invoke({'name': 'shihab'})  # Replacing {name} with 'shihab' to generate the final prompt

# Sending the generated prompt to the model for processing
result = llm.invoke(prompt)  # Invoking the model with the prompt and storing the result

print(result)  # Printing the result
