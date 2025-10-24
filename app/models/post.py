"""
Blog post models
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Post(Base):
    """Blog post model"""
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False, index=True)
    excerpt = Column(Text, nullable=True)
    content = Column(Text, nullable=False)
    
    # Status: draft, published, archived
    status = Column(String(20), default="draft", nullable=False)
    
    # Timestamps
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Metadata
    reading_time = Column(Integer, nullable=True)  # Minutes
    author = Column(String(100), default="Gustav Louv")
    
    # Optional audio
    audio_url = Column(String(500), nullable=True)
    transcript_url = Column(String(500), nullable=True)
    
    # Relationships
    editions = relationship("PostEdition", back_populates="post", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Post(id={self.id}, slug='{self.slug}', status='{self.status}')>"


class PostEdition(Base):
    """
    Cryptographically sealed edition of a blog post
    Each publish creates a new edition with proof artifacts
    """
    __tablename__ = "post_editions"
    
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    edition_number = Column(Integer, nullable=False)
    
    # Content snapshot
    content_snapshot = Column(Text, nullable=False)
    
    # Cryptographic proofs
    content_hash = Column(String(64), nullable=False)  # SHA-256
    signature = Column(Text, nullable=True)  # GPG signature
    signature_fingerprint = Column(String(40), nullable=True)
    
    # Proof artifacts URLs
    qtsp_token_url = Column(String(500), nullable=True)  # Danish QTSP .tsr
    ots_proof_url = Column(String(500), nullable=True)   # OpenTimestamps .ots
    ipfs_cid = Column(String(100), nullable=True)         # IPFS Content ID
    bundle_url = Column(String(500), nullable=True)       # Edition bundle download
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    verified = Column(Boolean, default=False)
    
    # Relationships
    post = relationship("Post", back_populates="editions")
    
    def __repr__(self):
        return f"<PostEdition(id={self.id}, post_id={self.post_id}, edition={self.edition_number})>"

