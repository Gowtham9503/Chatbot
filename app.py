import os
import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import warnings

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

@st.cache_resource
def load_model():
    try:
        model_name = "google/flan-t5-small"  
        
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        
        model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32,
            device_map=None,  
            trust_remote_code=True
        )
        
        
        chatbot = pipeline(
            task="text2text-generation",
            model=model,
            tokenizer=tokenizer,
            max_length=256
        )
        return chatbot
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def preprocess_query(userinput):
    return f"""Answer the following medical question professionally: {userinput}
              If serious symptoms are mentioned, recommend seeking medical attention.
              Response:"""

def health_chatbot(userinput):
    chatbot = load_model()
    if chatbot is None:
        return "System unavailable. Please try again."
    
    try:
        prompt = preprocess_query(userinput)
        with st.spinner("Analyzing..."):
            response = chatbot(
                prompt,
                max_length=150,
                num_return_sequences=1,
                do_sample=True
            )[0]['generated_text']
        return response.split("Response:")[-1].strip()
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return "Unable to process request."

def main():
    st.title("AI Medical Assistant")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Describe your symptoms"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response = health_chatbot(prompt)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()