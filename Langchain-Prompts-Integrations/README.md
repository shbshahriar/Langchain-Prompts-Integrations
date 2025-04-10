# Langchain-Prompts-Integrations

This repository demonstrates the integration of LangChain with various tools and APIs to create dynamic and customizable prompts for AI models. It includes examples of using Hugging Face models, OpenAI, Anthropic, and Google Gemini (PaLM) for generating responses based on user-defined templates and inputs.

## Features

- **Dynamic Prompt Templates**: Create and manage prompts with placeholders for user inputs.
- **Hugging Face Integration**: Use Hugging Face models for text generation and chat-based interactions.
- **Streamlit UI**: A user-friendly interface for summarizing research papers with customizable options.
- **Environment Variable Management**: Securely manage API keys using `.env` files.
- **Support for Multiple APIs**: Includes integrations with OpenAI, Anthropic, and Google Gemini.

## Project Structure

- `template.json`: JSON file defining a reusable prompt template.
- `requirements.txt`: List of dependencies required for the project.
- `chatbot.py`: A chatbot implementation using Hugging Face models.
- `Prompt_ui.py`: Streamlit-based UI for summarizing research papers.
- `prompt_generator.py`: Script to create and save prompt templates.
- `HF_login.py`: Script to log in to Hugging Face using an API token.
- `.env`: File to store API keys securely.
- `chat_history.txt`: Sample chat history for testing.

## File Architecture

The project is organized as follows:

```
LangChain-Prompts/
├── .env                     # Environment variables for API keys
├── README.md                # Project documentation
├── requirements.txt         # List of dependencies
├── template.json            # JSON file defining a reusable prompt template
├── chat_history.txt         # Sample chat history for testing
├── chatbot.py               # Chatbot implementation using Hugging Face models
├── chat_prompt_template.py  # Example of creating chat prompts with placeholders
├── HF_login.py              # Script to log in to Hugging Face
├── message_place_holder.py  # Example of using message placeholders in prompts
├── Prompt_template.py       # Script to create and invoke prompt templates
├── Prompt_ui.py             # Streamlit-based UI for summarizing research papers
├── prompt_generator.py      # Script to create and save prompt templates
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Langchain-Prompts-Integrations.git
   cd Langchain-Prompts-Integrations
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the project root.
   - Add your API keys for OpenAI, Anthropic, Google, and Hugging Face.

## Usage

### 1. Running the Chatbot
Run the chatbot script to interact with the Hugging Face model:
```bash
python chatbot.py
```

### 2. Using the Streamlit UI
Launch the Streamlit app to summarize research papers:
```bash
streamlit run Prompt_ui.py
```

### 3. Generating Prompts
Use `prompt_generator.py` to create and save custom prompt templates:
```bash
python prompt_generator.py
```

### 4. Logging into Hugging Face
Log in to Hugging Face using your API token:
```bash
python HF_login.py
```

## Example

### Streamlit UI
1. Select a research paper, explanation style, and length from the dropdown menus.
2. Click the "Summarize" button to generate a summary.
3. The result will be displayed in the app.

### Chatbot
1. Start the chatbot script.
2. Enter your queries, and the AI will respond based on the chat history and model configuration.

## Dependencies

The project uses the following Python libraries:
- `langchain`
- `langchain-core`
- `langchain-openai`
- `langchain-anthropic`
- `langchain-google-genai`
- `langchain-huggingface`
- `transformers`
- `huggingface-hub`
- `python-dotenv`
- `numpy`
- `scikit-learn`
- `streamlit`

## API Keys

Ensure you have valid API keys for the following services:
- OpenAI
- Anthropic
- Google Gemini
- Hugging Face

Store these keys in the `.env` file as shown in the provided example.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain) for providing the core framework.
- [Hugging Face](https://huggingface.co/) for their powerful models and APIs.
- [Streamlit](https://streamlit.io/) for the interactive UI framework.

Feel free to contribute to this project by submitting issues or pull requests!
