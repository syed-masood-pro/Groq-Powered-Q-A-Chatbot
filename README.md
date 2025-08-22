# Groq-Powered Q&A Chatbot

## 📝 Table of Contents
- [📌 About the Project](#-about-the-project)
- [✨ Key Features](#-key-features)
- [🛠️ Requirements](#️-requirements)
- [🚀 How to Run](#-how-to-run)
- [🖼️ Sample Interface](#-sample-interface)
- [📄 License](#-license)
- [📧 Contact](#-contact)
---
## 📌 About the Project

This project is a simple, yet powerful, Q&A chatbot built using **Streamlit** for the user interface and **Groq's high-speed inference engine** for lightning-fast responses. It leverages **LangChain** to handle the conversational logic and prompt management. The goal is to create a functional and customizable chatbot that demonstrates the seamless integration of these tools.

---

## ✨ Key Features
  * **Fast Inference:** Utilizes Groq's low-latency inference engine for near-instantaneous AI responses.

  * **Dynamic Configuration:** Users can select from various supported LLM models (Llama 3, Gemma 2, etc.) and adjust generation parameters like `temperature` and `max_tokens` via a user-friendly sidebar.

  * **Secure API Handling:** Uses a `.env` file to securely manage API keys, ensuring credentials are not exposed in the codebase.

  * **LangChain Integration:** Employs LangChain for a structured approach to building the LLM chain, including a system prompt template and output parsing.

---
## 🛠️ Requirements

You can install all necessary Python packages by running the following command:

```bash 
pip install -r requirements.txt
```
---

## 🚀 How to Run

**1. Clone the Repository**
```
git clone https://github.com/syed-masood-pro/Groq-Powered-Q-A-Chatbot.git
cd Groq-Powered-Q-A-Chatbot
```
**2. Set Up Your Environment**

Create a file named .env in the root directory of the project. Do not commit this file to Git. Add your Groq and LangChain API keys to this file:
```
GROQ_API_KEY="your_groq_api_key_here"
LANGCHAIN_API_KEY="your_langchain_api_key_here"
```

**3. Run the Streamlit App**

From your terminal, run the following command to start the application:
```
streamlit run main.py
```
The app will open automatically in your web browser, and you can start interacting with the chatbot.

---

## 🖼️ Sample Interface

**Example Conversation**

<img width="954" height="474" alt="proj1" src="https://github.com/user-attachments/assets/b1288183-62f8-42ff-91eb-081c562321a5" />

<img width="956" height="472" alt="proj2" src="https://github.com/user-attachments/assets/8566f775-599b-41bf-9748-07249ad6962f" />

---

## 📄 License

This project is licensed under the MIT License.

---

## 📧 Contact
**Syed Masood**

✉️ [syedmasood.pro@gmail.com](syedmasood.pro@gmail.com)

🔗 [GitHub Profile](https://github.com/syed-masood-pro/)

💼 [LinkedIn](https://www.linkedin.com/in/syed-masood-pro/)
