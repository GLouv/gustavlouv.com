# Gustav Louv Website - Quick TODO Summary

**Project**: gustavlouv.com  
**Status**: Setup fase - cursor prompts klar, klar til development

---

## ✅ DONE (1/34 major tasks)
1. ✓ Cursor prompt architecture - komplet setup

---

## 🎯 NEXT 5 PRIORITIES

### 1. Project Setup (0/5)
- [ ] Initialize Python FastAPI project
- [ ] Setup virtual environment + requirements.txt
- [ ] Configure Tailwind CSS med custom theme (#0785FF blue)
- [ ] Setup Black, isort, flake8 for code formatting
- [ ] Create folder structure (app/, templates/, static/, scripts/)
- [ ] Git repository setup

### 2. Database Setup (0/7)
- [ ] Create PostgreSQL database (Railway eller Supabase - DK region)
- [ ] SQLAlchemy models: Post, PostEdition, Project, ThoughtOfWeek
- [ ] Alembic migration scripts
- [ ] Storage: Railway volumes eller Supabase Storage
- [ ] JWT auth for /admin routes
- [ ] Environment variables (.env file)
- [ ] Test database connections

### 3. Core Pages & Routes (0/6)
- [ ] Homepage: FastAPI route + Jinja2 template med hero + Agent360
- [ ] About page: route + template med full story
- [ ] Blog: routers/blog.py + list/detail templates
- [ ] Projects: route + grid template
- [ ] Contact: route + simple template
- [ ] Verify: routers/verify.py + verification logic

### 4. Provenance System (0/4)
- [ ] ProofPanel Jinja2 template partial
- [ ] scripts/publish_edition.py (Python)
- [ ] IPFS node setup (DK) + ipfshttpclient
- [ ] Danish QTSP integration (Python service)

### 5. Content & Launch (0/5)
- [ ] Write 3-5 initial blog posts
- [ ] Create project descriptions
- [ ] Professional photography
- [ ] Privacy policy
- [ ] Deploy to production

---

## 📊 COMPLETION TRACKER

**Infrastructure**: 1/34 tasks done (3%)  
**Pages**: 0/6 core pages  
**Components**: 0/10 components  
**Integrations**: 0/5 integrations  

**Estimated til MVP launch**: 4-6 uger med fuld dedikation

---

## 🚀 QUICK START COMMAND

```bash
# 1. Setup Python environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux

# 2. Install dependencies
pip install fastapi uvicorn[standard] jinja2 sqlalchemy alembic
pip install python-gnupg cryptography ipfshttpclient httpx
pip install python-multipart pydantic slowapi python-jose[cryptography]

# 3. Create project structure
mkdir -p app/{routers,models,templates,static,services,utils}
mkdir -p migrations scripts tests

# 4. Start development server
uvicorn app.main:app --reload --port 8002
```

---

**Se PROJECT_STATUS.md for fuld detaljer på alle 34 task groups**

