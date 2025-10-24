#!/usr/bin/env python3
"""
Seed database with example data
For development and testing
"""
import sys
from pathlib import Path
from datetime import datetime, date

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app.database import SessionLocal
from app.models import Post, Project, ThoughtOfWeek


def seed_data():
    """Seed database with example content"""
    db = SessionLocal()
    
    try:
        print("🌱 Seeding database...")
        
        # Check if data already exists
        existing_posts = db.query(Post).count()
        if existing_posts > 0:
            print(f"⚠️  Database already contains {existing_posts} posts")
            response = input("Continue anyway? (y/N): ")
            if response.lower() != 'y':
                print("Aborted.")
                return
        
        # Seed Projects
        print("\n📂 Creating projects...")
        
        projects = [
            Project(
                title="Agent360",
                slug="agent360",
                description="AI voice agents for Nordic sales teams. Context-aware, tool-equipped, and built for scale. Currently in active development with early pilot customers.",
                status="active",
                order=1,
                website_url="https://agent360.ai",
            ),
            Project(
                title="EcommerceBot",
                slug="ecommercebot",
                description="The hostage saga, SF rebuild, and Shopify pivot. Lessons learned on the path to Agent360. Built with first co-founder, held hostage, rebuilt in San Francisco.",
                status="archived",
                order=2,
            ),
            Project(
                title="Tenerife Ventures",
                slug="tenerife-ventures",
                description="Early entrepreneurial experiments in Tenerife. Small ventures, rapid iteration, learning what worked and what didn't. Foundation for everything that came after.",
                status="completed",
                order=3,
            ),
        ]
        
        for project in projects:
            db.add(project)
        
        db.commit()
        print(f"✅ Created {len(projects)} projects")
        
        # Seed Thought of the Week
        print("\n💭 Creating thought of the week...")
        
        thought = ThoughtOfWeek(
            content="Context isn't just data—it's the difference between an agent that responds and one that understands. The best AI sales tools won't replace reps; they'll make exceptional performance repeatable.",
            week_start=date.today(),
            active=True,
        )
        db.add(thought)
        db.commit()
        print("✅ Created thought of the week")
        
        # Seed example blog post (optional)
        print("\n📝 Creating example blog post...")
        
        example_post = Post(
            title="Context as Key Differentiator",
            slug="context-as-key-differentiator",
            excerpt="Why the best AI agents win on context, not just speed.",
            content="""
# Context as Key Differentiator

The race in AI sales automation isn't about who can respond fastest. It's about who understands best.

## The Problem with Speed

Most AI sales tools optimize for response time. They hear a question, match a pattern, spit out an answer. Fast, but hollow.

Speed matters. But context wins.

## What Context Means

Context isn't just data. It's the difference between knowing someone asked about pricing and understanding *why* they asked about pricing at this exact moment in the conversation.

Context is:
- The three emails that came before this one
- The prospect's company size and industry
- What they've looked at on your website
- The objections they raised last week
- The competitive alternatives they're evaluating

## How We Build for Context

At Agent360, we built our voice agents to be context-aware from the ground up:

1. **Conversation memory** - Every interaction is stored and referenced
2. **CRM integration** - Pull in deal stage, company data, previous touchpoints
3. **Real-time analysis** - Understand intent, not just keywords
4. **Adaptive responses** - Different answers for different contexts

## The Result

An agent that doesn't just respond. It understands. It adapts. It closes.

That's the future of AI sales. Not faster chatbots. Smarter systems.
            """.strip(),
            status="published",
            published_at=datetime.utcnow(),
            reading_time=3,
            author="Gustav Louv",
        )
        db.add(example_post)
        db.commit()
        print(f"✅ Created example post: {example_post.title}")
        
        print("\n✅ Database seeded successfully!")
        print(f"\nCreated:")
        print(f"  - {len(projects)} projects")
        print(f"  - 1 thought of the week")
        print(f"  - 1 example blog post")
        
    except Exception as e:
        print(f"\n❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()

