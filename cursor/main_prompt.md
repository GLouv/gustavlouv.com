You are building Gustav Louv's personal website at gustavlouv.com. The site must feel like the home of a Nordic AI operator: human, sharp, quietly confident. Naval Ravikant meets Sam Altman, with straight-talking builder energy. No marketing fluff, no startup clichés. Voice comes from someone in the arena.

Tone & Voice
- Visitors should describe Gustav as authentic, visionary, strategic, grounded, relentless.
- Write in first-person where natural; keep it precise, direct, and personal but never overshared.
- When in doubt, choose clarity over hype.

Audience Focus
- Operators & founders should think "I could learn from or partner with this person."
- Investors should think "He's someone I should back early."
- AI enthusiasts & sales leaders should think "I want to follow his build journey—this is where the future is being built."

Narrative Priorities
- Above the fold: spotlight Agent360's vision (building the Nordic AI sales infrastructure), the shift from top salesperson to AI founder, and a tight hero line such as "From sales floors to AI agents. Automating how the Nordics sell."
- Deeper in the scroll: early sales success (8,000+ electricity contracts before 25), Tenerife ventures, the EcommerceBot hostage saga + San Francisco rebuild + Shopify pivot, lessons learned, and the Agent360 roadmap.
- Treat setbacks as iterations toward mastery, not failures.

Required Sections & Content
1. Homepage
   - Hero: tagline + two-sentence framing of the journey into AI infrastructure.
   - Brief Agent360 snapshot and the current focus.
   - Latest blog highlights (3 max) with timestamp references.
   - Featured projects card row (link to Projects).
   - Dynamic "Thought of the Week" block: original insight or reflection; assume weekly refresh driven from CMS content.
   - CTAs: Read the blog (primary), Follow on X, subtle invite to hear about future updates (no visible newsletter form yet).

2. About
   - Concise, high-impact story covering: early sales record, Tenerife entrepreneurship, EcommerceBot hostage incident and pivot, move to SF, rebuilding with new co-founder, transition into AI, founding Agent360 six months ago, current mission to build the top AI-powered sales voice solution in the Nordics.
   - Focus on professional milestones; keep it tight and forward-looking.

3. Blog
   - List view with verifiable timestamps (see Provenance section).
   - Post template that reads like a builder thinking out loud: reflections-in-motion, intellectual but grounded.
   - Highlight starting themes: context as key differentiator, AI agents with tools, EU AI Act perspective, AI + real estate, problem-solving mindset, AI video's creative wave.
   - Cadence guidance: 1–2 thoughtful essays per month plus shorter "thought of the week" artifacts.

4. Projects
   - Grid/card layout for past and current initiatives with images (or tasteful placeholders), short descriptions, and status tags.
   - Include Agent360, EcommerceBot, Tenerife ventures, and other AI experiments.

5. Contact
   - Simple, direct contact options (email and social handles). Emphasize approachability without forms if unnecessary.

6. Verify & Provenance
   - Dedicated `/verify` page tied to the sealed-edition workflow (see Provenance plan below).
   - On each blog post, surface a ProofPanel summarizing tamper evidence and verification links.

7. Footer
   - Repeat minimal CTAs, link to privacy, and note the forthcoming newsletter in plain text only ("Newsletter coming later—get updates via X for now.")

Interaction Goals
- Make the site calm and intentional. Use no more than the three primary CTAs listed above.
- Encourage exploration and repeat visits, not hard conversions.

Visual Identity
- Palette: white + black/graphite foundation with a restrained electric blue accent (#0785FF) for links/highlights; keep dark mode consistent with accent.
- Typography: modern sans-serif (Inter or Neue Montreal) for text and headings. Prepare for optional system-font fallback for performance.
- Imagery: documentary-style, candid photography; avoid stock or illustration clutter. Content should be the visual anchor.
- Wordmark: "Gustav Louv" in the headline typeface; no extra logo.

Dynamic Elements
- "Thought of the Week" pulls from CMS; treat it as an original micro-reflection (2–3 sentences). Respect performance budgets—no heavy animations.
- Blog timestamps must be verifiable (see Provenance plan). Display published UTC and link to proof artifacts.

Provenance & Timestamping (implement per verifiedTimeStampPlan.md)
- Use the provided structure: scripts/publish_edition.sh, proofs/, edition_bundles/, ProofPanel.tsx, verify page, lib helpers, Supabase schema (`post_editions`), and publish workflow as outlined.
- Bundle each post edition, hash (SHA-256), sign with GPG/YubiKey, obtain Danish QTSP token (.tsr), optional OpenTimestamps (.ots), add to IPFS, store metadata + artifacts URLs in Supabase.
- ProofPanel component should mirror the plan (tamper evidence list, links to proofs, verify call-to-action).
- `/verify` page must fetch an edition, recompute hash, verify signature, and outline hooks for QTST/OTS validation. Use web crypto / OpenPGP.js stubs as noted.
- Ensure audio hooks and transcript support are ready for future features.

Technology & Platform
- Framework: Python FastAPI backend with Jinja2 templates for SSR, or FastAPI + React/HTMX for hybrid approach.
- Database: Supabase (Postgres) or Railway PostgreSQL for posts, versions, audio, proof metadata.
- Storage: Supabase Storage or Railway volumes for static assets and proof artifacts.
- Public blog read access; JWT auth for `/admin` routes.
- Keep content in Markdown/HTML in DB; support future i18n.
- Integrations: Google Analytics (+ optional Plausible), IPFS node, DK eIDAS QTSP, OpenTimestamps. No heavy tag managers.
- Deploy: Railway (as per project infrastructure).

Newsletter Handling
- No newsletter UI at launch. Prepare Supabase table and architectural hooks for future signups, but keep all references textual only (e.g., "Newsletter coming soon" note). Do not render a form yet.

Performance & Accessibility
- Target WCAG 2.2 AA; Lighthouse accessibility ≥95.
- Mobile-first; optimize for iOS/Android Safari/Chrome first, then desktop Safari/Chrome.
- Performance budgets: LCP <2.5s, CLS <0.1, TTI <3.5s, total JS ≤200KB on article pages.
- Typography defaults: base font 16–18px, line height 1.6–1.8, max text width 70–80ch.
- Respect prefers-reduced-motion; avoid heavy animations, especially on article pages.
- Touch targets ≥44×44 px; no hover-only interactions.
- Keyboard navigation, visible focus states, skip-to-content, semantic landmarks, correct heading hierarchy.
- Media accessibility: transcripts for audio, captions for future video, accessible players.

SEO & Compliance
- Server-rendered HTML, clean URLs, canonical tags, Open Graph/Twitter cards, JSON-LD Article schema, sitemap, robots.txt.
- Minimal cookies; GDPR-compliant consent handling. Clear privacy page.
- Defer analytics scripts until consent if required.

Reliability & Observability
- Export PDF/A inside edition bundles.
- Avoid third-party font dependence where possible.
- Implement lightweight `/admin` dashboard: pageviews, listens/reads counters, proof health, feature flags for future modules (newsletter, comments).

Deliverables for Cursor
- Scaffold FastAPI routes and Jinja2 templates per structure above.
- Implement database schema migrations (Alembic or SQLAlchemy).
- Implement publish script (Python) and ensure proof artifacts flow through database/storage.
- Build ProofPanel component (template partial) and `/verify` page with verification hooks.
- Create homepage, blog index/detail, projects, about, contact pages honoring tone and narrative.
- Provide stub data/examples where appropriate.
- Use Python libraries: FastAPI, Jinja2, SQLAlchemy, cryptography, gpg, ipfshttpclient.

Always default to authenticity, clarity, and momentum. Let the copy and structure show a builder in motion who is engineering the Nordic AI sales infrastructure.

Development Rules
- NEVER create files that don't have a function in the code - no explanatory documents, report documents, todo documents, or other non-functional files unless specifically requested
- Never make guides unless told
- Never create mock tests or mockdata without the user asking
- NEVER make any rapports, no test repports, no nothing without user asking you to

