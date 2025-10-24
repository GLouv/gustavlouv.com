# Gustav Louv Personal Website

**gustavlouv.com** - Personal website for Nordic AI operator Gustav Louv, founder of Agent360.

## Tech Stack

- **Backend**: Python FastAPI
- **Templates**: Jinja2 (server-side rendering)
- **Database**: PostgreSQL (Railway or Supabase)
- **ORM**: SQLAlchemy + Alembic
- **Styling**: Tailwind CSS
- **Hosting**: Railway
- **Provenance**: GPG + Danish QTSP + IPFS + OpenTimestamps

## Project Structure

```
gustavlouv.com-korrekt/
├── app/
│   ├── main.py                 # FastAPI application entry
│   ├── routers/                # API routes
│   │   ├── blog.py
│   │   ├── projects.py
│   │   ├── admin.py
│   │   └── verify.py
│   ├── models/                 # SQLAlchemy models
│   │   ├── post.py
│   │   ├── project.py
│   │   └── proof.py
│   ├── templates/              # Jinja2 templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── blog/
│   │   ├── projects/
│   │   └── partials/
│   ├── static/                 # Static assets
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── services/               # Business logic
│   │   ├── proof_service.py
│   │   ├── ipfs_service.py
│   │   └── qtsp_service.py
│   └── utils/                  # Utilities
│       ├── crypto.py
│       └── markdown.py
├── migrations/                 # Alembic migrations
├── scripts/                    # Utility scripts
│   └── publish_edition.py
├── tests/                      # Tests
├── cursor/                     # Cursor AI prompts
├── requirements.txt
├── .env.example
└── README.md

```

## Quick Start

### 1. Setup Python Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your credentials
nano .env
```

### 3. Setup Database

```bash
# Run migrations
alembic upgrade head

# (Optional) Seed initial data
python scripts/seed_data.py
```

### 4. Run Development Server

```bash
# Start server (port 8002 as per project standards)
uvicorn app.main:app --reload --port 8002

# Visit: http://localhost:8002
```

## Key Features

### 🔐 Provenance System

Each blog post edition is cryptographically sealed with:
- **SHA-256 hash** of content bundle
- **GPG signature** via YubiKey hardware key
- **Danish QTSP timestamp** (.tsr) for legal timeproof
- **OpenTimestamps proof** (.ots) for Bitcoin anchoring
- **IPFS pinning** for immutable distributed storage

### 📝 Blog with Verification

Every post displays a ProofPanel showing tamper evidence:
- Published UTC timestamp
- Content hash
- Signature verification
- QTSP token
- IPFS gateway link
- Verify button → `/verify` page

### 🎨 Design Philosophy

- **Minimal**: Content-first, timeless design
- **Accessible**: WCAG 2.2 AA compliant
- **Performance**: LCP < 2.5s, CLS < 0.1, TTI < 3.5s
- **Nordic Operator Aesthetic**: Calm, confident, authentic

## Development

### Code Quality

```bash
# Format code
black app/
isort app/

# Lint
flake8 app/

# Run tests
pytest
```

### Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "Description"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

### Publish Blog Edition

```bash
# Publish new post edition (creates proofs)
python scripts/publish_edition.py --post-id 1
```

## Deployment (Railway)

### Environment Variables

Set in Railway dashboard:
- `DATABASE_URL` (auto-provided by Railway Postgres)
- `SECRET_KEY`
- `JWT_SECRET_KEY`
- `IPFS_GATEWAY_URL`
- `GPG_KEY_ID`
- All other vars from `.env.example`

### Deploy Command

Railway will detect `uvicorn` and run:
```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## Documentation

- **PROJECT_STATUS.md** - Complete task breakdown (34 major tasks)
- **TODO_SUMMARY.md** - Quick reference guide
- **/cursor/** - AI context system for consistent development
- **/docs/** - Architecture decisions and guides

## License

Private project - All rights reserved © 2025 Gustav Louv

## Contact

- **Website**: gustavlouv.com (when live)
- **X**: [@gustavlouv](https://x.com/gustavlouv)
- **Email**: gustav@gustavlouv.com

---

**Built with authenticity, clarity, and momentum.**

