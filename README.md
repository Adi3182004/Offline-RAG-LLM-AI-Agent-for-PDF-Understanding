## 🚀 Getting Started (Run from GitHub)

### Short Brief
This project is a **fully offline AI desktop application** that lets you interact with academic PDFs using a **RAG + local LLM pipeline**.  
The GitHub repository contains **source code only**. Build files and binaries are generated locally.

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Adi3182004/Offline-RAG-LLM-AI-Agent-for-PDF-Understanding.git
cd Offline-RAG-LLM-AI-Agent-for-PDF-Understanding


---

2️⃣ Create & Activate Virtual Environment

python -m venv venv
venv\Scripts\activate


---

3️⃣ Install Dependencies

pip install -r requirements.txt


---

4️⃣ Run the Application

python main.py

The desktop UI will launch locally and work completely offline.


---

(Optional) Build Windows EXE

pip install pyinstaller
pyinstaller main.spec

Output:

dist/main/main.exe


---

Notes

dist/, build/, .exe, .dll files are not in GitHub by design

All binaries are reproducible locally

No internet, no cloud APIs, no data leakage
