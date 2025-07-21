# 📚 Personal Local Tutor Chatbot

A lightweight(?), local chatbot app built for **desktop/laptop use** — perfect for study help, reviews, or just chatting. It runs entirely offline using open-source LLMs.

Before you begin I would like to say that the model I used is the best suited for this project but if you wish to change it to your likes then so be it.
---

## 🚀 Features

- 💬 Local chatbot powered by [Ollama](https://ollama.com)
- 🧠 Custom memory via `memory.json`
- 📓 Chat history saved in `chat_history.json`
- 🧠 Uses models tested/downloaded from [LM Studio](https://lmstudio.ai/)
- 🖥️ Built for desktop/laptop (not mobile optimized)
- 🔧 Minimal setup — great for personal/local use

---

## 🎞️ Live Demo

Here’s what it looks like running locally:

![Chatbot Demo](demo.gif)

---
## 🖥️ System Requirements

> 💡 This chatbot was developed and tested on a **laptop with the following specs**:
>
> - Intel Core **i5-13420H**
> - **RTX 4050** GPU (Laptop variant)
> - **16GB RAM**
> - Windows 11
>
> While the app is lightweight, **running local LLMs** (like NeuralHermes 2.5) with good performance requires at least:
>
> - ✅ **Quad-core CPU or better**
> - ✅ **8–16GB RAM** minimum (16GB recommended)
> - ✅ Optional: **Discrete GPU** (NVIDIA/AMD) for smoother model loading & interaction
>
> 📝 If you're using a lower-end machine, try **smaller quantized models** (e.g. Q4_0, Q5_K_M) for better performance.

## 🧠 LM Studio-First Workflow (Preferred)

You can test models in **LM Studio** first, then use the same model inside your chatbot via Ollama + Modelfile.

### 🔹 Step 1: Test in LM Studio

1. Install LM Studio → [https://lmstudio.ai](https://lmstudio.ai)
2. Open LM Studio → go to **Models** tab
3. Download a model like `NeuralHermes 2.5 Q4_K_M.gguf`
4. Try it in their chat UI to confirm it fits your needs

### 🔹 Step 2: Locate Your Downloaded Model

```
Windows: C:\Users\<you>\.lmstudio\models
macOS: ~/Library/Application Support/LM Studio/models
```

### 🔹 Step 3: Create a `Modelfile`

In your chatbot project folder, create a `Modelfile` like this:

```Dockerfile
FROM ./models/neuralhermes-2.5.Q4_K_M.gguf
PARAMETER temperature 0.7
```

> 📌 Place the `.gguf` file in a folder called `models/` inside your chatbot directory or update the path accordingly.

### 🔹 Step 4: Import Model to Ollama

```bash
ollama create mychatmodel -f Modelfile
ollama run mychatmodel
```

You now have a working local model, ready for chat.

---

## 🔧 Technologies Used

- 🐍 Python 3.10.11 (recommended) → [Download](https://www.python.org/downloads/release/python-3100/)
- ⚙️ Flask (`pip install flask`)
- 🤖 Ollama → [https://ollama.com](https://ollama.com)
- 🧠 LM Studio → [https://lmstudio.ai](https://lmstudio.ai)
- 🖥️ Visual Studio Code or any IDE you like → [https://code.visualstudio.com](https://code.visualstudio.com)

---

## 📁 Folder Structure

```
├── app.py              # Flask backend
├── brain.py            # Handles model logic
├── templates/
│   └── index.html      # UI layout
├── static/
│   └── style.css       # Styling
├── memory.json         # Memory per session
├── chat_history.json   # Full conversation logs
├── Modelfile           # LLM import config
├── demo.gif            # Demo recording
```

---

## 🛠️ How to Set It Up

### 1. Clone the Project

```bash
git clone https://github.com/yourusername/personal-tutor-chatbot.git
cd personal-tutor-chatbot
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\\Scripts\\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Start Ollama + Run Flask App

- Make sure you’ve imported your model via `ollama create`
- Then run:

```bash
python app.py
```

### 5. Open in Browser

Visit:

```
http://localhost:11434
```

---

## ✅ Check Your Versions

Use these to ensure everything's set up:

```bash
python --version
flask --version
ollama --version
```

---

## 📬 Contact

Made with ❤️ by **yubedaoneineed/Pranziss(got suspended)**

For questions or ideas, feel free to fork, star ⭐, or reach out!
