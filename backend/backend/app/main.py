from fastapi import FastAPI, HTTPException
from app.db.supabase import get_supabase_client

app = FastAPI(title="ACTA API", description="Action Coordination & Task Agent backend", version="0.1.0")

@app.get("/")
def root():
    return {"name": "ACTA API", "status": "running", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/divisions")
def list_divisions():
    try:
        response = get_supabase_client().table("divisions").select("*").order("name").execute()
        return {"data": response.data, "count": len(response.data)}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Could not load divisions. Check backend configuration and Supabase tables.") from exc

@app.get("/api/employees")
def list_employees():
    try:
        response = get_supabase_client().table("employees").select("*").order("name").execute()
        return {"data": response.data, "count": len(response.data)}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Could not load employees. Check backend configuration and Supabase tables.") from exc

@app.get("/api/projects")
def list_projects():
    try:
        response = get_supabase_client().table("projects").select("*").order("name").execute()
        return {"data": response.data, "count": len(response.data)}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Could not load projects. Check backend configuration and Supabase tables.") from exc
