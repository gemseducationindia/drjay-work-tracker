"""Encrypt Jay's personal tracker data for this Pages site (public repo, so only ciphertext is ever committed).

    TRACKER_PASS='...' python tracker/seal.py /path/to/me.json

me.json is built outside the repo from Outlook mail + calendar and must never be committed.
Output: site/me/data.enc = JSON {salt, iter, iv, ct} (base64), PBKDF2-SHA256 -> AES-256-GCM over gzip(JSON).
"""
import base64, gzip, json, os, secrets, sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

pw = os.environ["TRACKER_PASS"].encode()
raw = gzip.compress(json.dumps(json.load(open(sys.argv[1])), separators=(",", ":")).encode())
salt, iv, it = secrets.token_bytes(16), secrets.token_bytes(12), 310000
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=it).derive(pw)
b = lambda x: base64.b64encode(x).decode()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data.enc")
json.dump({"salt": b(salt), "iter": it, "iv": b(iv), "ct": b(AESGCM(key).encrypt(iv, raw, None))}, open(out, "w"))
print("sealed", len(raw), "bytes ->", os.path.normpath(out))
