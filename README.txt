PhishScan v2 — Smart URL Inspector (Web App)
------------------------------------------
What you get:
- Flask app (app.py) with endpoints:
  - GET / -> UI
  - POST /api/predict -> JSON prediction, logs to data/history.json
  - GET /api/history -> recent checks

- feature_extractor.py -> extracts features + heuristic scoring
- templates/index.html -> improved UI with chart + history
- static/css/style.css
- data/ (stores history.json)

How to run:
1. Create a virtualenv:
   python -m venv venv
   source venv/bin/activate   (Windows: venv\Scripts\activate)

2. Install dependencies:
   pip install flask joblib pandas tldextract validators scikit-learn

3. (Optional) Place an ML model named 'model.joblib' in project root. The app will use it if available.
   If no model exists, a fast heuristic is used.

4. Run:
   python app.py

5. Open http://127.0.0.1:5000

Notes:
- The app logs the last 200 checks to data/history.json.
- Export history from UI as JSON.
- Model format expected: joblib.dump({'model': clf, 'columns': columns}, 'model.joblib')
