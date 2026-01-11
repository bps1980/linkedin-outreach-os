# LinkedIn Outreach OS — Demo Version

This repository contains a **safe, minimal demo** of the LinkedIn Outreach OS — a fully autonomous outreach engine originally built to power Finovia and POSOVIA.

The full system mines leads, sends connection requests, detects acceptances, and handles follow‑ups automatically. It runs 24/7 using a Celery automation layer and a product‑aware routing system.

This demo includes:
- Example placeholder scraper
- Example message template
- Minimal placeholder database schema
- Screenshots of the real system
- Architecture overview
- Link to the Pro version

---

## 🚀 What the Full System Does

The full LinkedIn Outreach OS includes:

- **Autonomous lead mining**  
  Scrapes LinkedIn search results for founders, operators, investors, and product‑specific audiences.

- **Connection sending engine**  
  Opens LinkedIn, sends connection requests, rotates templates, and updates lead status.

- **Acceptance detection**  
  Detects new accepted connections and triggers the correct follow‑up sequence.

- **Follow‑up automation**  
  Sends post‑accept messages and scheduled follow‑ups with product‑aware templates.

- **Celery + Beat automation layer**  
  Runs scraping, sending, acceptance checks, and follow‑ups on a schedule.

- **Multi‑product routing**  
  Finovia, POSOVIA, and investor audiences each get their own messaging logic.

- **SQLite pipeline**  
  Tracks leads, statuses, messages, timestamps, and campaign state.

---

## 📁 Repository Structure (Demo Only)

