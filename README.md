# 🛡️ CyberGuard: Intelligent Phishing URL Detection System

CyberGuard is a **smart web application** designed to protect users from phishing attacks by analyzing URLs using **Machine Learning**.  
Built with **Python (Flask)** and a trained ML model, it provides **instant, real-time phishing detection** through a clean and minimal web interface.

---

## 🌍 Overview

Phishing websites are one of the most common cyber threats today.  
CyberGuard helps prevent **credential theft and data breaches** by scanning URLs and predicting whether they are **safe or malicious** — before the user even clicks on them.

This project combines **cybersecurity principles** with **machine learning intelligence** to create a **real-world, practical defense tool**.

---

## ⚙️ Tech Stack

| Layer | Technology |
|------|-----------|
| 💻 Frontend | HTML5, CSS3, JavaScript |
| 🔥 Backend | Python (Flask) |
| 🧠 Machine Learning | Scikit-learn, Pandas, Joblib |
| 📂 Dataset | Public Phishing & Legitimate URL Dataset |
| 🧰 Others | TLDExtract, Validators, Feature Engineering |

---

## 🚀 Features

✅ Detects whether a given URL is **Legitimate or Phishing**  
✅ Simple and intuitive **web interface**  
✅ Lightweight **Flask backend** (easy to run locally)  
✅ Uses **real URL-based features** (length, domain, symbols, etc.)  
✅ Trained ML model for **high-accuracy predictions**  
✅ Easily extendable for future cybersecurity projects  

---

## 🧩 Project Structure

CyberGuard/
│
├── app.py # Flask web application

├── feature_extractor.py # URL feature extraction logic

├── data/ # Dataset (optional)

├── templates/

│ └── index.html # Frontend HTML page
├── static/

│ └── css/ # Stylesheets

├── model.joblib # Trained ML model (optional)

└── README.md

yaml
Copy code

---

## ⚡ How to Run Locally

### Step 1️⃣ – Clone the Repository
```bash
git clone https://github.com/Anwita0106/CyberGuard.git
cd CyberGuard
Step 2️⃣ – Create a Virtual Environment
bash
Copy code
python -m venv venv
Activate it:

Windows

bash
Copy code
venv\Scripts\activate
Mac/Linux

bash
Copy code
source venv/bin/activate
Step 3️⃣ – Install Dependencies
bash
Copy code
pip install -r requirements.txt
If requirements.txt is not available, install manually:

bash
Copy code
pip install flask pandas joblib scikit-learn tldextract validators
Step 4️⃣ – Run the Application
bash
Copy code
python app.py
Step 5️⃣ – Open in Browser
👉 Visit: http://127.0.0.1:5000/
Enter a URL and get instant phishing detection results ⚡



🌍 Use Cases
🛡️ Phishing detection for end users
🌐 Browser-based URL safety checking
🏢 Enterprise cybersecurity tools
🎓 Educational cybersecurity & ML projects

🧑‍💻 Developer
👩‍💻 Anwita Padhi
Passionate about Cybersecurity, Machine Learning, and Web Development

❤️ Contributions
Contributions, issues, and feature requests are welcome!
Feel free to fork the repository and submit a pull request 💪

