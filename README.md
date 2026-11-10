# Dr Jay's work tracker

One page of what I have been working on: CRM, Exotel, Caredesk, GR8, Training, Marketing and Dashboards, each split into sub-areas, with every point marked done, to do or waiting.

The page is public, but the data is not: `data.enc` is encrypted (PBKDF2-SHA256 + AES-256-GCM) and opens only with the passphrase. The plaintext `me.json` is built outside this repo and must never be committed.

Refresh: rebuild `me.json`, then run `TRACKER_PASS='…' python tracker/seal.py me.json`, then commit `data.enc`.
