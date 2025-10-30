import re
from urllib.parse import urlparse
import tldextract
import validators

def has_ip_address(host):
    return bool(re.match(r'^\d{1,3}(\.\d{1,3}){3}$', host))

def count_digits(s):
    return sum(ch.isdigit() for ch in s)

def extract_features_dict(url: str):
    url = url.strip()
    valid = 1 if validators.url(url) else 0
    try:
        parsed = urlparse(url)
        netloc = parsed.netloc.lower()
        path = parsed.path or ''
        query = parsed.query or ''
        scheme = parsed.scheme
    except Exception:
        netloc = ''
        path = ''
        query = ''
        scheme = ''

    url_len = len(url)
    host_len = len(netloc)
    path_len = len(path)
    digits = count_digits(url)
    hyphens = url.count('-')
    ats = url.count('@')
    dots = url.count('.')
    specials = sum(1 for c in url if not c.isalnum())
    suspicious_tokens = ['login', 'signin', 'secure', 'account', 'update', 'verify', 'confirm', 'bank', 'password', 'reset']
    token_count = sum(1 for t in suspicious_tokens if t in url.lower())
    ext = tldextract.extract(url)
    domain = ext.domain or ''
    subdomain = ext.subdomain or ''
    domain_has_hyphen = 1 if '-' in domain else 0
    subdomain_parts = 0 if subdomain == '' else len(subdomain.split('.'))
    host_only = netloc.split(':')[0]
    ip_flag = 1 if has_ip_address(host_only) else 0

    feats = {
        'valid': valid,
        'scheme': scheme,
        'url_len': url_len,
        'host_len': host_len,
        'path_len': path_len,
        'query_len': len(query),
        'digits': digits,
        'hyphens': hyphens,
        'ats': ats,
        'dots': dots,
        'specials': specials,
        'token_count': token_count,
        'domain_has_hyphen': domain_has_hyphen,
        'subdomain_parts': subdomain_parts,
        'ip_flag': ip_flag
    }
    return feats

def heuristic_score(feats: dict) -> float:
    """Return a heuristic phishing score 0..1 if no ML model is available."""
    score = 0.0
    # strong signals
    score += 0.25 * feats.get('ip_flag',0)
    score += 0.15 * min(feats.get('token_count',0), 3)
    score += 0.10 * (1 if feats.get('domain_has_hyphen',0) else 0)
    score += 0.10 * (1 if feats.get('ats',0) else 0)
    # long URL / many special chars
    if feats.get('url_len',0) > 75:
        score += 0.10
    score += 0.02 * feats.get('specials',0)
    # invalid URL increases suspicion
    score += 0.20 * (1 - feats.get('valid',1))
    # clamp 0..1
    if score < 0: score = 0.0
    if score > 1: score = 1.0
    return round(score, 3)
