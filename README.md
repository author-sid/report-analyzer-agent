# 🩺 Report Analyzer Agent

A modular AI-based medical report analyzer that simulates specialist doctors (Cardiologist, Psychologist, Pulmonologist) and a Multidisciplinary Team (MDT) to provide expert assessments using LLMs. Built with LangChain, Streamlit, and runs locally using open-source LLMs via Ollama.

---

## 🚀 Features

- 📂 Upload `.txt` medical reports through a web UI
- 🧠 Role-based simulated analysis by:
  - Cardiologist
  - Psychologist
  - Pulmonologist
  - Multidisciplinary Team (combined review)
- 💬 Returns structured, human-readable diagnostic insights
- 💾 Automatically saves analysis in `results/` folder using the patient's name
- 🌐 Streamlit-based browser UI (no need to write code)
- 🔓 Entirely local & private using [Ollama](https://ollama.com/) + open-source LLMs

---

## 🧰 Tech Stack

- Python 3.10+
- LangChain
- Streamlit
- Ollama (local LLM runtime)
- LLaMA 3 / Mistral / Phi-3 (or any other compatible model)

---

## 📁 Project Structure

```
ReportAnalyzerAgent/
├── agents/
│   ├── base_agent.py         # Core Agent class with prompt logic
│   └── roles.py              # Role-specific agent subclasses
├── Medical reports/          # Optional folder for test report files
├── results/                  # Outputs saved with patient-based filenames
├── app.py                    # Streamlit UI entry point
├── main.py                   # CLI version for local testing
├── requirements.txt          # Python dependencies
└── README.md                 # Project info
```

---

## 🖥️ Local Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/report-analyzer-agent.git
cd report-analyzer-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama

Download from: https://ollama.com  
Then run:

```bash
ollama pull llama3
ollama run llama3
```

> Make sure Ollama is running before starting the app.

---

## 🧪 Run the Application

### Option A: Streamlit UI (Recommended)

```bash
streamlit run app.py
```

- Upload a `.txt` report
- Click **Analyze Report**
- View structured results in-browser

### Option B: Command Line

Place your `.txt` file in `Medical reports/` and run:

```bash
python main.py
```

---

## 📤 Output

- Results are saved to the `results/` folder
- Filenames are auto-generated based on patient name
- Example: `results/Michael_Johnson.txt`

---

## 📌 Sample Input Format

Your input `.txt` should contain fields like:

```
Name: Michael Johnson
Age: 29
Gender: Male
Chief Complaint: ...
Medical History: ...
Lab Results: ...
```

---

## 🌐 Deployment

You can deploy this app on:
- **Streamlit Cloud** *(requires replacing local LLM with OpenAI or OpenRouter model)*
- **Hugging Face Spaces** *(using Gradio + Transformers)*

> Ollama-based local models only run on your machine — they are not cloud-hosted.

---

## 💡 Future Enhancements

- Add more specialist roles (Neurologist, Endocrinologist)
- Parse PDFs or medical imaging reports
- Export results as PDFs
- Deploy cloud version with OpenRouter LLM

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Credits

- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com)
- [Streamlit](https://streamlit.io)
