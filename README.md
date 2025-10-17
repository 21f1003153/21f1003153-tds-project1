# 🎯 TDS Project 1 – LLM-Generated Web App  

[![Live on GitHub Pages](https://img.shields.io/badge/🟢%20Live%20on-GitHub%20Pages-blue?style=for-the-badge)](https://21f1003153.github.io/21f1003153-tds-project1/)  

---

## 🧠 Overview  

This repository hosts the implementation for **TDS Project 1**, showcasing a fully automated **LLM-assisted web app generation and deployment pipeline**.  
The system accepts a project *brief*, uses a **Large Language Model (via AIPipe API)** to generate a working app, and auto-deploys it using **GitHub Actions → GitHub Pages**.  

---

## 🚀 Live Deployment  

**🌐 App URL:**  
➡️ [https://21f1003153.github.io/21f1003153-tds-project1/](https://21f1003153.github.io/21f1003153-tds-project1/)  

Each submission automatically:  
1. Generates an HTML+JavaScript app from a new task brief.  
2. Commits and pushes the code to this repository.  
3. Triggers a GitHub Actions workflow that deploys the app to **GitHub Pages**.  
4. Reports status and commit SHA to the evaluator.  

---

## ⚙️ Tech Stack  

| Component | Technology Used |
|------------|-----------------|
| **Backend** | Python (FastAPI + requests) |
| **LLM Service** | AIPipe (OpenAI-compatible endpoint) |
| **Deployment** | GitHub Actions + GitHub Pages |
| **Frontend** | Auto-generated HTML, CSS & JavaScript |

---

## 🔄 Core Flow  

1. **Brief Received** → Input text and attachments describe the app goal.  
2. **LLM Generation** → The `generate_app_from_brief()` helper calls the AIPipe model to produce HTML.  
3. **Save + Commit** → The output is written as `index.html` and committed to the repo.  
4. **Deploy + Notify** → GitHub Pages hosts the site; evaluator receives the URLs and commit SHA.  

---

## 💡 Example Output  

Currently deployed example:  
An **interactive quiz app** with the following features:  
- Radio-button multiple-choice questions  
- Instant scoring on submit  
- Clean, minimal design  
- Automatic hosting via GitHub Pages  

---

## 👩‍💻 Submitted by: 

**Monalisa Kisku**  
🎓 _Student ID: 21f1003153_  
💼 _TDS Project – Stage 2: LLM App Deployment_  

---

### 🏁 Project Highlights  

✅ Fully autonomous LLM workflow  
✅ Live GitHub Pages deployment  
✅ Hands-off CI/CD pipeline  
✅ Minimal, elegant front-end generation  

---

> _“Code created by intelligence, deployed by automation, and understood by curiosity.”_
