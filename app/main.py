from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.database import Base, engine, SessionLocal
import app.models
from app.models import Document

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "AI Engine Running 🚀"}

@app.post("/upload-data")
def upload_data(content: str, source: str, db: Session = Depends(get_db)):
    doc = Document(content=content, source=source)
    db.add(doc)
    db.commit()
    db.refresh(doc)

    return {"id": doc.id, "message": "Stored successfully"}