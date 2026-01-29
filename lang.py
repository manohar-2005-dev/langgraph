import os
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph

# Set your Groq API key securely
os.environ["GROQ_API_KEY"] = "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"

# This function represents one node in the state graph
def ask_question(state):
    # state is a dictionary that carries data between nodes

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7
    )

    # Invoke the model with a prompt sends the prompt as input to the model and gets the response
    response = llm.invoke("Give me a motivational quote")

    # Return output as dictionary to be used in the state
    return {"output": response.content}

# Create a StateGraph using dictionary-based state
graph = StateGraph(dict)

# Add node to the graph
graph.add_node("ask", ask_question)

# Define entry and finish points
graph.set_entry_point("ask")
graph.set_finish_point("ask")

# Compile the graph into an executable app
app = graph.compile()

# Execute the graph
result = app.invoke({})
print(result)
