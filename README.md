
# 🛠️ YAML to JSON Utility

This utility parses a Docker Compose YAML file and converts it into JSON format using Python.  

It uses the `docker-compose.yaml` from one of my full stack projects (**File-Vault: Smart File Upload System**) as a real-world example.

---

## 📦 About File-Vault

[File-Vault](https://github.com/Saicharan1505/File-Vault) is an AI-assisted smart file upload system built with **React, Django REST API**, and **Cursor AI**.

- 🚀 Built an AI-assisted upload platform to streamline developer workflows and accelerate feature delivery.  
- 💾 Engineered file deduplication with content hashing (SHA-256) for optimized storage and scalability.  
- 🔎 Designed dynamic search and filtering across multiple attributes for faster file retrieval.  

This repo uses File-Vault’s Docker Compose configuration to demonstrate YAML parsing.

---

## ⚙️ How It Works

- Reads `docker-compose.yaml`
- Converts it to JSON format
- Saves the result as `docker-compose.json`

---

## 🚀 Quick Start

### 1️⃣ Install dependencies
```bash
pip install pyyaml
python .\parse_and_transform.py
