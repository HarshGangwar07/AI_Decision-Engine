from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.db.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    source = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
