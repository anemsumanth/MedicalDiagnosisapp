# Medical Diagnosis App - Comprehensive Documentation

## 📋 **Project Structure**

### **Core Architecture**
Your app is a **FastAPI-based medical diagnosis assistant** that uses OpenAI GPT-4 and PubMed to provide medical insights.

### **Main Entry Points**
- **app.py** - FastAPI server with a `/diagnosis` endpoint
- **main.py** - Basic CLI entry point

### **Key Workflow (in app.py)**
```
User Input (symptoms) 
  ↓
1. Extract symptoms (regex parsing)
  ↓
2. Get AI diagnosis (GPT-4)
  ↓
3. Fetch PubMed articles (medical research)
  ↓
4. Summarize articles (GPT-4)
  ↓
Return JSON response
```

---

## 🔧 **Functions Directory** (Core Logic)

### **1. symptom_extractor.py**
- **Purpose**: Extract medical symptoms from text input
- **Method**: Regex pattern matching for hardcoded symptoms (headache, fever, nausea, fatigue, pain)
- **Output**: List of detected symptoms
- **Limitation**: Only recognizes 5 preset symptoms

### **2. diagnosis_symptoms.py**
- **Purpose**: Generate medical diagnosis based on symptoms
- **Uses**: OpenAI GPT-4 API
- **Input**: List of symptoms
- **Output**: AI-generated diagnosis and treatment suggestions
- **Requires**: `.env` file with `OPENAI_API_KEY`

### **3. pubmed_articles.py**
- **Purpose**: Fetch medical research articles from PubMed
- **API Used**: NCBI Entrez E-utilities (free public API)
- **Steps**:
  1. Search PubMed database for relevant articles
  2. Parse XML response to extract metadata
  3. Extract title, abstract, authors, publication date, URLs
- **Fallback**: Returns mock data if API fails or no results found
- **Output**: List of article objects with metadata

### **4. summerize_pubmed.py**
- **Purpose**: Summarize medical articles using AI
- **Uses**: OpenAI GPT-4 API
- **Input**: Medical text (first 3000 chars from articles)
- **Output**: Condensed summary in plain language
- **Requires**: `.env` file with `OPENAI_API_KEY`

---

## 🌐 **API Endpoint**

### **POST /diagnosis**
```json
Request: { "description": "I have a headache and fever" }

Response: {
  "symptom": ["headache", "fever"],
  "diagnosis": "...(GPT-4 response)...",
  "pubmed_summary": "...(summarized articles)..."
}
```

---

## 📦 **Dependencies** (requirements.txt)
- **openai** - GPT-4 API integration
- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **python-dotenv** - Environment variable management
- **beautifulsoup4** - XML/HTML parsing
- **requests** - HTTP requests
- **pytest** - Testing framework

---

## 🔑 **Configuration**
- **`.env` file** - Stores `OPENAI_API_KEY` (must be created locally, not in git)
- **`.gitignore`** - Protects sensitive files
- **Host**: 0.0.0.0, **Port**: 8080

---

## 🚀 **To Run**
```bash
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

Then POST to `http://localhost:8080/diagnosis` with symptom descriptions.

---

## ⚠️ **Current Limitations**
1. Symptom extraction only recognizes 5 hardcoded keywords
2. Requires OpenAI API key (costs money)
3. Relies on external APIs (PubMed, OpenAI)
4. No user authentication
5. No database for storing results
