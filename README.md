# Fleming
Fleming is an AI-driven medical assistant that provides safe, guideline-based health advice and connects users to licensed doctors for free or paid consultations, ensuring privacy, compliance, and reliable clinical guidance.
# Fleming — Local SQLite MVP (FastAPI)

This is a **local-only** MVP: triage endpoints (FEVER), doctor directory (CSV seed), and admin references.

## Prereqs
- Python 3.10+

## Setup
```bash
cd /mnt/data/fleming_backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Seed doctors
```bash
python seed_doctors.py
```

## Run API
```bash
uvicorn app.main:app --reload --port 8000
```

## Test endpoints

### Health
```bash
curl http://127.0.0.1:8000/health
```

### Start triage (fever)
```bash
curl -X POST http://127.0.0.1:8000/triage/start -H "Content-Type: application/json" -d '{"complaint":"fever"}'
```

### Answer step
Replace TRIAGE_ID with the value you got from /start.
```bash
curl -X POST http://127.0.0.1:8000/triage/answer -H "Content-Type: application/json" -d '{"triage_id":"TRIAGE_ID","answer":"no"}'
```

### Finish triage (generates PDF)
```bash
curl -X POST http://127.0.0.1:8000/triage/finish -H "Content-Type: application/json" -d '{"triage_id":"TRIAGE_ID"}'
# PDF saved in ./summaries/<encounter_id>.pdf
```

### List doctors
```bash
curl "http://127.0.0.1:8000/doctors"
curl "http://127.0.0.1:8000/doctors?is_free=true"
```

### Admin: add fever references (ICMR/AIIMS)
```bash
curl -X POST http://127.0.0.1:8000/admin/references -H "Content-Type: application/json" -d '{
  "complaint": "fever",
  "source": "ICMR/AIIMS",
  "version": "2024",
  "body": "ICMR/AIIMS fever assessment summary (placeholder)."
}'
```

### Admin: list references
```bash
curl "http://127.0.0.1:8000/admin/references?complaint=fever"
```
