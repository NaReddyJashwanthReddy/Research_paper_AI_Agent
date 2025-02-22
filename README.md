# AI Research Paper Assistant

## Project Overview
The AI Research Paper Assistant is a **Retrieval-Augmented Generation (RAG) model** designed to assist researchers by retrieving and generating relevant information from research papers. The system integrates **Streamlit for the user interface, ChromaDB for vector storage, and DeepSeek R1 for response generation**.

## Features
- **Chat-based Research Assistance**: Users can input research-related queries and receive relevant information from research papers.
- **Retrieval-Augmented Generation (RAG)**: The assistant retrieves information from stored research papers and generates precise responses.
- **ChromaDB for Vector Storage**: Research papers are embedded and stored in ChromaDB, allowing efficient retrieval.
- **DeepSeek R1 for LLM Generation**: Uses DeepSeek R1 to generate high-quality responses without hallucinations.

## Technologies Used
- **Streamlit**: Interactive UI for research query handling.
- **ChromaDB**: Vector database for storing and retrieving research data.
- **SentenceTransformer (all-MiniLM-L6-v2)**: Used for embedding research papers.
- **LangChain & ChatGroq**: Framework for prompting and generating responses using LLM.
- **PyPDFLoader**: Extracts content from research PDFs.
- **Python Libraries**: NumPy, dotenv, torch, random, os, wave, pyaudio.

## Setup Instructions

### 1. Install Dependencies
Ensure you have Python installed, then install required packages:
```sh
pip install streamlit chromadb langchain-groq sentence-transformers langchain_community torch pyaudio numpy python-dotenv
```

### 2. Set Up API Keys
Create a `.env` file and add your `GROQ_API` key:
```sh
GROQ_API=your_api_key_here
```

### 3. Load Research Papers
- Place research PDFs in the appropriate directory.
- The system automatically ingests PDFs into ChromaDB if they are not already stored.

### 4. Run the Application
Start the Streamlit app:
```sh
streamlit run app.py
```

## How It Works
1. **User Inputs Query**: The user types a research-related question in the chat interface.
2. **Retrieve Relevant Research Data**: The system retrieves the most relevant content from the embedded research papers stored in ChromaDB.
3. **Generate Response Using LLM**: DeepSeek R1 generates a refined response based on the retrieved content.
4. **Display Response**: The response is displayed in the chat window.

## File Structure
```
📂 AI_Research_Assistant
│── app.py  # Main Streamlit application
│── model_llm.py  # LLM response generation logic
│── rad.py  # Retrieval logic using ChromaDB
│── my_chroma_db/  # Persistent vector database
│── .env  # API Key configuration
│── requirements.txt  # Dependencies
│── README.txt  # Project Documentation
```

## Notes
- The model is designed **not to hallucinate** and generates only necessary information.
- The database is checked before ingestion to **avoid redundant embeddings**.
- The system retrieves **20-30 results per query** to enhance response accuracy.

## Future Improvements
- Add more LLM options for comparison.
- Improve retrieval filtering to prioritize **most recent** papers.
- Implement better summarization techniques for research output.

## Troubleshooting
- **Issue: No Response from LLM**
  - Ensure `GROQ_API` key is correctly set.
  - Check if ChromaDB contains stored documents.
- **Issue: Incorrect Retrieval Results**
  - Verify that research papers are correctly loaded.
  - Adjust retrieval settings (`n_results` in `retrive_data`).
