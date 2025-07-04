from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from config.personal_data import user_context

template = """
    Answer the questions:

    Here is the context:
    {context}

    Question:
    {question}

    Answer:

"""

model = OllamaLLM(model="phi4-mini")
prompt = PromptTemplate.from_template(template)
chain = prompt | model

def chat():
    print("Welcome to A-B0T chat")
    context = user_context
    while True:
        question = input("Question: ")
        if question in ["exit", "quit", "bye"]:
            break
        
        result = chain.invoke({"context": context, "question": question})
        print("Bot: ", result)

        # Commented to not exceed the token limit
        #context += f"User: {question}\nBot: {result}\n"

if __name__ == "__main__":
    chat()