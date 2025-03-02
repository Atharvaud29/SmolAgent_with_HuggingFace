## Smolagent AI chatbot from HuggingFace with the help of Huggingface & OpenAI API's key. 

# Smolagent :

SmolAgents is a cutting-edge library developed by Hugging Face to simplify the creation of intelligent agents capable of performing complex tasks. Designed with a minimalist philosophy, the library encapsulates agent logic in approximately 1,000 lines of code, making it both lightweight and powerful.

# WorkFlow of RAG application :

![image](https://github.com/user-attachments/assets/e17cdc43-124b-430f-bde2-f71b39f984b8)

# Working of Project :

**Step-1** = Install all the below libraries in **requirements.txt** file

    streamlit
    smolagents
    litellm  //LiteLLM simplifies model access, spend tracking and fallbacks. 
    python-dotenv //Read key-value pairs from a .env file and set them as environment variables.

**Step-2** = Create the API key's on HuggingFace and OpenAI in **.env** file

    """
       HF_TOKEN = " Your API key value "
       OPENAI_API_KEY = " Your API key value "
    """

**Step-3** = Now write the code in **app.py** file

3.1 = Import all the libraries

    import streamlit as st
    from dotenv import load_dotenv
    import os
    from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool
    load_dotenv()

3.2 = Retrieve API keys from environment  

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    HF_TOKEN = os.getenv("HF_TOKEN")

3.3 = Initialize the model

    model = HfApiModel(token=HF_TOKEN) 

3.4 = Initialize a CodeAgent with the **DuckDuckGoSearchTool**

    agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

3.5 = Create Streamlit UI 

    st.title(" 🤖 SmolAgent AI Chat Application")
    st.write("Enter a query below and let the agent work its magic ! ")
    if st.button("Get Answer"):
        st.info("Running agent...")
        result = agent.run(user_query)
        st.success("Agent Result : ")
        st.write(result)

**Step-4** = Now run the app.py in treminal in your **IDE** code compiler

    streamlit run app.py

**Output :** 

![Screenshot 2025-03-02 174856](https://github.com/user-attachments/assets/81c9d9a7-14ba-431a-b57f-75c06e87eac2)

## Conclusion :

This project shows that combining Hugging Face’s SmolAgents with OpenAI’s API can yield a powerful yet compact AI chatbot, laying the groundwork for future enhancements.

