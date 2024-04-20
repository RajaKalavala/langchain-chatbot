# from langchain.agents import create_csv_agent
from langchain_experimental.agents import create_csv_agent
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
import streamlit as st


def main():

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:
        llm=Ollama(model="llama2")
        agent_executer = create_csv_agent(
            llm, csv_file, verbose=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question:
            with st.spinner(text="In progress..."):
                    try:
                        response = agent_executer.run(user_question,handle_parsing_errors=True)
                        st.write(response)
                    except Exception as e:
                        st.error(f"Failed to process your question. Error: {str(e)}")


if __name__ == "__main__":
    main()