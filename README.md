# GenAI FAQ Assistant (LangChain + OpenAI)

## Overview
This project uses Retrieval-Augmented Generation (RAG) with LangChain and OpenAI GPT-4 to answer company-specific FAQs from internal documents.

## Features
- Custom knowledge base from text files
- FAISS for vector search
- LangChain RAG pipeline
- Flask API (`/ask`) for interaction
- Cron-based retrain script

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Add your OpenAI API Key: `export OPENAI_API_KEY="your-key"`
3. Run `python main.py`
4. Use Postman or curl to POST a question to `http://localhost:5000/ask`

## Example Request
```
POST /ask
{
  "question": "How can I apply for leave?"
}
```

## Response
```
{
  "response": "You can apply for leave by filling the HRMS form..."
}
```

## Folder Structure
- `main.py`: Flask API
- `rag_pipeline.py`: RAG logic
- `retrain.py`: Re-index vector DB if docs change
- `data/company_docs/`: Internal knowledge base
- `utils.py`: Logging, etc.