# Gustav Louv Website - Project Status & TODO

**Project**: gustavlouv.com - Personal website for Nordic AI operator  
**Last Updated**: 2025-10-24  
**Status**: Initial Setup Phase

---

## ✅ COMPLETED

### 1. Cursor Prompt Architecture (DONE ✓)
- [x] `/cursor/main_prompt.md` - Hovedprompt med tone, voice, narrative
- [x] `/cursor/sub_prompts/site_style_guide.md` - Design filosofi
- [x] `/cursor/sub_prompts/accessibility_platforms.md` - WCAG 2.2 AA krav
- [x] `/cursor/sub_prompts/provenance_plan.md` - Timestamp workflow
- [x] `/cursor/cursor_instructions.json` - Prompt loading config
- [x] `/cursor/config.json` - Context enforcement
- [x] `/cursor/README.md` - Dokumentation

**Result**: Cursor har nu fuld kontekst på brand, tone og tekniske krav.

---

## 🚧 IN PROGRESS

*Ingen aktive tasks pt.*

---

## 📋 TODO - INFRASTRUCTURE & SETUP

### 2. Project Initialization
- [ ] Initialize Python FastAPI project
- [ ] Setup Python virtual environment (venv)
- [ ] Create requirements.txt with dependencies:
  - [ ] fastapi
  - [ ] uvicorn[standard]
  - [ ] jinja2
  - [ ] sqlalchemy
  - [ ] alembic
  - [ ] python-multipart
  - [ ] cryptography
  - [ ] python-gnupg
  - [ ] ipfshttpclient
  - [ ] httpx (for async requests)
- [ ] Configure Tailwind CSS with custom theme (via CDN or build process)
  - [ ] Electric blue (#0785FF) as primary
  - [ ] Graphite colors for text
  - [ ] 8px spacing system
  - [ ] Custom font: Inter or Neue Montreal
- [ ] Setup Black, isort, flake8 for code formatting
- [ ] Create basic folder structure:
  ```
  app/
    main.py
    routers/
      blog.py
      projects.py
      admin.py
      verify.py
    models/
      post.py
      project.py
      proof.py
    templates/
      base.html
      index.html
      about.html
      blog/
      projects/
      verify.html
    static/
      css/
      js/
      images/
    services/
      proof_service.py
      ipfs_service.py
      qtsp_service.py
    utils/
      crypto.py
      markdown.py
  migrations/
  scripts/
    publish_edition.py
  tests/
  ```

### 3. Database Setup (Railway PostgreSQL or Supabase)
- [ ] Create PostgreSQL database (Railway eller Supabase - DK region hvis muligt)
- [ ] Setup SQLAlchemy models:
  - [ ] `Post` model (id, title, slug, content, published_at, status, created_at, updated_at)
  - [ ] `PostEdition` model (id, post_id, edition_number, content_hash, signature, qtsp_token_url, ots_url, ipfs_cid, bundle_url, created_at)
  - [ ] `Project` model (id, title, description, image_url, status, order, created_at)
  - [ ] `ThoughtOfWeek` model (id, content, week_start, active, created_at)
  - [ ] `NewsletterSignup` model (id, email, subscribed_at, active) - til senere brug
- [ ] Create Alembic migration scripts
- [ ] Setup storage løsning:
  - [ ] Railway volumes for local file storage
  - [ ] OR Supabase Storage buckets (post-images, audio, proofs, editions)
  - [ ] Create upload/download helper functions
- [ ] Configure database connection pooling
- [ ] Setup JWT auth for `/admin` routes
- [ ] Create `.env` file with database credentials og secrets

### 4. Development Environment
- [ ] Create development startup script (`scripts/development/start.sh`)
- [ ] Configure uvicorn with hot reload: `uvicorn app.main:app --reload --port 8002`
- [ ] Setup environment variables template (`.env.example`)
- [ ] Create `.gitignore` for Python projekt (venv/, __pycache__/, .env, *.pyc)
- [ ] Initialize git repository hvis ikke allerede gjort
- [ ] Setup pre-commit hooks (black, isort, flake8)

---

## 📋 TODO - CORE PAGES & COMPONENTS

### 5. Homepage (`/`)
- [ ] Create FastAPI route: `@app.get("/")` → render `index.html`
- [ ] Jinja2 template: `templates/index.html`
- [ ] Hero sektion med tagline
- [ ] Agent360 snapshot sektion
- [ ] "Thought of the Week" komponent (dynamisk fra database)
- [ ] Seneste blog highlights (3 posts max) - query fra database
- [ ] Featured projects cards - query fra database
- [ ] CTAs: "Read the Blog", "Follow on X"
- [ ] Responsive layout (mobile-first)
- [ ] Template partial: `_hero.html`, `_thought_of_week.html`

### 6. About Page (`/about`)
- [ ] Create FastAPI route: `@app.get("/about")` → render `about.html`
- [ ] Jinja2 template: `templates/about.html`
- [ ] Hovedfortælling:
  - [ ] 8,000+ kontrakter før 25 år
  - [ ] Tenerife ventures
  - [ ] EcommerceBot hostage saga
  - [ ] SF rebuild + Shopify pivot
  - [ ] Transition til AI
  - [ ] Agent360 founding (6 måneder siden)
- [ ] Professional milestones timeline (valgfrit)
- [ ] Fremadrettet fokus på Nordic AI sales

### 7. Blog (`/blog`)
- [ ] Create FastAPI routes in `routers/blog.py`:
  - [ ] `@router.get("/blog")` → blog list view
  - [ ] `@router.get("/blog/{slug}")` → individual post
- [ ] Jinja2 templates:
  - [ ] `templates/blog/index.html` - list view
  - [ ] `templates/blog/post.html` - individual post
- [ ] Blog list view med:
  - [ ] Post cards (title, excerpt, published date)
  - [ ] Verifiable timestamps display
  - [ ] Filter/sort options (newest first)
  - [ ] Pagination (using query params: ?page=1)
  - [ ] SQLAlchemy query: `Post.query.filter_by(status='published').order_by(desc(Post.published_at))`
- [ ] Individual blog post page (`/blog/{slug}`)
  - [ ] Markdown rendering (using Python `markdown` library)
  - [ ] ProofPanel template partial (se nedenfor)
  - [ ] Reading time estimate (calculate from word count)
  - [ ] Social share buttons (static HTML/JS)
  - [ ] Max text width 70-80ch
  - [ ] Audio player placeholder (til fremtidig brug)
- [ ] Blog post starting content (skriv 3-5 initial posts):
  - [ ] "Context as Key Differentiator"
  - [ ] "AI Agents with Tools"
  - [ ] "EU AI Act Perspective"
  - [ ] "AI + Real Estate"
  - [ ] "Problem-Solving Mindset"

### 8. Projects Page (`/projects`)
- [ ] Create FastAPI route: `@router.get("/projects")` → render `projects.html`
- [ ] Jinja2 template: `templates/projects/index.html`
- [ ] Grid/card layout
- [ ] Project cards med:
  - [ ] Billede eller placeholder
  - [ ] Title + description
  - [ ] Status tag (Active, Completed, Archived)
  - [ ] Link til mere info (hvis relevant)
  - [ ] SQLAlchemy query: `Project.query.order_by(Project.order).all()`
- [ ] Featured projects:
  - [ ] Agent360 (active)
  - [ ] EcommerceBot (archived + pivot story)
  - [ ] Tenerife ventures
  - [ ] Andre AI eksperimenter

### 9. Contact Page (`/contact`)
- [ ] Create FastAPI route: `@app.get("/contact")` → render `contact.html`
- [ ] Jinja2 template: `templates/contact.html`
- [ ] Email display
- [ ] Social links (X, LinkedIn, etc.)
- [ ] Simpel, direkte layout
- [ ] Ingen forms (medmindre ønsket)

### 10. Verify Page (`/verify`)
- [ ] Create FastAPI routes in `routers/verify.py`:
  - [ ] `@router.get("/verify")` → render verify form
  - [ ] `@router.post("/verify")` → perform verification
  - [ ] `@router.get("/verify/{slug}/{edition}")` → direct verification link
- [ ] Jinja2 template: `templates/verify.html`
- [ ] Edition lookup interface (by post slug + edition number)
- [ ] Display original edition metadata
- [ ] Python verification logic:
  - [ ] Recompute SHA-256 hash using `hashlib`
  - [ ] Verify GPG signature using `python-gnupg`
  - [ ] QTSP token validation hooks (stub for Danish QTSP)
  - [ ] OpenTimestamps validation hooks (stub)
  - [ ] IPFS retrieval verification using `ipfshttpclient`
- [ ] Result display: "✓ Verified" eller "✗ Tampered"

---

## 📋 TODO - PROVENANCE SYSTEM

### 11. ProofPanel Template Partial
- [ ] Create Jinja2 template partial: `templates/partials/_proof_panel.html`
- [ ] Display fields:
  - [ ] Published UTC timestamp
  - [ ] SHA-256 hash
  - [ ] GPG signature fingerprint + download link
  - [ ] Danish QTSP token link (.tsr file)
  - [ ] OpenTimestamps proof link (.ots file)
  - [ ] IPFS CID + gateway link
  - [ ] "Verify this edition" CTA → `/verify`
- [ ] Pass edition data from route: `{{ proof_data }}`
- [ ] Styling: minimal, calm, technical but accessible
- [ ] Responsive layout

### 12. Edition Publishing Workflow
- [ ] Create Python script: `scripts/publish_edition.py`:
  - [ ] Bundle post content + metadata + audio (hvis tilgængelig)
  - [ ] Generate SHA-256 hash using `hashlib`
  - [ ] Sign hash med GPG/YubiKey using `python-gnupg`
  - [ ] Obtain Danish QTSP timestamp (.tsr)
  - [ ] (Optional) Create OpenTimestamps proof (.ots)
  - [ ] Pin bundle til IPFS node → get CID using `ipfshttpclient`
  - [ ] Upload artifacts til storage (Railway volumes or Supabase)
  - [ ] Insert metadata i `post_editions` table via SQLAlchemy
- [ ] Create supporting service modules:
  - [ ] `services/proof_service.py` - main orchestration
  - [ ] `utils/crypto.py` - SHA-256 hashing and bundling
  - [ ] `utils/gpg_signer.py` - GPG signing wrapper
  - [ ] `services/qtsp_service.py` - Danish QTSP API client
  - [ ] `services/ots_service.py` - OpenTimestamps client
  - [ ] `services/ipfs_service.py` - IPFS pinning client
  - [ ] `services/verification_service.py` - verification logic

### 13. IPFS Setup
- [ ] Setup self-hosted IPFS node (DK) - kan køre på Railway eller separate VPS
- [ ] Configure IPFS daemon (ipfs init && ipfs daemon)
- [ ] Install `ipfshttpclient`: `pip install ipfshttpclient`
- [ ] Create Python pinning service: `services/ipfs_service.py`
- [ ] Document IPFS gateway URLs (local + public fallback)
- [ ] Test edition pinning & retrieval
- [ ] Setup IPFS API auth hvis exposed publicly

### 14. Danish QTSP Integration
- [ ] Research Danish eIDAS QTSP providers (gratis options)
- [ ] Setup API credentials
- [ ] Implement timestamp request flow
- [ ] Store .tsr files i Supabase Storage
- [ ] Document QTSP verification process

### 15. OpenTimestamps (Optional)
- [ ] Install OpenTimestamps client
- [ ] Implement .ots file generation
- [ ] Setup Bitcoin anchoring monitoring
- [ ] Store .ots files i Supabase Storage

---

## 📋 TODO - SHARED COMPONENTS & LAYOUT

### 16. Layout Templates
- [ ] Create `templates/base.html` - master layout template
- [ ] Header/Navigation partial: `templates/partials/_header.html`
  - [ ] Logo: "Gustav Louv" wordmark
  - [ ] Nav links: Home, About, Blog, Projects, Contact
  - [ ] Responsive menu (mobile) - Alpine.js eller pure CSS
  - [ ] Dark mode toggle (valgfrit) - Alpine.js
- [ ] Footer partial: `templates/partials/_footer.html`
  - [ ] Minimal CTAs
  - [ ] Privacy link
  - [ ] "Newsletter coming later" note
  - [ ] Social links

### 17. Shared Template Partials & CSS
- [ ] Template partials:
  - [ ] `_card.html` - reusable card (projects, blog highlights)
  - [ ] `_button.html` - button styles (primary, secondary variants)
  - [ ] `_loading.html` - loading spinner
- [ ] CSS components (Tailwind classes eller custom CSS):
  - [ ] Button variants (.btn-primary, .btn-secondary)
  - [ ] Card styling
  - [ ] Typography scale (h1, h2, body)
  - [ ] Link styling (blue accent hover)
- [ ] Error handling:
  - [ ] Custom error pages: `templates/errors/404.html`, `500.html`
  - [ ] FastAPI exception handlers

---

## 📋 TODO - ADMIN & CMS

### 18. Admin Dashboard (`/admin`)
- [ ] Create FastAPI router: `routers/admin.py`
- [ ] JWT authentication dependency:
  - [ ] Login endpoint: `@router.post("/admin/login")`
  - [ ] JWT token generation og validation
  - [ ] Protected routes decorator: `@router.get("/admin/", dependencies=[Depends(verify_token)])`
- [ ] Templates:
  - [ ] `templates/admin/login.html`
  - [ ] `templates/admin/dashboard.html`
  - [ ] `templates/admin/post_editor.html`
  - [ ] `templates/admin/projects.html`
- [ ] Dashboard overview:
  - [ ] Pageviews (GA integration via API)
  - [ ] Blog post reads counters
  - [ ] Proof health status
  - [ ] Feature flags (newsletter, comments - til senere)
- [ ] Blog post editor:
  - [ ] Markdown editor med preview (SimpleMDE eller Trix)
  - [ ] Metadata input (title, slug, excerpt)
  - [ ] Publish workflow trigger (call publish_edition.py)
  - [ ] Draft/published status toggle
  - [ ] CRUD endpoints for posts
- [ ] "Thought of the Week" editor
- [ ] Projects manager (CRUD interface)

---

## 📋 TODO - INTEGRATIONS & ANALYTICS

### 19. Analytics Setup
- [ ] Google Analytics 4 integration:
  - [ ] Add GA4 script til `base.html` template
  - [ ] Conditional loading based on consent
- [ ] (Optional) Plausible Analytics - self-hosted eller cloud
- [ ] GDPR-compliant consent banner:
  - [ ] Create `templates/partials/_cookie_banner.html`
  - [ ] JavaScript for consent management (localStorage)
- [ ] Cookie policy page: `templates/privacy.html`
- [ ] Defer analytics til consent givet
- [ ] Custom events: blog reads, proof verifications
  - [ ] Server-side event tracking via GA Measurement Protocol (optional)

### 20. SEO & Meta
- [ ] Server-side rendering (SSR) via Jinja2 templates - already enabled ✓
- [ ] Dynamic meta tags i `base.html`:
  - [ ] Pass `page_title`, `page_description` from routes
  - [ ] Template blocks: `{% block meta %}{% endblock %}`
- [ ] Open Graph tags (og:title, og:description, og:image)
- [ ] Twitter Card tags (twitter:card, twitter:title, twitter:image)
- [ ] JSON-LD Article schema for blog posts:
  - [ ] Generate JSON-LD in Python, pass to template
  - [ ] `<script type="application/ld+json">{{ json_ld | safe }}</script>`
- [ ] Canonical URLs: `<link rel="canonical" href="{{ canonical_url }}" />`
- [ ] `sitemap.xml` generation:
  - [ ] FastAPI route: `@app.get("/sitemap.xml")`
  - [ ] Generate XML from database queries
- [ ] `robots.txt`: static file in `static/robots.txt`
- [ ] Structured data testing (Google Rich Results Test)

---

## 📋 TODO - PERFORMANCE & OPTIMIZATION

### 21. Performance Tuning
- [ ] Image optimization (Next.js Image component)
- [ ] Font optimization (local hosting eller fallback)
- [ ] Code splitting
- [ ] Lazy loading for below-fold content
- [ ] Prefetching for blog navigation
- [ ] Bundle analysis
- [ ] Target metrics:
  - [ ] LCP < 2.5s
  - [ ] CLS < 0.1
  - [ ] TTI < 3.5s
  - [ ] Total JS ≤ 200KB (article pages)

### 22. Accessibility Audit
- [ ] Run Lighthouse accessibility audit (target ≥95)
- [ ] Test keyboard navigation across site
- [ ] Verify focus states are visible
- [ ] Test with screen reader (VoiceOver på Mac)
- [ ] Verify touch target sizes (≥44×44px)
- [ ] Implement skip-to-content link
- [ ] Semantic HTML landmarks
- [ ] Correct heading hierarchy (h1 → h2 → h3)
- [ ] Alt text for alle images
- [ ] ARIA labels hvor nødvendigt
- [ ] Color contrast validation (WCAG AA)

### 23. Media Accessibility
- [ ] Transcript upload system for audio
- [ ] Accessible audio player
- [ ] Caption support for future video
- [ ] Prefers-reduced-motion respect

---

## 📋 TODO - DEPLOYMENT & INFRASTRUCTURE

### 24. Hosting Setup (Railway)
- [ ] Deploy to Railway (as per project infrastructure)
- [ ] Create Railway project og link GitHub repo
- [ ] Configure deployment pipeline:
  - [ ] Create `railway.toml` eller use Procfile
  - [ ] Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
  - [ ] Set reasonable timeouts (as per user rules)
- [ ] Setup custom domain: gustavlouv.com
  - [ ] Configure DNS records (A/CNAME)
  - [ ] SSL certificate (automatic via Railway)
- [ ] Environment variables for production (set in Railway dashboard)
- [ ] Setup staging environment (separate Railway service)

### 25. Static Assets & CDN
- [ ] Configure DNS records (via domain registrar)
- [ ] Setup CDN for static assets:
  - [ ] Railway serves static files via FastAPI StaticFiles
  - [ ] Optional: Cloudflare for CDN + DDoS protection
- [ ] Configure cache headers in FastAPI:
  - [ ] `Cache-Control` headers for static assets
  - [ ] `max-age` for images, CSS, JS
- [ ] Image optimization:
  - [ ] Use Pillow for resizing/compression
  - [ ] Serve WebP format where supported

### 26. Monitoring & Reliability
- [ ] Error tracking (Sentry eller lignende)
- [ ] Uptime monitoring
- [ ] Performance monitoring
- [ ] Log aggregation
- [ ] Backup strategy for Supabase data

---

## 📋 TODO - CONTENT CREATION

### 27. Initial Content
- [ ] Write About page copy
- [ ] Write 3-5 initial blog posts
- [ ] Create "Thought of the Week" for første 4 uger
- [ ] Gather project images/descriptions
- [ ] Professional photos (documentary-style)
- [ ] Create privacy policy
- [ ] Create terms of service (hvis relevant)

### 28. Media Assets
- [ ] Professional headshot(er)
- [ ] Project screenshots
- [ ] Documentary-style photos
- [ ] Favicon & app icons
- [ ] Social share preview images

---

## 📋 TODO - FUTURE FEATURES (DEFERRED)

### 29. Newsletter (Not at Launch)
- [ ] Supabase table ready (done in step 3)
- [ ] Design signup form
- [ ] Email service integration (Resend, SendGrid?)
- [ ] Welcome email template
- [ ] Regular newsletter template
- [ ] Unsubscribe flow
- [ ] GDPR compliance

### 30. Comments System (Future)
- [ ] Evaluate options (Giscus, custom?)
- [ ] Moderation workflow
- [ ] Notification system

### 31. Audio Version of Posts (Future)
- [ ] Recording workflow
- [ ] Audio hosting strategy
- [ ] Player integration
- [ ] Transcript generation/sync

### 32. Internationalization (Future)
- [ ] i18n framework setup
- [ ] Danish translation
- [ ] Language switcher
- [ ] Locale-specific content

---

## 🔧 TECHNICAL DEBT & CLEANUP

### 33. Code Quality
- [ ] Setup automated testing:
  - [ ] pytest for unit tests
  - [ ] pytest-asyncio for async tests
  - [ ] httpx for testing FastAPI endpoints
- [ ] Write unit tests:
  - [ ] `tests/test_crypto.py` - hashing, signing
  - [ ] `tests/test_services/` - proof, IPFS, QTSP services
  - [ ] `tests/test_routes/` - API endpoint tests
- [ ] Write integration tests:
  - [ ] Full publish workflow
  - [ ] Verification workflow
- [ ] Code review checklist
- [ ] Documentation:
  - [ ] Docstrings for all functions
  - [ ] README for each major module

### 34. Security
- [ ] Security audit
- [ ] Rate limiting på API routes:
  - [ ] Use `slowapi` library: `pip install slowapi`
  - [ ] Apply rate limits til admin endpoints
- [ ] Input validation:
  - [ ] Pydantic models for all request bodies
  - [ ] Validation for slugs, emails, etc.
- [ ] XSS protection:
  - [ ] Jinja2 auto-escaping enabled (default)
  - [ ] Use `| safe` filter sparingly
- [ ] CSRF protection:
  - [ ] CSRF tokens for admin forms
  - [ ] Use `starlette-csrf` middleware
- [ ] Content Security Policy headers:
  - [ ] Add CSP middleware til FastAPI
  - [ ] Configure allowed sources for scripts, styles

---

## 📊 METRICS & SUCCESS CRITERIA

### Launch Readiness Checklist
- [ ] All core pages live (Home, About, Blog, Projects, Contact, Verify)
- [ ] Minimum 3 blog posts published
- [ ] Provenance system functional (can verify at least 1 post)
- [ ] Lighthouse scores: Performance ≥90, Accessibility ≥95, SEO ≥95
- [ ] Mobile responsive across iOS/Android
- [ ] Analytics tracking
- [ ] GDPR compliance
- [ ] Privacy policy live
- [ ] Custom domain configured
- [ ] SSL active

### Post-Launch Priorities
1. Monitor analytics & user behavior
2. Publish blog posts 1-2x/måned
3. Gather feedback
4. Iterate på UX
5. Add newsletter når klar
6. Consider audio versions
7. Community building (X, LinkedIn)

---

## 📝 NOTES & DECISIONS

### Key Architectural Decisions
- **Backend Framework**: Python FastAPI for API + SSR
- **Template Engine**: Jinja2 for server-side rendering
- **Database**: PostgreSQL (Railway eller Supabase)
- **ORM**: SQLAlchemy with Alembic migrations
- **Styling**: Tailwind CSS med custom theme (CDN eller build process)
- **Interactivity**: Alpine.js eller HTMX for dynamic UI (minimal JS)
- **Provenance**: GPG + Danish QTSP + IPFS + (optional OTS)
- **Hosting**: Railway (as per project infrastructure)
- **Analytics**: GA4 + optional Plausible
- **Port**: Backend runs on port 8002 (as per user rules)

### Design Philosophy Reminder
- **Minimal**: Content first, decoration last
- **Timeless**: Avoid trends; focus på clarity
- **Calm**: Generous whitespace, subtle motion
- **Accessible**: WCAG 2.2 AA minimum
- **Authentic**: Tone = Nordic operator, builder energy

### Dependencies & Integrations
- Python packages:
  - fastapi, uvicorn, jinja2, sqlalchemy, alembic
  - python-gnupg (GPG signing/verification)
  - cryptography (hashing, crypto operations)
  - ipfshttpclient (IPFS integration)
  - httpx (async HTTP client)
  - pydantic (data validation)
  - slowapi (rate limiting)
  - python-jose[cryptography] (JWT tokens)
- PostgreSQL database (Railway eller Supabase)
- Storage: Railway volumes eller Supabase Storage
- IPFS node (self-hosted i DK)
- Danish QTSP provider (research gratis options)
- OpenTimestamps (optional Bitcoin anchoring)
- Google Analytics (+ optional Plausible)

---

## 🎯 CURRENT PRIORITY

**Next Steps**:
1. Initialize FastAPI project structure
2. Setup PostgreSQL database + SQLAlchemy models
3. Create base template + homepage route
4. Build blog routes og templates
5. Implement ProofPanel template partial
6. Build publish_edition.py script

---

**End of Status Document**

