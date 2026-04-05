# Medical Diagnosis App - Application Explanation

## 1. Project Overview

This repository contains a simple Python-based medical diagnosis app prototype. The current code is organized into:
- `main.py`: entry point
- `functions/diagnosis_symptoms.py`: connects to OpenAI for diagnosis generation
- `functions/symptom_extractor.py`: extracts symptoms from free-text input
- `README.md`: generic uv project guide
- `pyproject.toml`: project metadata and dependency configuration

The app is intended to be a foundation for a medical assistant that can:
- parse a user symptom description
- identify key symptoms
- request a diagnosis and recommendations from an LLM

It is not currently a full production app, but the source files show the intended architecture.

## 2. File and Folder Structure

- `main.py`
  - Contains a simple `main()` function that prints a greeting message.
  - This file is the Python process entry point, but it does not implement any diagnosis flow yet.

- `functions/diagnosis_symptoms.py`
  - Loads environment variables from `.env` using `python-dotenv`.
  - Initializes the OpenAI client with `OPEN_API_KEY`.
  - Defines `get_diagnosis(symptoms: list[str]) -> str`:
    - Builds a prompt with the symptom list.
    - Sends it to `gpt-4` using the OpenAI Chat Completions API.
    - Returns the assistant reply text.

- `functions/symptom_extractor.py`
  - Implements symptom extraction from a text string.
  - Contains two methods:
    - `extract_symptoms(text: str) -> List[str]`
      - Uses regex and word boundaries to find matching symptom keywords.
    - `extract_symptoms2(text: str) -> List[str]`
      - Uses basic substring matching against a predefined symptom list.
  - Both methods return a unique list of symptoms.
  - The module also includes a simple example at the bottom demonstrating extraction from the text `"i have back pain and fever"`.

- `pyproject.toml`
  - Declares the package name, version, Python requirement, and dependencies.
  - Dependencies include:
    - `beautifulsoup4`
    - `fastapi`
    - `lxml`
    - `openai`
    - `python-dotenv`
    - `requests`
    - `uvicorn`

- `README.md`
  - Contains generic instructions for the `uv` package manager.
  - Describes how to create a project, activate the environment, install dependencies, and add a `.env` file.
  - Also contains an architecture plan for future modules such as:
    - Symptom Checker
    - Diagnosis Module
    - PubMed Search
    - Summarizer

## 3. How the Current Code Works

### `main.py`

This file currently does not implement diagnosis logic. It only prints:
```python
Hello from medical-diagnosis-app!
```

This means the current app entry point is a placeholder only.

### `functions/symptom_extractor.py`

This module is responsible for extracting symptoms from a user's input sentence. It currently supports only four symptom keywords:
- `headache`
- `fever`
- `back pain`
- `cough`

Examples:
- `extract_symptoms("I have fever and cough")` returns `['fever', 'cough']`
- `extract_symptoms2("I have back pain and fever")` returns `['back pain', 'fever']`

Limitations:
- The extraction list is small and hardcoded.
- It does not understand synonyms or more complex phrases.
- The second function is case-insensitive but still relies on exact keyword matching.

### `functions/diagnosis_symptoms.py`

This module handles the connection to OpenAI:
- Loads environment variables from `.env`
- Reads `OPEN_API_KEY`
- Creates a `OpenAI` client instance
- Defines `get_diagnosis(symptoms)` which:
  - formats the input symptoms into a prompt
  - asks the OpenAI `gpt-4` chat completion API
  - returns the LLM response text

Prompt used:
```python
Patient has symptoms: {','.join(symptoms)}. suggest possible medical diagnoses suggest me possible cure for the same
```

Note:
- The OpenAI call is synchronous.
- There is no error handling for missing API key or request failure.
- The function assumes the `openai` package interface supports `chat.completions.create`, which matches the older OpenAI Python bindings.

## 4. Required Environment Setup

To run the app, you need:
- Python 3.12 or newer
- A `.env` file in the project root containing:
  ```bash
  OPEN_API_KEY=your_api_key_here
  ```

The current code expects the `OPEN_API_KEY` variable name exactly as shown.

## 5. Dependencies

The project dependencies in `pyproject.toml` are:
- `beautifulsoup4>=4.14.3`
- `fastapi>=0.135.1`
- `lxml>=6.0.2`
- `openai>=2.28.0`
- `python-dotenv>=1.2.2`
- `requests>=2.32.5`
- `uvicorn>=0.42.0`

At present, only `python-dotenv` and `openai` are actively used in the source code.

## 6. Expected Application Flow (Intended Architecture)

Based on the files and notes, the intended app flow is:
1. The user submits a symptom description.
2. The symptom extractor parses the text and returns a list of symptoms.
3. The diagnosis module queries a medical intelligence source (OpenAI GPT-4) to suggest diagnoses and cures.
4. Future modules may add:
   - a symptom checker model
   - a PubMed article search and summarizer
   - a FastAPI server interface

## 7. What Is Missing / Next Steps

The repository is currently a prototype with these gaps:
- `main.py` is not wired to the symptom extraction or diagnosis modules.
- No FastAPI app or web/API interface is implemented.
- No PubMed search or summarizer code exists yet.
- No package-level `functions/__init__.py` exists.
- No tests are included.
- Symptom extraction only handles a fixed small set of keywords.
- No validation or error handling for empty or invalid inputs.

## 8. Recommended Improvements

To make the app functional, add the following:
- `functions/__init__.py` to expose extractor and diagnosis helpers
- A FastAPI server file such as `app.py` or `api.py`
- A `run()` path in `main.py` that calls `extract_symptoms()` and `get_diagnosis()`
- A larger symptom dictionary and better NLP parsing
- Proper OpenAI API error handling
- A PubMed search integration using `requests` and `beautifulsoup4`
- A README with actual usage examples and endpoint details

## 9. Quick Start Example

A minimal usage example for the current modules might look like:

```python
from functions.symptom_extractor import extract_symptoms
from functions.diagnosis_symptoms import get_diagnosis

text = "I have fever and headache"
symptoms = extract_symptoms(text)
print("Extracted:", symptoms)

if symptoms:
    diagnosis = get_diagnosis(symptoms)
    print("Diagnosis:", diagnosis)
```

This script requires a valid `OPEN_API_KEY` in `.env` and the project dependencies installed.

## 10. Summary

This project is a starting point for a medical diagnosis assistant. The current code demonstrates symptom extraction and an OpenAI-based diagnosis step, but it still needs a complete application flow, API layer, and stronger extraction logic.

`readme_app.md` documents the current repository contents, explains how each file works, and points out what is implemented versus what is planned.
