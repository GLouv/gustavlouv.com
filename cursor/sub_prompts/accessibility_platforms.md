# Accessibility & Platform Fundamentals
- Meet WCAG 2.2 AA; Lighthouse ≥ 95 Accessibility.
- Mobile-first; optimize for iOS/Android Safari/Chrome first.
- Performance: LCP < 2.5 s, CLS < 0.1, TTI < 3.5 s, JS ≤ 200 KB/article.
- Touch targets ≥ 44 × 44 px; avoid hover-only controls.
- Keyboard nav + visible focus, skip-to-content, semantic landmarks.
- Transcripts for audio; captions for future video.
- Respect prefers-reduced-motion.
- Backend: Python FastAPI with Jinja2 SSR or FastAPI + HTMX/Alpine.js for interactivity.
- Database: PostgreSQL (Railway or Supabase); Markdown/HTML content.
- Storage: Railway volumes or Supabase Storage for assets.
- Analytics: GA + (optional Plausible); defer until consent.
- GDPR compliance; minimal cookies; clear privacy page.
- Deploy: Railway with reasonable timeout configurations.
- Keep site performant, privacy-respectful, human-readable.

