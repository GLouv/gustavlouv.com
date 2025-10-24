"""
Main FastAPI application entry point
"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

# Import routers
from app.routers import blog, projects, verify

# Create FastAPI app
app = FastAPI(
    title="Gustav Louv",
    description="Personal website for Gustav Louv - Nordic AI operator, founder of Agent360",
    version="0.1.0",
)

# Setup static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Register routers
app.include_router(blog.router)
app.include_router(projects.router)
app.include_router(verify.router)


# Homepage route
@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    """Homepage with hero, Agent360 snapshot, and thought of the week"""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "page_title": "Gustav Louv - Nordic AI Operator",
            "page_description": "From sales floors to AI agents. Automating how the Nordics sell.",
        }
    )


# About page route
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """About page with Gustav's story"""
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
            "page_title": "About - Gustav Louv",
            "page_description": "8,000+ contracts before 25. From Tenerife to SF to Agent360.",
        }
    )


# Contact page route
@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """Contact information"""
    return templates.TemplateResponse(
        "contact.html",
        {
            "request": request,
            "page_title": "Contact - Gustav Louv",
            "page_description": "Get in touch with Gustav Louv",
        }
    )


# Health check
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "version": "0.1.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)

