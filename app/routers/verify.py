"""
Verification routes for provenance system
"""
from fastapi import APIRouter, Request, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.post import Post, PostEdition
from app.services.verification_service import verify_edition

router = APIRouter(prefix="/verify", tags=["verify"])
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
async def verify_form(request: Request):
    """Verification form page"""
    return templates.TemplateResponse(
        "verify.html",
        {
            "request": request,
            "page_title": "Verify Post Edition - Gustav Louv",
            "page_description": "Verify the authenticity and timestamp of blog post editions",
        }
    )


@router.get("/{slug}/{edition}", response_class=HTMLResponse)
async def verify_edition_direct(
    request: Request,
    slug: str,
    edition: int,
    db: Session = Depends(get_db)
):
    """Direct verification link"""
    # Get post
    post = db.query(Post).filter(Post.slug == slug).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Get edition
    edition_obj = db.query(PostEdition).filter(
        PostEdition.post_id == post.id,
        PostEdition.edition_number == edition
    ).first()
    
    if not edition_obj:
        raise HTTPException(status_code=404, detail="Edition not found")
    
    # Perform verification
    verification_result = await verify_edition(edition_obj, db)
    
    return templates.TemplateResponse(
        "verify.html",
        {
            "request": request,
            "post": post,
            "edition": edition_obj,
            "verification": verification_result,
            "page_title": f"Verify: {post.title} (Edition {edition})",
        }
    )


@router.post("", response_class=HTMLResponse)
async def verify_edition_post(
    request: Request,
    slug: str = Form(...),
    edition_number: int = Form(...),
    db: Session = Depends(get_db)
):
    """Handle verification form submission"""
    # Get post
    post = db.query(Post).filter(Post.slug == slug).first()
    if not post:
        return templates.TemplateResponse(
            "verify.html",
            {
                "request": request,
                "error": "Post not found",
            }
        )
    
    # Get edition
    edition_obj = db.query(PostEdition).filter(
        PostEdition.post_id == post.id,
        PostEdition.edition_number == edition_number
    ).first()
    
    if not edition_obj:
        return templates.TemplateResponse(
            "verify.html",
            {
                "request": request,
                "error": "Edition not found",
            }
        )
    
    # Perform verification
    verification_result = await verify_edition(edition_obj, db)
    
    return templates.TemplateResponse(
        "verify.html",
        {
            "request": request,
            "post": post,
            "edition": edition_obj,
            "verification": verification_result,
        }
    )

