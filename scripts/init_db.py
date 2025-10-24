#!/usr/bin/env python3
"""
Initialize database schema
Creates all tables from SQLAlchemy models
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app.database import engine, Base
from app.models import Post, PostEdition, Project, ThoughtOfWeek


def init_db():
    """Create all database tables"""
    print("🗄️  Initializing database...")
    print(f"Database: {engine.url}")
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    print("✅ Database tables created successfully!")
    print("\nTables:")
    for table in Base.metadata.sorted_tables:
        print(f"  - {table.name}")


if __name__ == "__main__":
    init_db()

