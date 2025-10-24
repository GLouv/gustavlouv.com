"""
Project model
"""
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base


class Project(Base):
    """Project showcase model"""
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    
    # Media
    image_url = Column(String(500), nullable=True)
    
    # Status: active, completed, archived
    status = Column(String(20), default="active", nullable=False)
    
    # Display order
    order = Column(Integer, default=0, nullable=False)
    
    # Optional links
    website_url = Column(String(500), nullable=True)
    github_url = Column(String(500), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Project(id={self.id}, title='{self.title}', status='{self.status}')>"

