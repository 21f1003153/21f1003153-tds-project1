# 21f1003153 – TDS Project 1

## 🎯 Project Overview
This project is part of the **TDS (Tools in Data Science)** course at IIT Madras.  
It implements a FastAPI-based endpoint that:

- Accepts a JSON POST request from an evaluator  
- Verifies a secret key  
- Uses an LLM (via AIPipe/OpenAI API) to auto-generate an interactive HTML quiz  
- Publishes it automatically to **GitHub Pages**  
- Reports deployment metadata (repo URL, pages URL, commit SHA) back to the evaluator  

---

## 🚀 Deployment Links
| Type | URL |
|------|-----|
| **Live API (Vercel)** | [https://21f1003153-tds-project1.vercel.app](https://21f1003153-tds-project1.vercel.app) |
| **GitHub Repository** | [https://github.com/21f1003153/21f1003153-tds-project1](https://github.com/21f1003153/21f1003153-tds-project1) |
| **Deployed Web App (GitHub Pages)** | [https://21f1003153.github.io/21f1003153-tds-project1/](https://21f1003153.github.io/21f1003153-tds-project1/) |

---

## ⚙️ Tech Stack
| Component | Description |
|------------|-------------|
| **Framework** | FastAPI (Python) |
| **Hosting** | Vercel |
| **Frontend Generation** | OpenAI (via AIPipe) |
| **Repo Automation** | GitHub REST API |
| **Environment Variables** | Managed via Vercel and `.env` |
| **Version Control** | Git + GitHub |

---

## 📦 API Endpoints

### `GET /`
Returns a simple status check:
```json
{"message": "Server is running fine!"}
