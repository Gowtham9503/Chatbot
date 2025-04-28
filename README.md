# AI Healthcare Assistant Chatbot

 - A Generative AI Medical Chatbot built using Hugging Face, Transformers, Streamlit, and the Google Flan-T5 Small model.
 - This AI Healthcare Assistant is designed to help users get professional answers to their medical queries while recommending consulting a doctor for serious symptoms.




---

## Live Demo:
https://medical-chatbot05.streamlit.app/


## Key Features

- Medical Query Handling: Responds to user health-related queries in a professional manner.

- **Safety-first Approach:** If the model detects serious symptoms, it recommends seeking immediate medical attention.

- **Generative AI:** Uses the Flan-T5 Small model fine-tuned for instruction following tasks.

- **Efficient Resource Management:** Model loading is optimized with Streamlit’s @st.cache_resource.

- **Interactive Frontend:** Built using Streamlit for fast and smooth UI interactions.

- **Preprocessing Prompts:** Custom prompt engineering is used to guide the model for accurate responses.



---

## Tech Stack

**Frontend:** Streamlit

**Backend:** Hugging Face Transformers, PyTorch

**Model:** Google Flan-T5 Small (google/flan-t5-small)

**Deployment:** Streamlit Community Cloud

**Libraries:**

 1. Transformers
 2.  Pytorch
 3.  Streamlit
 
---

## Project Structure

**AI-Healthcare-Assistant**/

├── app.py             # Main Streamlit application

├── requirements.txt   # List of Python dependencies

├── README.md          # Project documentation



---

## How It Works

**Load Model:**

- The Flan-T5 Small model and its tokenizer are loaded via Hugging Face.

- Streamlit’s @st.cache_resource ensures the model is loaded only once per session for efficiency.

**Process Query:**
- User inputs are preprocessed into a structured prompt asking for professional medical advice.


**Generate Response:**

- The model generates a response using text2text generation pipeline.

- If critical symptoms are detected, the model advises users to seek medical consultation.


**Chat Interface:**

- The Streamlit app maintains chat history using st.session_state.

- New user messages and bot responses appear in a continuous chat flow.




---

## Built With

<p align="left">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/HuggingFace-FFCC00?style=for-the-badge&logo=huggingface&logoColor=black" alt="HuggingFace" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/Transformers-4E4E4E?style=for-the-badge&logo=transformers&logoColor=yellow" alt="Transformers" />
</p>

---

## Future Enhancements

- Integration with speech-to-text for voice queries.

- More advanced symptom checking with external medical databases.

- Multi-language support (using multilingual models).

- Adding user authentication and query history.



---

## License

This project is licensed under the MIT License.




---

## *Built with passion for AI and Healthcare! AI Healthcare Assistant*
