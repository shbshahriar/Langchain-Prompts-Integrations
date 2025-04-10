from langchain_core.prompts import PromptTemplate  # Importing PromptTemplate to create and manage prompt templates

# Creating a prompt template with specific instructions for summarizing research papers
template = PromptTemplate(
    template="""  # Defining the template string for the prompt
Please summarize the research paper titled "{paper_input}" with the following specifications:  # Instruction to summarize the paper
Explanation Style: {style_input}  # Placeholder for the explanation style (e.g., Beginner-Friendly, Technical)
Explanation Length: {length_input}  # Placeholder for the explanation length (e.g., Short, Medium, Long)
1. Mathematical Details:  # Section for including mathematical details
   - Include relevant mathematical equations if present in the paper.  # Instruction to include equations if available
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  # Instruction to simplify math concepts with code
2. Analogies:  # Section for using analogies
   - Use relatable analogies to simplify complex ideas.  # Instruction to use analogies for better understanding
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  # Instruction to avoid guessing if data is missing
Ensure the summary is clear, accurate, and aligned with the provided style and length.  # Instruction to ensure clarity and alignment with inputs
""",
    input_variables=['paper_input', 'style_input', 'length_input'],  # Defining the input variables for the template
    validate_template=True  # Enabling validation to ensure the template is correctly formatted
)

template.save('template.json')  # Saving the template to a JSON file named 'template.json'