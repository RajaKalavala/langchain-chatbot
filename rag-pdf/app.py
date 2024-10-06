
import streamlit as st
from query_data import query_rag

st.title('PDF Chatbot')
input_text=st.text_input("Search the topic u want")

if input_text:
    response = query_rag(input_text)
    print("Response :",response)
    st.write(response)