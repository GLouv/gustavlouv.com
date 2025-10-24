"""
Blog routes
"""
from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.post import Post, PostEdition

router = APIRouter(prefix="/blog", tags=["blog"])
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
async def blog_list(
    request: Request,
    page: int = 1,
    db: Session = Depends(get_db)
):
    """Blog list page with pagination"""
    per_page = 10
    offset = (page - 1) * per_page
    
    # Query published posts
    posts = db.query(Post).filter(
        Post.status == "published"
    ).order_by(
        Post.published_at.desc()
    ).offset(offset).limit(per_page).all()
    
    # Get total count for pagination
    total = db.query(Post).filter(Post.status == "published").count()
    total_pages = (total + per_page - 1) // per_page
    
    return templates.TemplateResponse(
        "blog/index.html",
        {
            "request": request,
            "posts": posts,
            "page": page,
            "total_pages": total_pages,
            "page_title": "Blog - Gustav Louv",
            "page_description": "Thoughts on AI, sales automation, and building the Nordic AI infrastructure",
        }
    )


@router.get("/{slug}", response_class=HTMLResponse)
async def blog_post(
    request: Request,
    slug: str,
    db: Session = Depends(get_db)
):
    """Individual blog post page"""
    # Get post by slug
    post = db.query(Post).filter(
        Post.slug == slug,
        Post.status == "published"
    ).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Get latest edition for proof data
    latest_edition = db.query(PostEdition).filter(
        PostEdition.post_id == post.id
    ).order_by(
        PostEdition.edition_number.desc()
    ).first()
    
    return templates.TemplateResponse(
        "blog/post.html",
        {
            "request": request,
            "post": post,
            "edition": latest_edition,
            "page_title": f"{post.title} - Gustav Louv",
            "page_description": post.excerpt or post.title,
        }
    )

