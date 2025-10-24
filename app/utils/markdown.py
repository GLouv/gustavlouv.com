"""
Markdown rendering utilities
"""
import markdown
from markdown.extensions import fenced_code, tables, codehilite


def render_markdown(content: str) -> str:
    """
    Render markdown content to HTML
    
    Args:
        content: Markdown string
        
    Returns:
        HTML string
    """
    md = markdown.Markdown(
        extensions=[
            'fenced_code',
            'tables',
            'codehilite',
            'nl2br',
            'sane_lists',
        ],
        extension_configs={
            'codehilite': {
                'css_class': 'highlight',
                'linenums': False,
            }
        }
    )
    return md.convert(content)


def calculate_reading_time(content: str, words_per_minute: int = 200) -> int:
    """
    Calculate estimated reading time in minutes
    
    Args:
        content: Text content
        words_per_minute: Average reading speed (default 200)
        
    Returns:
        Estimated reading time in minutes
    """
    words = len(content.split())
    minutes = max(1, round(words / words_per_minute))
    return minutes

