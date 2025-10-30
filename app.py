from flask import Flask, render_template, request, jsonify
import os, time, json
from joblib import load
from feature_extractor import extract_features_dict, heuristic_score
import pandas as pd

app = Flask(__name__)
DATA_FILE = os.path.join('data','history.json')
MODEL_PATH = 'model.joblib'  # optional: if present, will be used

model = None
columns = None
if os.path.exists(MODEL_PATH):
    try:
        data = load(MODEL_PATH)
        model = data.get('model', None) if isinstance(data, dict) else data
        columns = data.get('columns', None) if isinstance(data, dict) else None
        print('[+] Loaded ML model from', MODEL_PATH)
    except Exception as e:
        print('[!] Failed to load ML model:', e)

def save_history(entry):
    os.makedirs('data', exist_ok=True)
    history = []
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE,'r',encoding='utf-8') as f:
                history = json.load(f)
        except:
            history = []
    history.insert(0, entry)  # newest first
    # keep last 200
    history = history[:200]
    with open(DATA_FILE,'w',encoding='utf-8') as f:
        json.dump(history, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    payload = request.json or {}
    url = payload.get('url','').strip()
    if not url:
        return jsonify({'error':'No URL provided'}), 400
    feats = extract_features_dict(url)
    score = None
    method = 'heuristic'
    if model is not None and columns is not None:
        try:
            X = pd.DataFrame([[feats[c] for c in columns]], columns=columns)
            score = float(model.predict_proba(X)[0][list(model.classes_).index(1)])
            method = 'ml'
        except Exception as e:
            # fallback
            score = heuristic_score(feats)
            method = 'heuristic'
    else:
        score = heuristic_score(feats)
        method = 'heuristic'
    verdict = 'Phishing' if score >= 0.5 else 'Legitimate'
    entry = {
        'url': url,
        'score': score,
        'verdict': verdict,
        'method': method,
        'features': feats,
        'ts': int(time.time())
    }
    save_history(entry)
    return jsonify(entry)

@app.route('/api/history', methods=['GET'])
def api_history():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,'r',encoding='utf-8') as f:
            h = json.load(f)
    else:
        h = []
    return jsonify(h)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
