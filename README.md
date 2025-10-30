🛡️ CyberGuard: Intelligent Phishing URL Detection System

CyberGuard is a smart web app designed to protect users from phishing attacks by analyzing and detecting malicious URLs using Machine Learning.
Built with 🧠 Python (Flask) and a trained ML model, it provides instant results and real-time phishing detection through a clean, minimal web interface.

🌍 Overview

Phishing websites are one of the most common forms of cyber threats today.
CyberGuard helps prevent data breaches and credential theft by scanning URLs and predicting whether they are safe or malicious — before the user even clicks on them.

This project combines cybersecurity principles with machine learning intelligence to create a real-world applicable defense tool.

⚙️ Tech Stack
Layer	Technology
💻 Frontend	HTML5, CSS3, JavaScript
🔥 Backend	Python (Flask)
🧠 Machine Learning	Scikit-learn, Pandas, Joblib
📂 Dataset	Public Phishing & Legitimate URL dataset
🧰 Others	TLDExtract, Validators, Feature Engineering
🚀 Features

✅ Detects if a given URL is Legitimate or Phishing
✅ Simple, intuitive web interface
✅ Lightweight Flask backend — easy to run locally
✅ Uses real URL-based features (length, domain, symbols, etc.)
✅ Trained ML model for high accuracy predictions
✅ Easily extendable for future cybersecurity projects

🧩 Project Structure
CyberGuard/
│
├── app.py                   # Flask web app
├── feature_extractor.py     # Extracts URL-based features
├── data/                    # Dataset (optional)
├── templates/
│   └── index.html           # Frontend page
├── static/
│   └── css/                 # Stylesheets
├── model.joblib             # Trained ML model (optional)
└── README.md

⚡ How to Run Locally
Step 1️⃣ – Clone this repository
git clone https://github.com/Anwita0106/CyberGuard.git
cd CyberGuard

Step 2️⃣ – Create a virtual environment
python -m venv venv


Activate it:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Step 3️⃣ – Install dependencies
pip install -r requirements.txt


(If requirements.txt is not available, install manually)

pip install flask pandas joblib scikit-learn tldextract validators

Step 4️⃣ – Run the app
python app.py

Step 5️⃣ – Visit in browser

👉 Open http://127.0.0.1:5000

Enter a URL — get instant results! ⚡

🧠 Future Enhancements

✨ Deploy on cloud (Heroku / Render / HuggingFace Spaces)
✨ Add real-time threat API integration
✨ Build browser extension for instant URL checking
✨ Enhance ML model with deep learning (LSTM)

🧑‍💻 Developer

👩‍💻 Anwita Padhi
💬 Passionate about Cybersecurity, AI, and Web Development
🌐 GitHub Profile

❤️ Contributions

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request 💪
