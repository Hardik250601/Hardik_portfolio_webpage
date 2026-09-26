# Hardik Darji Portfolio — Complete Documentation

**Live URL:** `https://hardikmdarji.work.gd/`  
**Repository:** `https://github.com/Hardikdarji921/Hardik-webpage`  
**Local Path:** `C:\Users\AINHMD\OneDrive - Ammann Group\Desktop\all MY project data\Hardik Webpage`

---

## 1. Overview

Personal portfolio for **Hardik Darji**, Senior Embedded Software Engineer at Ammann India. Showcases 3 case studies, a CMS for content management, 3 theme modes, 3D WebGL hero, and full SEO/accessibility compliance.

---

## 2. Pages & Structure

| File | Purpose | Key Features |
|------|---------|--------------|
| `index.html` | Homepage | Hero (3D + profile), summary, featured project, expertise, experience timeline, skills, achievements, projects grid, latest blog, education, "Beyond Embedded Software", contact form, newsletter, footer |
| `projects.html` | All projects list | Grid of 3 case studies with links to detail pages |
| `blogs.html` | All blog posts list | Grid layout (empty until posts added) |
| `project-template.html` | Case study detail | Dynamic hydration from `content.json` via URL `?slug=` |
| `blog-template.html` | Blog post detail | Dynamic hydration from `content.json` via URL `?slug=` |
| `404.html` | Not found page | Constellation background, back-to-home button |
| `crm.html` | CMS Dashboard | Add/edit projects & blogs, GitHub API integration |
| `crm-projects.html` | Project list in CMS | Delete projects |
| `crm-blogs.html` | Blog list in CMS | Delete blogs |
| `crm-edit-project.html` | Edit project form | Pre-filled form for existing project |
| `crm-edit-blog.html` | Edit blog form | Pre-filled form for existing blog |

---

## 3. Content (content.json)

### Projects (3)

1. **ESP32 Data Logger & Telematics Platform** (Professional)
   - Slug: `ammann-data-logger-telematics`
   - ESP32-S3, CAN/J1939, 4G/LTE, MQTT, Flask, Leaflet dashboard
   - 90% cost reduction (₹50k → ₹3.7k)
   - 3 supportive images: hardware, architecture, dashboard

2. **Remote-Controlled Multipurpose Robot** (Academic)
   - Slug: `remote-controlled-multipurpose-robot`
   - Arduino, nRF24L01, robotic arm, motor control
   - 2 supportive images: robot, architecture

3. **Smart Garbage Monitoring System** (Academic)
   - Slug: `smart-garbage-monitoring`
   - Arduino Uno, ultrasonic, IR, GSM, servo
   - 2 supportive images: garbage bin, architecture

### Blogs (0)
- Empty array — ready for posts via `manage_content.py` or CMS

---

## 4. Core Features

### 3D WebGL Hero (`app.js` → `initHero3D()`)
- Three.js (r160) lazy-loaded from CDN
- Animated microchip PCB with auto-orbit + mouse parallax
- WebGL detection with SVG fallback (`images/hero-card-back.svg`)
- Respects `prefers-reduced-motion` and `navigator.connection.saveData`

### Constellation Background
- 60-80 amber particles with mouse-reactive connection lines
- Theme-aware colors (amber/dark/light)
- Runs on all pages via `app.js` → `initConstellation()`

### Hero Particles
- Interactive particles attracting to cursor
- Canvas overlay on hero section

### Theme System (3 modes)
- **Amber** (default) — dark bg, amber accents
- **Dark** — pure dark, white text
- **Light** — light bg, dark text
- Persisted in `localStorage`, smooth CSS transitions
- Theme toggle in navbar (sun/moon/palette icons)

### Animations & Interactions
- Scroll reveal (IntersectionObserver)
- Animated counters (4+, 40+, 4, 100%)
- Skill bars with animated fill
- 3D card tilt on hover (`data-tilt`)
- Scroll-spy for active nav highlighting
- Share-link buttons on sections (clipboard copy + toast)
- Click-to-zoom lightbox for case study images
- Vertical timeline for experience (5 roles)

### CMS (Client-side GitHub API)
- Reads/writes `content.json` via GitHub Contents API
- Base64 encoding with Unicode-safe helpers (`toBase64`/`fromBase64`)
- Optimistic UI, event-delegated delete buttons
- Form validation + character counters
- Requires fine-grained PAT in `crm-github.js:20`

### Contact & Newsletter Forms
- Currently use `data-netlify="true"` — **must migrate to Formspree** for GitHub Pages
- Formspree integration documented in `FINAL-GO-LIVE.md`

### vCard Download
- `hardik-darji.vcf` — one-click contact import

### SEO & Accessibility
- JSON-LD `Person` schema
- Open Graph + Twitter cards
- Canonical URLs
- `manifest.json` (PWA)
- `robots` meta
- Semantic HTML, ARIA labels, focus-visible outlines
- Skip-to-main link on all pages
- `prefers-reduced-motion` respected
- `prefers-reduced-data` check for 3D assets

---

## 5. Technical Stack

| Category | Technology |
|----------|------------|
| HTML | Semantic HTML5, 6 pages + 5 CMS pages |
| CSS | Custom `styles.css` (558 lines) + Tailwind via CDN |
| JS | Vanilla ES6 modules pattern: `app.js` (750 lines), `renderer.js` (244), `blog-renderer.js`, `crm-*.js` |
| 3D | Three.js r160 (CDN) |
| Fonts | Inter + JetBrains Mono (Google Fonts) |
| Icons | Inline SVG |
| Hosting | GitHub Pages (static) |
| Forms | Formspree (to be configured) |
| CMS Auth | GitHub fine-grained PAT (to be configured) |
| Domain | Custom subdomain `hardikmdarji.work.gd` via CNAME |

---

## 6. Assets

### Images (in `images/`)
| File | Used In |
|------|---------|
| `project-telematics-hardware.svg` | Project 1 main |
| `project-telematics-architecture.svg` | Project 1 supportive |
| `project-telematics-dashboard.svg` | Project 1 supportive |
| `project-robot.svg` | Project 2 main |
| `project-robot-arch.svg` | Project 2 supportive |
| `project-garbage.svg` | Project 3 main |
| `project-garbage-arch.svg` | Project 3 supportive |
| `hero-card-back.svg` | 3D hero fallback |
| `og-image.svg` | Open Graph social preview |
| `favicon.svg` | Browser tab icon |
| `placeholder-project.svg` | CMS placeholder |

### Profile Image
- `Hardik Profile PIC.png` — displayed in hero section (circular, amber ring)

### Documents
- `HardikDarji CV.pdf` — Download CV buttons
- `hardik-darji.vcf` — Save contact button

---

## 7. Configuration Files

| File | Purpose |
|------|---------|
| `.nojekyll` | Required for GitHub Pages (prevents Jekyll processing) |
| `.gitignore` | Excludes `.kilo/`, `node_modules/`, `dist/`, `*.log`, `.env`, etc. |
| `manifest.json` | PWA manifest (name, icons, theme color) |
| `FINAL-GO-LIVE.md` | Step-by-step deployment guide |
| `manage_content.py` | Python CLI to add projects/blogs to `content.json` |

---

## 8. Deployment Checklist

### Required Before Go-Live
- [ ] **Formspree ID** in `index.html` (2 forms, lines ~843 & ~919)
- [ ] **GitHub PAT** in `crm-github.js:20` (fine-grained, Contents: R/W)
- [ ] **CNAME file** with `hardikmdarji.work.gd`

### Deploy Commands
```powershell
cd "C:\Users\AINHMD\OneDrive - Ammann Group\Desktop\all MY project data\Hardik Webpage"
echo "hardikmdarji.work.gd" > CNAME
git init
git add .
git commit -m "Go-live: Formspree forms, GitHub PAT, custom domain CNAME"
git branch -M main
git remote add origin https://github.com/Hardikdarji921/Hardik-webpage.git
git push -u origin main
```

### GitHub Settings
1. Settings → Pages → Source: **Deploy from branch** → `main` / `/(root)`
2. Custom domain: `hardikmdarji.work.gd` → Save
3. Wait for "DNS check passed" → Enable **Enforce HTTPS**

### DNS (at work.gd provider)
| Type | Host | Value |
|------|------|-------|
| CNAME | `@` | `hardikdarji921.github.io` |

---

## 9. Adding Content (Post-Launch)

### Option A: Python Script (Recommended)
```powershell
python manage_content.py
# Choose 1=Project, 2=Blog, follow prompts
git add . && git commit -m "Add new project" && git push
```

### Option B: CMS Web Interface
1. Visit `https://hardikmdarji.work.gd/crm.html`
2. Fill form, upload images
3. Click "Publish Project" / "Publish Blog Post"
4. Commits directly to `content.json` via GitHub API

---

## 10. Maintenance Notes

| Task | Frequency |
|------|-----------|
| Update GitHub PAT | Before expiry (max 1 year) |
| Renew domain | Annually |
| Add blog posts | As needed |
| Update experience/skills | When roles change |
| Check Formspree quota | Monthly (free: 50/month) |
| Monitor Lighthouse scores | Quarterly |

---

## 11. Known Limitations

1. **Forms** — Require Formspree (not Netlify) on GitHub Pages
2. **CMS PAT** — Client-side visible; production should use Cloudflare Worker/Netlify Function proxy
3. **Tailwind CDN** — ~300 KB; could be replaced with local build for performance
4. **SVGs** — Not optimized with SVGO (30-40% savings possible)
5. **No CI/CD** — Manual push deploy; could add GitHub Actions workflow
6. **No tests** — Manual QA only

---

## 12. File Structure (Clean)

```
Hardik-webpage/
├── index.html
├── projects.html
├── blogs.html
├── project-template.html
├── blog-template.html
├── 404.html
├── crm.html
├── crm-projects.html
├── crm-blogs.html
├── crm-edit-project.html
├── crm-edit-blog.html
├── crm-github.js
├── crm.js
├── crm-projects.js
├── crm-blogs.js
├── crm-edit-project.js
├── crm-edit-blog.js
├── crm-header.html
├── crm-nav.html
├── app.js
├── renderer.js
├── blog-renderer.js
├── data.js
├── styles.css
├── content.json
├── manifest.json
├── .nojekyll
├── .gitignore
├── CNAME
├── FINAL-GO-LIVE.md
├── manage_content.py
├── favicon.svg
├── Hardik Profile PIC.png
├── HardikDarji CV.pdf
├── hardik-darji.vcf
└── images/
    ├── project-telematics-hardware.svg
    ├── project-telematics-architecture.svg
    ├── project-telematics-dashboard.svg
    ├── project-robot.svg
    ├── project-robot-arch.svg
    ├── project-garbage.svg
    ├── project-garbage-arch.svg
    ├── hero-card-back.svg
    ├── og-image.svg
    ├── favicon.svg
    └── placeholder-project.svg
```

---

**Document generated:** 2026-09-26  
**Status:** Ready for deployment — complete `FINAL-GO-LIVE.md` steps