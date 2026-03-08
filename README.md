🇮🇳 CYBERLEX – Indian Cyberlaw Chatbot

CYBERLEX is an AI-powered chatbot designed to help users understand Indian cybercrime laws. The system analyzes user queries related to cyber offenses and maps them to the most relevant legal sections under the Information Technology Act, 2000 and Indian Penal Code (IPC).

Using Natural Language Processing (NLP) and a structured cyber law knowledge base, the chatbot provides simple explanations of cybercrime laws, legal provisions, and possible penalties.

The goal of this project is to improve cyber law awareness and make legal information more accessible through an interactive conversational interface.

📌 Features

🤖 NLP-based chatbot for cyber law queries

⚖️ Mapping cybercrime scenarios to legal sections

📚 Structured cyber law dataset (cyber_laws.json)

📊 Evaluation system for chatbot accuracy

🧠 Query testing and performance metrics

💬 Simple interface for interacting with the chatbot

🛠 Tech Stack

Python

Natural Language Processing (NLP)

JSON-based legal knowledge base

CSV for evaluation results

Streamlit / Python interface

CYBERLEX
│
├── app.py                    # Main application interface
├── chatbot_backend.py        # Core chatbot logic and NLP processing
│
├── cyber_laws.json           # Cyber law knowledge base
├── test_queries.json         # Sample queries used for testing
│
├── evaluation_with_csv.py    # Script for evaluating chatbot performance
├── evaluation_metrics.txt    # Evaluation metrics and results summary
├── evaluation_results.csv    # CSV output of chatbot evaluation
│
├── package-lock.json         # Dependency tracking
└── README.md                 # Project documentation

⚙️ How It Works

1️⃣ The user asks a cybercrime-related question.

Example:

What is the punishment for identity theft?

2️⃣ The chatbot processes the query using NLP techniques.

3️⃣ The system matches the query with the most relevant cybercrime category stored in cyber_laws.json.

4️⃣ The chatbot returns:

Applicable law section

Description of the offense

Legal explanation

Penalties

📊 Evaluation System

The project includes an evaluation pipeline to measure chatbot performance.

Files used for evaluation:

test_queries.json → Predefined test questions

evaluation_with_csv.py → Evaluation script

evaluation_results.csv → Stores prediction results

evaluation_metrics.txt → Performance summary

This allows the chatbot’s accuracy and response quality to be measured systematically.

💡 Example Queries

Examples of questions the chatbot can answer:
What law applies to hacking in India?
What is the punishment for identity theft?
Is phishing a cybercrime under Indian law?
What happens if someone steals my OTP?

🎯 Future Improvements

Add Machine Learning intent classification

Support multiple Indian languages

Integrate Large Language Models

Improve legal explanation generation

Build a web interface for public use

👨‍💻 Author
Manikandan Nadar