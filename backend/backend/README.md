# ACTA Backend — Step 5

This starter verifies that FastAPI runs and can read organization data from Supabase.

## Requirements
- Python 3.11+ recommended
- Supabase project with ACTA tables and seed data

## Setup (run from repository root)
```bash
cd backend
python -m venv .venv
```

Activate:
- Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install and create local env:
```bash
pip install -r requirements.txt
copy .env.example .env
```
On macOS/Linux use `cp .env.example .env`.

Fill `.env` with `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY`. Find the project URL and key in Supabase project settings/API keys. Use the backend-only secret/service-role key only on the server: it bypasses RLS. Never expose it to frontend code or commit `.env` to GitHub.

## Run
```bash
uvicorn app.main:app --reload
```
Visit:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/api/divisions` (expect 8)
- `http://127.0.0.1:8000/api/employees` (expect 16)
- `http://127.0.0.1:8000/api/projects` (expect 1)

If an endpoint returns HTTP 503, verify environment variables, table names, and seed data.

## Scope
This is only a connection test. Audio/PPT ingestion, AI extraction, task assignment, Trello, and Slack will be added in later steps.
