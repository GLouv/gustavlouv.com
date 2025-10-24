"""
Thought of the Week model
"""
from sqlalchemy import Column, Integer, Text, Date, Boolean, DateTime
from datetime import datetime
from app.database import Base


class ThoughtOfWeek(Base):
    """Weekly thought/reflection model"""
    __tablename__ = "thoughts_of_week"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    
    # Week identifier
    week_start = Column(Date, nullable=False, unique=True)
    
    # Active flag - only one should be active at a time
    active = Column(Boolean, default=False, nullable=False)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<ThoughtOfWeek(id={self.id}, week_start={self.week_start}, active={self.active})>"

