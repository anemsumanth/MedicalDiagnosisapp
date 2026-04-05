created this project using uv package manager, which is a modern Python package manager that provides a simple and efficient way to manage dependencies and virtual environments.
go to terminal and run the following command to create a new project using uv:
```bash uv new my_project
``` or ```bash uv new my_project --python 3.10
```or ```bash uv init ```
activate environment using uv:
```bash uv .venv/Scripts/activate
```
install dependencies using uv:
```bash uv add package_name
``` or ```bash uv add -r requirements.txt
```

to store environment variables, create a .env file in the root directory of your project and add your environment variables in the following format:
```bash	OPENAI_API_KEY=your_api_key_here
```

Now as per the architecture of the project we have below functions to be created, 
	1.Symptom Checker: This function will take the user's symptoms as input and return a list of possible diseases or conditions that match those symptoms. It will use a pre-trained machine learning model to make predictions based on the input symptoms.
	2.Diagnosis Module: This function will take the list of possible diseases or conditions from the Symptom Checker and provide a more detailed diagnosis. It will use additional information such as the user's medical history, age, and other relevant factors to narrow down the possibilities and provide a more accurate diagnosis.
	3.PubMed Search: This function will allow users to search for medical research articles and studies related to their symptoms or conditions. It will use the PubMed API to retrieve relevant articles and provide summaries or links to the full texts.
	4.Summarizer

--> Creating a folder as functions and inside that folder we will create separate files for each of the above functions. For example, we can create symptom_checker.py, diagnosis_module.py, pubmed_search.py, and summarizer.py.
	create a constructor file __init__.py inside the functions folder to make it a package. In this file, we will import all the functions from the respective files so that they can be easily accessed when we import the functions package in our main.py file.

## Symptom Extractor Module (`symptom_extractor.py`)

This module is responsible for extracting medical symptoms from user input text. It provides two different approaches for symptom extraction:

### Functions:

#### 1. `extract_symptoms(text: str) -> List[str]`
- **Purpose**: Extracts symptoms from text using regex pattern matching
- **Approach**: Uses regular expressions with word boundaries to identify predefined symptoms
- **Supported Symptoms**: headache, fever, back pain, cough
- **Parameters**: 
  - `text` (str): User input text describing their symptoms
- **Returns**: List of unique symptoms found (as a set, so no duplicates)
- **Example**:
  ```python
  text = "i have back pain and fever"
  symptoms = extract_symptoms(text)
  # Output: ['back pain', 'fever']
  ```

#### 2. `extract_symptoms2(text: str) -> List[str]`
- **Purpose**: Extracts symptoms from text using keyword matching
- **Approach**: Simple string matching against a predefined list of possible symptoms (case-insensitive)
- **Supported Symptoms**: back pain, fever, headache, cough
- **Parameters**: 
  - `text` (str): User input text describing their symptoms
- **Returns**: List of unique symptoms found
- **Example**:
  ```python
  text = "i have back pain and fever"
  symptoms = extract_symptoms2(text)
  # Output: ['back pain', 'fever']
  ```

### Key Features:
- Both functions return **unique symptom lists** (duplicates removed using `set()`)
- **Case-insensitive** matching for better user experience
- **Regex-based approach** (function 1) is more precise with word boundaries
- **Keyword-based approach** (function 2) is simpler and more flexible for variations

### Future Enhancements:
- Expand symptom dictionary to include more medical conditions
- Integrate NLP/ML model for better symptom recognition from free-form text
- Handle symptom variations and synonyms (e.g., "migraine" = "headache")
- Add confidence scores to extracted symptoms



