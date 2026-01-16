<h1>🧠 Offline AI Agent for PDF Understanding</h1>
<p><strong>RAG + Offline LLM | Desktop-First | Privacy-First</strong></p>

<p>
Hi, I’m <strong>Aditya Andhalkar</strong> 👋<br>
I built this project to solve a real problem I personally faced as a student —
<strong>making semester notes manually is boring, time-consuming, and inefficient</strong>.
</p>

<p>
Instead of rewriting notes again and again, I decided to build software that can
<strong>read, understand, and interact with PDFs like a human tutor</strong> —
completely offline.
</p>

<p>
This repository contains everything you need to run the project on your own machine.
Follow the guide below exactly as written.
</p>

<p><strong>No cloud. No APIs. No data leakage.</strong></p>

<hr>

<h2>🚀 What This Project Does</h2>

<p>
This project converts PDFs (digital, scanned, or handwritten)
into an <strong>interactive AI study companion</strong>.
</p>

<ul>
  <li>Ask questions directly from your PDFs</li>
  <li>Control answer difficulty (easy / medium / hard)</li>
  <li>Generate exam-oriented MCQs with marks</li>
  <li>Maintain per-PDF chat history for revision</li>
  <li>Use voice input (speech → question → answer)</li>
  <li>Export MCQs as PDF for practice</li>
  <li>Runs fully offline as desktop software</li>
</ul>

<hr>

<h2>🧠 Core Architecture (High-Level)</h2>

<ul>
  <li>OCR for scanned & handwritten PDFs</li>
  <li>Academic text chunking</li>
  <li>Sentence embeddings + FAISS vector search</li>
  <li>RAG pipeline to prevent hallucinations</li>
  <li>Offline LLM reasoning using Phi-3 (via Ollama)</li>
  <li>Streamlit-based interactive UI</li>
</ul>

<hr>

<h2>🧭 COMPLETE SETUP GUIDE</h2>
<p><strong>Zero → Working Project (Windows)</strong></p>

<p>
This setup guide is written by me based on real errors, crashes, and debugging issues
I personally faced while building this project.
</p>

<p><strong>Please follow every step line by line. Do not skip or improvise.</strong></p>

<hr>

<h2>✅ Assumptions</h2>

<ul>
  <li>Windows 10 / 11</li>
  <li>Python 3.12.x installed</li>
  <li>You want a fully offline setup</li>
  <li>Ollama + Phi-3 as the local LLM</li>
</ul>

<hr>

<h2>📁 Folder Structure (MANDATORY)</h2>

<p>
Before running anything, your project structure must look exactly like this:
</p>

<pre>
Offline-Handwritten-PDF-AI-Chat/
│
├─ app.py
├─ requirements.txt
│
├─ src/
│   ├─ ocr.py
│   ├─ chunker.py
│   ├─ embeddings.py
│   ├─ vector_store.py
│   ├─ qa.py
│   ├─ llm.py
│   ├─ voice.py
│   └─ export_pdf.py
│
├─ data/
│   ├─ uploaded_pdfs/
│   ├─ extracted_text/
│   └─ faiss_indexes/
│
├─ models/
│
└─ venv/
</pre>

<p><strong>⚠️ If this structure is wrong, the app will break.</strong></p>

<hr>

<h2>1️⃣ Create Virtual Environment</h2>

<p>Open PowerShell in the project root:</p>

<pre>
python -m venv venv
</pre>

<p>Activate it:</p>

<pre>
.\venv\Scripts\Activate.ps1
</pre>

<p>You must see <code>(venv)</code> in the terminal.</p>

<hr>

<h2>2️⃣ Upgrade pip (Safe & Required)</h2>

<pre>
python -m pip install --upgrade pip
</pre>

<hr>

<h2>3️⃣ requirements.txt (Use Exactly This)</h2>

<pre>
streamlit
numpy&lt;2
sentence-transformers
faiss-cpu
easyocr
pillow
pdf2image
pypdf
torch
openai-whisper
sounddevice
scipy
reportlab
</pre>

<p><strong>⚠️ numpy&lt;2 is mandatory.</strong></p>

<hr>

<h2>4️⃣ Install Python Dependencies</h2>

<pre>
pip install -r requirements.txt
</pre>

<p>This may take time. Do not interrupt.</p>

<hr>

<h2>5️⃣ Install Poppler (PDF → Image Conversion)</h2>

<p>Download from:<br>
https://github.com/oschwartz10612/poppler-windows/releases</p>

<p>Extract to:</p>

<pre>
C:\poppler
</pre>

<p>Add this to System PATH:</p>

<pre>
C:\poppler\Library\bin
</pre>

<p>Restart PowerShell and test:</p>

<pre>
pdfinfo -v
</pre>

<hr>

<h2>6️⃣ Install Tesseract OCR (Backup OCR)</h2>

<p>
EasyOCR is the primary OCR engine, but Tesseract is installed as a fallback.
</p>

<p>Download from:<br>
https://github.com/UB-Mannheim/tesseract/wiki</p>

<pre>
tesseract --version
</pre>

<hr>

<h2>7️⃣ Install Ollama (Offline LLM Runtime)</h2>

<p>Download from:<br>
https://ollama.com/download</p>

<p>After installation, reboot once.</p>

<pre>
ollama --version
</pre>

<hr>

<h2>8️⃣ Download Phi-3 Model (One-Time)</h2>

<pre>
ollama pull phi3
</pre>

<p>Test directly:</p>

<pre>
ollama run phi3
</pre>

<p>Type:</p>

<pre>
Explain photosynthesis in one line
</pre>

<p>If you get an answer, the LLM is ready.</p>

<hr>

<h2>9️⃣ Test LLM from Python</h2>

<pre>
python -c "from src.llm import generate; print(generate('Say hello'))"
</pre>

<hr>

<h2>🔟 Test Streamlit (MANDATORY Before EXE)</h2>

<pre>
python -m streamlit run app.py
</pre>

<p>Open manually:</p>

<pre>
http://localhost:8501
</pre>

<p>
If this does not work, do not attempt EXE packaging.
Fix Streamlit first.
</p>

<hr>

<h2>1️⃣1️⃣ Verify RAG (Core Logic)</h2>

<p>Upload a PDF and ask:</p>

<pre>
What is the goal of this meeting?
</pre>

<p>
If the answer comes from the document content:
</p>

<ul>
  <li>OCR works</li>
  <li>Chunking works</li>
  <li>Embeddings work</li>
  <li>FAISS search works</li>
  <li>RAG works</li>
</ul>

<hr>

<h2>1️⃣2️⃣ Voice Input (Optional)</h2>

<pre>
python -c "import sounddevice; print(sounddevice.query_devices())"
</pre>

<p>
Whisper will download its model automatically once.
</p>

<hr>

<h2>1️⃣3️⃣ Common Mistakes (Please Avoid)</h2>

<ul>
  <li>Running EXE before Streamlit works</li>
  <li>Using NumPy 2.x</li>
  <li>Mixing system Python with venv</li>
  <li>Expecting EXE to auto-open browser</li>
</ul>

<hr>

<h2>1️⃣4️⃣ About EXE (Reality Check)</h2>

<p>
Streamlit apps are not traditional desktop GUIs.
When the EXE runs, it starts a local server.
</p>

<p>You must manually open:</p>

<pre>
http://localhost:8501
</pre>

<p>This behavior is expected.</p>

<hr>

<h2>✅ Final Sanity Checklist</h2>

<ul>
  <li>ollama run phi3 works</li>
  <li>python -m streamlit run app.py works</li>
  <li>PDF Q&A works</li>
  <li>MCQs generate</li>
  <li>Internet disconnected → app still works</li>
</ul>

<hr>

<h2>🧠 Final Note from Me</h2>

<p>
This is a real <strong>RAG + Offline LLM system</strong>, not a demo project.
</p>

<p>
Streamlit + EXE is suitable for demos, portfolios, and academic projects.
For production-grade desktop UX, a different stack is recommended.
</p>

<p>
<strong>
Built and maintained by Aditya Andhalkar.<br>
If you’re a student — feel free to learn, extend, and improve this system.
</strong>
</p>
