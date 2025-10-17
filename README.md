# 🎯 TDS Project 1 – LLM-Generated Web App  

[![Live on GitHub Pages](https://img.shields.io/badge/🟢%20LIVE%20ON-GitHub%20Pages-blue?style=for-the-badge)](https://21f1003153.github.io/21f1003153-tds-project1/)  

↗️  
↗️  

---

## 🧠 Overview  

This repository hosts the implementation for **TDS Project 1**, showcasing a fully automated **LLM-assisted web app generation and deployment pipeline**.  
The system accepts a project *brief*, uses a **Large Language Model (via AIPipe API)** to generate a working app, and auto-deploys it using **GitHub Actions → GitHub Pages**.  

---

## 🚀 Live Deployment  

| Type                                | URL                                                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **API Endpoint (Vercel)**           | [https://21f1003153-tds-project1.vercel.app/task](https://21f1003153-tds-project1.vercel.app/task)             |
| **GitHub Repository**               | [https://github.com/21f1003153/21f1003153-tds-project1](https://github.com/21f1003153/21f1003153-tds-project1) |
| **Deployed Web App (GitHub Pages)** | [https://21f1003153.github.io/21f1003153-tds-project1/](https://21f1003153.github.io/21f1003153-tds-project1/) |


Each submission automatically:  
1. Generates an HTML+JavaScript app from a new task brief.  
2. Commits and pushes the code to this repository.  
3. Triggers a GitHub Actions workflow that deploys the app to **GitHub Pages**.  
4. Reports status and commit SHA to the evaluator.  

---

## ⚙️ Tech Stack  

| Component                 | Technology Used                     |
| ------------------------- | ----------------------------------- |
| **Backend**               | Python (FastAPI + requests)         |
| **Hosting**               | Vercel                              |
| **Frontend Generation**   | AIPipe / OpenAI API                 |
| **Repository Automation** | GitHub REST API                     |
| **Deployment**            | GitHub Pages                        |
| **Secrets & Config**      | .env + Vercel Environment Variables |


---

## 🔄 Workflow  

1. **POST `/task` (JSON)** → Request includes:  
   - `email`, `secret`, `task`, `round`, `brief`, and optional `attachments`.  
2. **Secret Validation** → The app verifies `email` + `secret` from `secrets.json`.  
3. **App Generation** → Uses the LLM (via AIPipe API) to create a fully working HTML + JavaScript app.  
4. **GitHub Commit + Deploy** → Pushes generated files to the repo and enables GitHub Pages automatically.  
5. **Evaluator Callback** → Sends a JSON response to the evaluator with:  
   - `repo_url`, `pages_url`, and `commit_sha`.  

---

## 💡 Example Output  

Currently deployed example:  
An **interactive quiz app** with the following features:  
- Radio-button multiple-choice questions  
- Scoring logic + “Retake Quiz” button  
- Clean, minimal design  
- Automatic hosting via GitHub Pages  

---

## 👩‍💻 Submitted by: 

**Monalisa Kisku**  
🎓 _Student ID: 21f1003153_  
💼 _TDS Project – LLM App Deployment via FastAPI + Vercel_  

---

### 🏁 Project Highlights  

✅ Fully autonomous LLM workflow  
✅ Automatic deployment & reporting
✅ Secure FastAPI endpoint with verification  
✅ Fully hosted on Vercel + GitHub Pages 

---

> _“Code created by intelligence, deployed by automation, and understood by curiosity.”_
