from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
import models, schemas

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow CORS (for frontend to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or set your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency: DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/report_incident", response_model=schemas.IncidentResponse)
def report_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    new_incident = models.Incident(
        type=incident.type,
        location=incident.location,
        time=incident.time,
        description=incident.description
    )
    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)
    return new_incident

@app.get("/get_incidents", response_model=list[schemas.IncidentResponse])
def get_incidents(db: Session = Depends(get_db)):
    return db.query(models.Incident).order_by(models.Incident.time.desc()).all()
