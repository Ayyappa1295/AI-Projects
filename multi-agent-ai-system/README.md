# 🤖 Multi-Agent AI System

A Python-based Multi-Agent AI application where multiple specialized AI agents collaborate to solve complex user tasks.

## 🚀 Overview

Traditional AI applications often use a single AI model to handle an entire task.

This project uses a **Multi-Agent Architecture**.

Different AI agents are assigned different responsibilities and work together through an **Orchestrator Agent**.

### Agent Workflow

```text
                    USER
                      │
                      ▼
              ┌───────────────┐
              │ ORCHESTRATOR  │
              │     AGENT     │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ RESEARCH      │
              │ AGENT         │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ CODING        │
              │ AGENT         │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ WRITER        │
              │ AGENT         │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ REVIEW        │
              │ AGENT         │
              └───────┬───────┘
                      │
                      ▼
                 FINAL ANSWER
```

## ✨ Features

* Multi-agent AI architecture
* Specialized AI agents
* Agent orchestration
* Research generation
* Technical solution generation
* AI-assisted writing
* Automatic response review
* Streamlit web interface
* Environment-variable based API configuration
* Modular Python architecture

## 🧠 Agents

### 1. Orchestrator Agent

Coordinates the complete workflow and sends the task through the appropriate agents.

### 2. Research Agent

Analyzes the task and creates structured research notes.

### 3. Coding Agent

Creates technical solutions and programming implementations.

### 4. Writer Agent

Converts the research and technical solution into a structured response.

### 5. Review Agent

Reviews the generated response and produces an improved final answer.

## 🛠️ Technologies

* Python
* OpenAI API
* Streamlit
* Prompt Engineering
* Multi-Agent Systems
* LLMs
* Environment Variables
* Git
* GitHub

## 📁 Project Structure

```text
multi-agent-ai-system/
│
├── agents/
│   ├── __init__.py
│   ├── orchestrator.py
│   ├── research_agent.py
│   ├── coding_agent.py
│   ├── writer_agent.py
│   └── review_agent.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── utils/
│   ├── __init__.py
│   └── llm.py
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Ayyappa1295/multi-agent-ai-system.git
```

Move into the project:

```bash
cd multi-agent-ai-system
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 API Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Never upload your `.env` file to GitHub.

## ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 Example Tasks

You can enter tasks such as:

```text
Create a Python expense tracker.
```

```text
Build a student management system using Java.
```

```text
Explain how RAG works and create a simple Python implementation.
```

```text
Create a SQL database for an e-commerce company.
```

```text
Design a full-stack project architecture for a hospital management system.
```

## 🔄 How It Works

### Step 1 — User Input

The user enters a task through the Streamlit interface.

### Step 2 — Research

The Research Agent analyzes the task and creates useful research notes.

### Step 3 — Technical Solution

The Coding Agent uses the task and research notes to create a technical solution.

### Step 4 — Writing

The Writer Agent converts the information into a structured response.

### Step 5 — Review

The Review Agent checks the generated response and improves it.

### Step 6 — Final Response

The application displays the reviewed final answer.

## 🎯 Learning Objectives

This project demonstrates:

* Large Language Models
* Prompt Engineering
* AI Agents
* Multi-Agent Architecture
* Agent Orchestration
* AI workflow design
* Python modular programming
* API integration
* Streamlit application development

## 🔮 Future Improvements

Possible future versions can add:

* RAG
* Vector databases
* Long-term agent memory
* Web search tools
* File/document analysis
* Tool calling
* Database agents
* LangGraph
* Agent-to-agent communication
* Parallel agent execution
* Authentication
* Conversation history
* Agent monitoring
* Cost tracking
* Production deployment

## 📌 Portfolio Description

**Multi-Agent AI System** is an AI-powered application that coordinates multiple specialized agents to research, develop, write, review, and deliver solutions to complex user tasks. The project demonstrates practical implementation of LLMs, prompt engineering, agent orchestration, Python, API integration, and Streamlit.

## 👨‍💻 Author

**Ayyappa1295**

GitHub:

https://github.com/Ayyappa1295
