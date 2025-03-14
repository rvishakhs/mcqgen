# Educational MCQ Generator App

## 🚀 Live website
https://mcqgen-visakhsr.streamlit.app/

## 📌 Overview
The **Educational MCQ Generator App** is a Streamlit-based web application that dynamically generates multiple-choice questions (MCQs) using OpenAI's **GPT-3.5-Turbo**. This project leverages **LangChain** for efficient LLM chaining, prompt engineering, and structured workflows.

## 🚀 Features
- **Automated MCQ Generation**: Generates high-quality MCQs based on user-provided topics.
- **Read from PDF and Txt files**: creating MCQs from the user given files (PDFs and txt).
- **LLM Chaining**: Enhances response generation through multiple LLM interactions.
- **User-Friendly UI**: Built with **Streamlit** for seamless user experience.
- **Efficient Backend Processing**: Powered by OpenAI’s **GPT-3.5-Turbo** for fast and accurate responses.

## 🛠 Tech Stack
- **Frontend**: Streamlit (Python)
- **Backend**: OpenAI GPT-3.5-Turbo
- **Frameworks/Libraries**:
  - LangChain (LLM Chaining, Prompt Templates)
  - OpenAI API
  - Pandas (Data Handling)

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/mcqgen.git
cd mcqgen
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Set Up OpenAI API Key
Create a `.env` file and add:
```
OPENAI_API_KEY=your_openai_api_key
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run StreamlitAPP.py
```

## 📖 Usage
1. Upload a pdf or txt file with the topic 
2. Enter the subject.
3. Enter the number of questions 
4. Select the difficulty level of questions 
5. Click **Generate MCQs**.

## 🔥 Future Enhancements
- Integration with other LLMs (GPT-4, Claude, or better opensource models)
- Developing more interactive frontend section 
- Export options (CSV, PDF)
- Support for different question formats (True/False, Fill-in-the-blanks)

## 🤝 Contributing
Pull requests are welcome! Open an issue for discussions.

