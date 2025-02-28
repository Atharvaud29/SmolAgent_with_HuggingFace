import streamlit as st
from dotenv import load_dotenv
import os
from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool

# Load environment variables from .env
load_dotenv()

# Retrieve API keys from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize the model (using HF_TOKEN for authentication)
model = HfApiModel(token=HF_TOKEN)
# Optionally, specify a model_id, e.g., "Qwen/Qwen2.5-Coder-32B-Instruct"
# model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct", token=HF_TOKEN)

# Initialize a CodeAgent with the DuckDuckGoSearchTool as an example tool
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

# Streamlit UI
st.title(" 🤖 SmolAgent AI Chat Application")
st.write("Enter a query below and let the agent work its magic ! ")

# Text input for the user query (default example: arithmetic or recipe)
user_query = st.text_input("Query", "what is 24*9")

if st.button("Get Answer"):
    st.info("Running agent...")
    # Run the agent; this may involve multiple steps internally
    result = agent.run(user_query)
    st.success("Agent Result : ")
    st.write(result)

