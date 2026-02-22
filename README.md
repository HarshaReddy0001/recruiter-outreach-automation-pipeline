<div align="center">

# 🚀 Google Leads Extractor & Automated Outreach System

**A modular, production-ready lead generation and outreach pipeline.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Gmail API](https://img.shields.io/badge/Gmail_API-Enabled-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](https://developers.google.com/gmail/api)
[![Serper API](https://img.shields.io/badge/Serper_API-Google_Search-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://serper.dev)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

*Automatically extract recruiter emails → scrape Google → merge leads → send personalized outreach → track everything. All on autopilot.*

</div>

---

## ✨ What This Does

| Feature | Description |
|--------|-------------|
| 🔎 **LinkedIn Boolean Search** | Manually search LinkedIn using Boolean queries to find hiring posts with recruiter emails |
| 🔍 **LinkedIn Email Extraction** | Regex-powered script parses copied post text and extracts all emails |
| 🌐 **Google Scraping** | Fetches search results via Serper API and extracts contact emails |
| 🔗 **Smart Merging** | Combines both sources and removes duplicate emails automatically |
| 📧 **Auto Email Sending** | Sends structured outreach emails via Gmail API |
| 📋 **Sent Log Tracking** | Prevents duplicate outreach with a persistent sent log |
| ⏰ **Daily Automation** | Fully automated daily execution via cron or Task Scheduler |

---

## 🏗️ System Architecture

```
 ┌──────────────────────────────────────────────┐
 │         MANUAL STEP (You do this)            │
 │                                              │
 │  LinkedIn Boolean Search → Open 30-50 Posts  │
 │  → Ctrl+A → Copy → Paste into linkedin.txt   │
 └──────────────────┬───────────────────────────┘
                    │
                    ▼
                        ┌─────────────────────────────┐
                        │       Daily Pipeline        │
                        │      daily_pipeline.py      │
                        │  (Orchestrates everything)  │
                        └──────────────┬──────────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
              ▼                        ▼                        ▼
 ┌────────────────────┐   ┌────────────────────┐   ┌────────────────────┐
 │ LinkedIn Extractor │   │  Google Scraper    │   │ Merge & Deduplicate│
 │ extract_contacts   │   │ google_leads_serper│   │  merge_emails.py   │
 │ reads linkedin.txt │   │   (Serper API)     │   │                    │
 └────────┬───────────┘   └────────┬───────────┘   └────────┬───────────┘
          │                        │                        │
          ▼                        ▼                        ▼
  leads_emails.txt        google_emails.txt          all_emails.txt
                                                           │
                                                           ▼
                                              ┌────────────────────────┐
                                              │   Gmail Auto Sender    │
                                              │  gmail_auto_sender.py  │
                                              └────────────┬───────────┘
                                                           │
                                                           ▼
                                                     sent_log.txt
```

---

## 📂 Project Structure

```
google_leads_extractor/
│
├── 📁 output5/
│   ├── leads_emails.txt        ← LinkedIn extracted emails
│   ├── google_emails.txt       ← Google scraped emails
│   ├── all_emails.txt          ← Merged & deduplicated list
│   └── sent_log.txt            ← Tracks sent emails
│
├── 📁 src/
│   ├── gmail_auto_sender.py    ← Gmail outreach engine
│   ├── merge_emails.py         ← Deduplication logic
│   └── daily_pipeline.py       ← Master orchestrator
│
├── 📁 output5/linkedin_extractor/
│   ├── linkedin.txt            ← ⚠️ YOU CREATE THIS (paste LinkedIn posts here)
│   └── extract_contacts.py     ← Extracts emails from linkedin.txt
│
├── google_leads_serper_fetch1.py  ← Google/Serper scraper
├── credentials.json               ← Gmail OAuth credentials
├── token.json                     ← Gmail OAuth token (gitignored)
├── requirements.txt
└── README.md
```

---

## 🔎 Step 0 — LinkedIn Lead Collection (Manual Boolean Search)

> ⚠️ **This is the most important step.** The pipeline cannot run without `linkedin.txt`. This step is done **manually by you** before running any code.

LinkedIn blocks automated scraping — so this project uses a smart manual approach: **Boolean search queries** to find posts where recruiters publicly share their email addresses.

---

### 📌 How It Works

LinkedIn's search lets you filter **Posts** using Boolean logic. We use this to find hiring posts that contain email addresses, then copy the text and feed it to our extractor script.

---

### 🧠 Boolean Search Queries to Use

Go to **LinkedIn → Search bar → Filter by: Posts**

Paste any of these queries to find recruiter posts with emails:

```
("email me" OR "send your resume" OR "send your CV") AND ("Data Scientist" OR "Data Science")
```
```
"Technical Recruiter" "Data Science" "Google" "USA"
```
```
("hiring data scientist" OR "hiring ai engineer") ("@") ("send resume" OR "email")
```
```
("hiring gen AI") ("@") ("send resume" OR "email") -senior -sr
```
```
("hiring gen AI") AND ("USA") AND ("@" OR "email")
```

**Hashtag-based searches (also very effective):**
```
#hiring #datascientist #usa
#hiring #AIengineer #usa
#datascience #recruiter #hiring
#genai #usa #jobs
```

> 💡 **Pro tip:** Filter by **"Past 24 hours"** or **"Past week"** to get the freshest leads with active recruiters.

---

### 📋 Step-by-Step Manual Collection

**Step 1 — Search LinkedIn**
1. Go to [linkedin.com](https://linkedin.com) → click the Search bar
2. Type a Boolean query from above
3. Hit Enter → click **Posts** tab in the filters

**Step 2 — Open & Expand Posts**
1. Browse through results — look for posts mentioning email addresses
2. Click **"See more"** on each post to expand the full text
3. Collect **30–50 posts** per session for a good batch of leads

**Step 3 — Copy All Post Text**
1. Click anywhere on the page
2. Press `Ctrl + A` to select all visible content
3. Press `Ctrl + C` to copy

**Step 4 — Save as `linkedin.txt`**
1. Open **Notepad** (or any plain text editor)
2. Press `Ctrl + V` to paste
3. Save the file as:

```
linkedin_extractor/linkedin.txt
```

> The extractor script reads this exact file path. Make sure the filename and location match.

**Step 5 — Run the Extractor**
```bash
python output5\linkedin_extractor\extract_contacts.py
```

The script will:
- Read `linkedin.txt`
- Use regex to find all email patterns
- Remove duplicates
- Save results to `output5/leads_emails.txt`

---

### 🔄 Full LinkedIn Data Flow

```
LinkedIn Boolean Search
        ↓
Open 30–50 Posts → Click "See more"
        ↓
Ctrl+A → Ctrl+C (copy all text)
        ↓
Paste into Notepad → Save as linkedin.txt
        ↓
Run extract_contacts.py
        ↓
output5/leads_emails.txt
        ↓
Merge with Google leads → Gmail Sender
```

---

### ⚠️ Best Practices

- Don't copy hundreds of posts at once — stay under 50 per session
- Focus on **recent posts** to reach active recruiters
- Avoid copying the same posts twice (causes duplicates, though the merge step handles these)
- Use **targeted queries** — the more specific, the better the email quality

---

## ⚡ Quick Start

### 1. Clone & Setup Environment

```bash
git clone <repo-url>
cd google_leads_extractor

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS

# Install dependencies
pip install -r requirements.txt
```

### 2. Gmail API Setup

> You need Gmail API credentials to send emails.

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project → Enable **Gmail API**
3. Create **OAuth 2.0 Client ID** (Desktop App)
4. Download and rename the file to `credentials.json`
5. Place it in the project root

### 3. Run the Full Pipeline

```bash
python -u src\daily_pipeline.py
```

That's it. The pipeline will handle everything automatically.

---

## 🔄 Manual Step-by-Step Execution

Prefer running each step individually? Here's the full flow:

```bash
# Step 1 — Extract LinkedIn emails
python -u output5\linkedin_extractor\extract_contacts.py
# Output: output5\leads_emails.txt

# Step 2 — Scrape Google via Serper API
python -u google_leads_serper_fetch1.py
# Output: output5\google_emails.txt

# Step 3 — Merge & deduplicate
python -u src\merge_emails.py
# Output: output5\all_emails.txt

# Step 4 — Send outreach emails
python -u src\gmail_auto_sender.py
# Updates: output5\sent_log.txt
```

---

## ⏰ Automated Daily Scheduling

### 🪟 Windows — Task Scheduler

| Field | Value |
|-------|-------|
| **Program** | `C:\Path\To\.venv\Scripts\python.exe` |
| **Arguments** | `src\daily_pipeline.py` |
| **Start In** | `C:\Path\To\google_leads_extractor` |

### 🐧 Linux — Cron Job

```bash
# Runs every day at 9:00 AM
0 9 * * * /home/user/google_leads_extractor/venv/bin/python \
  /home/user/google_leads_extractor/src/daily_pipeline.py \
  >> /home/user/logs/outreach.log 2>&1
```

### 🐧 Linux — First-Time VPS Setup

```bash
git clone <repo-url>
cd google_leads_extractor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Authenticate Gmail OAuth (do this once manually)
python src/gmail_auto_sender.py
```

---

## 🔒 Security Notes

> Take these seriously — your Gmail account depends on it.

- **Never push `token.json` to Git** — add it to `.gitignore`
- Keep daily sending limits conservative to avoid account flags
- Monitor your Gmail account health regularly
- Avoid aggressive sending patterns that trigger spam filters

**Recommended `.gitignore` additions:**
```
token.json
credentials.json
output5/sent_log.txt
```

---

## 🗺️ Complete Data Flow

```
[YOU] LinkedIn Boolean Search
        ↓
[YOU] Copy post text → Save as linkedin.txt
        ↓
LinkedIn Extractor ──┐
                     ├──► Merge & Deduplicate ──► Gmail Sender ──► sent_log.txt
Google (Serper) ─────┘
```

1. **You (manual)** — Boolean search LinkedIn → copy posts → save as `linkedin.txt`
2. **`extract_contacts.py`** — Reads `linkedin.txt`, extracts emails → `leads_emails.txt`
3. **`google_leads_serper_fetch1.py`** — Finds emails via Serper API → `google_emails.txt`
4. **`merge_emails.py`** — Combines both sources, removes duplicates → `all_emails.txt`
5. **`gmail_auto_sender.py`** — Sends to new contacts only, updates `sent_log.txt`
6. **`daily_pipeline.py`** — Runs steps 2–5 automatically in sequence

---

## 🛣️ Roadmap

- [ ] SQLite/PostgreSQL backend to replace text files
- [ ] Dockerized deployment
- [ ] Web dashboard for campaign analytics
- [ ] Rate limiting & smart send scheduling
- [ ] Email open/reply tracking

---

## 📌 Version Info

| Property | Value |
|----------|-------|
| **Version** | 1.0 |
| **Architecture** | Modular CLI Pipeline |
| **Deployment** | Local / Scheduler / VPS |
| **Storage** | Text-file based (upgradeable to DB) |

---

<div align="center">

Made with ☕ and Python &nbsp;|&nbsp; Contributions welcome

</div>
