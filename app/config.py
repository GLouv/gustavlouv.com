"""
Application configuration
Loads environment variables and provides settings
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # Application
    app_env: str = "development"
    app_port: int = 8002
    debug: bool = True
    
    # Database
    database_url: str = "sqlite:///./gustavlouv.db"  # Default to SQLite for dev
    
    # Security
    secret_key: str = "change-this-in-production"
    jwt_secret_key: str = "change-this-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Supabase (optional)
    supabase_url: Optional[str] = None
    supabase_key: Optional[str] = None
    supabase_service_key: Optional[str] = None
    
    # Storage
    storage_type: str = "local"  # or 'supabase'
    upload_dir: str = "./uploads"
    proof_artifacts_dir: str = "./proof_artifacts"
    edition_bundles_dir: str = "./edition_bundles"
    
    # IPFS
    ipfs_host: str = "localhost"
    ipfs_port: int = 5001
    ipfs_gateway_url: str = "http://localhost:8080/ipfs/"
    
    # GPG
    gpg_key_id: Optional[str] = None
    gpg_passphrase: Optional[str] = None
    
    # QTSP (Danish Qualified Trust Service Provider)
    qtsp_api_url: Optional[str] = None
    qtsp_api_key: Optional[str] = None
    
    # OpenTimestamps
    ots_enabled: bool = False
    ots_calendar_url: str = "https://alice.btc.calendar.opentimestamps.org"
    
    # Analytics
    ga_measurement_id: Optional[str] = None
    plausible_domain: Optional[str] = None
    plausible_api_url: Optional[str] = None
    
    # Admin
    admin_email: str = "admin@gustavlouv.com"
    admin_password_hash: Optional[str] = None
    
    # CORS
    allowed_origins: list = ["http://localhost:8002", "https://gustavlouv.com"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()

