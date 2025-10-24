"""
Projects routes
"""
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.project import Project

router = APIRouter(prefix="/projects", tags=["projects"])
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
async def projects_list(
    request: Request,
    db: Session = Depends(get_db)
):
    """Projects showcase page"""
    # Get all projects ordered by display order
    projects = db.query(Project).order_by(Project.order).all()
    
    return templates.TemplateResponse(
        "projects/index.html",
        {
            "request": request,
            "projects": projects,
            "page_title": "Projects - Gustav Louv",
            "page_description": "Agent360, EcommerceBot, and other AI experiments",
        }
    )

