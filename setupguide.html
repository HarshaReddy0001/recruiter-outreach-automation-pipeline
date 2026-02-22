<div align="center">

# 🛠️ SETUP GUIDE
## Google Leads Extractor & Automated Outreach System

**A complete step-by-step installation and usage manual.**
*Every click. Every file. Every command. Nothing skipped.*

---

[![Windows](https://img.shields.io/badge/Windows-10%2F11-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![VS Code](https://img.shields.io/badge/VS%20Code-Required-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Gmail API](https://img.shields.io/badge/Gmail_API-OAuth2-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](https://developers.google.com/gmail/api)
[![Serper](https://img.shields.io/badge/Serper_API-Free_Tier-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://serper.dev)
[![Setup Time](https://img.shields.io/badge/Setup_Time-45–60_min-brightgreen?style=for-the-badge)](.)

---

> 💡 **Who this guide is for:** Anyone — even if you have never used Python, APIs, or a terminal before.
> Follow this guide from top to bottom. The system **will work.**

</div>

---

## 📋 Table of Contents

| # | Section | Time |
|---|---------|------|
| [00](#-00--system-overview) | System Overview | 3 min read |
| [01](#-01--before-you-begin) | Before You Begin — checklist | 2 min |
| [02](#-02--install-python) | Install Python on Windows | 5 min |
| [03](#-03--setup-vs-code) | Setup VS Code + integrated terminal | 5 min |
| [04](#-04--get-the-project-files) | Get the Project Files | 3 min |
| [05](#-05--create-virtual-environment) | Create Virtual Environment | 3 min |
| [06](#-06--install-dependencies) | Install Dependencies | 3 min |
| [07](#-07--get-your-serper-api-key) | Get Your Serper API Key | 3 min |
| [08](#-08--gmail-api-setup) | Gmail API Setup — full walkthrough | 15 min |
| [09](#-09--add-api-key--file-path-to-scripts) | Add API Key & File Path to Scripts | 3 min |
| [10](#-10--linkedin-manual-collection) | LinkedIn Manual Collection | 10 min |
| [11](#-11--run-the-pipeline) | Run the Pipeline | 2 min |
| [12](#-12--automate-daily-execution) | Automate Daily Execution | 5 min |
| [13](#-13--verify-everything-worked) | Verify Everything Worked | 3 min |
| [14](#-14--troubleshooting) | Troubleshooting — 8 common errors | reference |
| [15](#-15--security-checklist) | Security Checklist | 2 min |

---

## 🗺️ 00 — System Overview

> Understand the full pipeline **before** you touch a single file.

There are **two types of steps** in this system:

| Type | Who Does It | Steps |
|------|------------|-------|
| 🟡 **Manual** | You | LinkedIn search → copy posts → save `linkedin.txt` |
| 🔵 **Automatic** | The scripts | Extract → Scrape Google → Merge → Send emails |

---

### Full Pipeline Architecture

```
╔══════════════════════════════════════════════════════╗
║           🟡 YOU DO THIS MANUALLY                    ║
║                                                      ║
║   LinkedIn Boolean Search  →  Open 30-50 Posts       ║
║   →  Ctrl+A  →  Ctrl+C  →  Paste into linkedin.txt  ║
╚══════════════════════════════╦═══════════════════════╝
                               ║
                               ▼
        ┌──────────────────────────────────────┐
        │          daily_pipeline.py           │
        │       (Orchestrates everything)      │
        └─────────┬──────────────────┬─────────┘
                  │                  │
      ┌───────────▼────┐    ┌────────▼──────────┐
      │  LinkedIn      │    │  Google Scraper   │
      │  Extractor     │    │  (Serper API)     │
      │extract_        │    │google_leads_      │
      │contacts.py     │    │serper_fetch1.py   │
      └───────┬────────┘    └────────┬──────────┘
              │                      │
              ▼                      ▼
      leads_emails.txt      google_emails.txt
              │                      │
              └──────────┬───────────┘
                         ▼
                  merge_emails.py
                         │
                         ▼
                   all_emails.txt
                         │
                         ▼
              gmail_auto_sender.py
                         │
                         ▼
                   sent_log.txt ✓
```

---

### What You Will Have After Setup

- ✅ Recruiter emails extracted from LinkedIn posts you copy manually
- ✅ Additional emails scraped from Google via Serper API
- ✅ Both lists merged and deduplicated automatically
- ✅ Outreach emails sent via your Gmail — zero manual clicking
- ✅ Sent log tracking — nobody gets emailed twice
- ✅ Daily automation via Windows Task Scheduler

---

## ✅ 01 — Before You Begin

Run through this checklist **before starting anything else.**

- [ ] Windows 10 or 11
- [ ] Stable internet connection
- [ ] A Gmail account *(this will send the outreach emails)*
- [ ] A LinkedIn account *(free tier works fine)*
- [ ] 45–60 minutes of uninterrupted time
- [ ] A browser already logged into Google

> ⚠️ **Do not start if you will be interrupted.** The Gmail API setup (Step 08) must be completed in one sitting.

---

## 🐍 02 — Install Python

> **Already have Python?** Open Command Prompt → run `python --version`.
> If you see `Python 3.8.x` or higher → **skip to Step 03.**

### Download & Install

**1.** Go to [python.org/downloads](https://www.python.org/downloads/) → click the big yellow **"Download Python 3.x.x"** button.

**2.** Open your **Downloads** folder → double-click the installer file (e.g. `python-3.12.0-amd64.exe`).

**3.** ⚠️ **STOP — do this before clicking anything else:**

```
┌──────────────────────────────────────────────────────┐
│  Python 3.12.0 (64-bit) Setup                        │
│                                                      │
│  ○  Install Now                                      │
│  ○  Customize installation                           │
│                                                      │
│  ☑  Add Python 3.12 to PATH   ← CHECK THIS BOX      │
│                                  BEFORE YOU CLICK    │
└──────────────────────────────────────────────────────┘
```

This is the **#1 mistake** beginners make. Without this, Python will not work from the terminal.

**4.** Click **"Install Now"** → wait for it to finish → click **Close**.

### Verify the Install

Press `Win + R` → type `cmd` → press Enter. In the black window:

```bash
python --version
```

✅ **Good:** `Python 3.12.0` (or any 3.x.x version)

❌ **Problem:** `'python' is not recognized` → you missed the PATH checkbox. Uninstall Python from Control Panel → reinstall → check the box.

---

## 💻 03 — Setup VS Code

### Install VS Code

**1.** Go to [code.visualstudio.com](https://code.visualstudio.com/) → click **"Download for Windows"** → run the installer with all default settings.

**2.** Open VS Code → press `Ctrl + Shift + X` to open Extensions → search **"Python"** → click **Install** on the extension by **Microsoft**.

---

### Open the Project Folder

**1.** Click **File → Open Folder** → navigate to your `google_leads_extractor` folder → click **"Select Folder"**.

**2.** Open the integrated terminal — this is where ALL commands in this guide are run:

```
Shortcut:  Ctrl + `  (backtick — the key directly above Tab)
```

A terminal panel opens at the bottom of VS Code.

**3.** Confirm the terminal is in the right folder. It should show:

```
PS C:\Users\YourName\Desktop\google_leads_extractor>
```

> 💡 If the path does not end with `google_leads_extractor`, run:
> ```bash
> cd C:\Users\YourName\Desktop\google_leads_extractor
> ```

---

### Tell VS Code Which Python to Use

After creating the virtual environment in Step 05, do this:

1. Press `Ctrl + Shift + P`
2. Type `Python: Select Interpreter` → press Enter
3. Select the option showing `.venv`:
   ```
   Python 3.x.x ('.venv': venv) ./.venv/Scripts/python.exe
   ```

---

## 📁 04 — Get the Project Files

### Option A — Git Clone

```bash
# Run in the VS Code terminal
git clone <your-github-repo-url>
cd google_leads_extractor
```

### Option B — Download ZIP (No Git needed)

**1.** Go to the GitHub page → click green **"Code"** button → **"Download ZIP"**

**2.** Open Downloads → right-click the ZIP → **"Extract All"** → choose Desktop or Documents

**3.** In VS Code → **File → Open Folder** → select the extracted folder

---

### Expected Folder Structure

```
📁 google_leads_extractor/
│
├── 📁 output5/
│   ├── 📁 linkedin_extractor/
│   │   └── 📄 extract_contacts.py
│   ├── 📄 leads_emails.txt       ← created automatically after running
│   ├── 📄 google_emails.txt      ← created automatically after running
│   ├── 📄 all_emails.txt         ← created automatically after running
│   └── 📄 sent_log.txt           ← created automatically after running
│
├── 📁 src/
│   ├── 📄 gmail_auto_sender.py
│   ├── 📄 merge_emails.py
│   └── 📄 daily_pipeline.py
│
├── 📄 google_leads_serper_fetch1.py  ← you add Serper key here (Step 09)
├── 📄 credentials.json               ← you place this here (Step 08)
├── 📄 token.json                     ← auto-created after Gmail auth (Step 08)
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🧪 05 — Create Virtual Environment

> **What is this?** A private, isolated copy of Python just for this project. Prevents conflicts with other Python projects. Always use one.

In the VS Code integrated terminal:

```bash
# Create the virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\activate
```

### How You Know It Worked

Your terminal prompt changes to show `(.venv)` at the start:

```
(.venv) PS C:\Users\YourName\Desktop\google_leads_extractor>
```

✅ That `(.venv)` prefix = virtual environment is active.

> ⚠️ **Every time you open a new VS Code terminal**, run `.venv\Scripts\activate` again before running any scripts. It does not stay active between sessions.

---

## 📦 06 — Install Dependencies

Make sure `(.venv)` is visible in your terminal, then run:

```bash
pip install -r requirements.txt
```

Lots of scrolling text will appear — this is normal. Takes 1–3 minutes.

### What Gets Installed

| Package | What It Does |
|---------|-------------|
| `requests` | HTTP calls to the Serper API |
| `beautifulsoup4` | Parses HTML from scraped pages |
| `lxml` | Fast HTML parser backend |
| `google-api-python-client` | Core Gmail API client |
| `google-auth` | Google authentication handling |
| `google-auth-oauthlib` | OAuth 2.0 login flow |
| `google-auth-httplib2` | Gmail HTTP transport layer |
| `python-dotenv` | Load config from `.env` files |
| `tqdm` | Progress bar while sending emails |

### Verify

```bash
pip list
```

✅ You should see `requests`, `beautifulsoup4`, `google-api-python-client`, and `tqdm` in the output.

> ❌ **If you see errors:** Run `pip install --upgrade pip` first, then retry `pip install -r requirements.txt`.

---

## 🔑 07 — Get Your Serper API Key

> Serper gives the script access to real Google Search results. **Free tier = 2,500 searches/month.** No credit card required.

**1.** Go to [serper.dev](https://serper.dev) → click **"Get Started"** or **"Sign Up"**

**2.** Create a free account with your email → verify your email if prompted

**3.** After logging in → find **"API Key"** in the left sidebar or dashboard

**4.** Your key looks like this:

```
a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2
```

**5.** Click the **Copy** button — you paste this into a script in Step 09.

---

## 📧 08 — Gmail API Setup

> ⚠️ **Most detailed step in this guide.** Read all 5 sub-steps once before starting. Done **one time only** — after that, `token.json` handles Gmail authorization automatically.

---

### 8.1 — Create a Google Cloud Project

**1.** Go to [console.cloud.google.com](https://console.cloud.google.com/) → sign in with the Gmail that will send outreach emails.

**2.** Click the **project dropdown** at the top of the page.

**3.** In the popup → click **"New Project"** (top right corner).

**4.** Fill in:
- **Project name:** anything — e.g. `leads-outreach`
- **Location:** leave as "No organization"

**5.** Click **Create** → wait a few seconds.

**6.** Click the dropdown again → select your new project to confirm you are inside it.

---

### 8.2 — Enable the Gmail API

**1.** In the top search bar → type `Gmail API` → press Enter

**2.** Click **"Gmail API"** in results

**3.** Click the blue **"Enable"** button → wait for confirmation ✅

---

### 8.3 — Configure OAuth Consent Screen

> Required by Google before you can create credentials — even for private personal apps.

**1.** Left sidebar → **APIs & Services** → **OAuth consent screen**

**2.** Select **"External"** → click **Create**

**3.** Fill in required fields only:

| Field | What to Enter |
|-------|--------------|
| App name | Anything — e.g. `Leads Outreach` |
| User support email | Select your email from dropdown |
| Developer contact information | Type your email address |

**4.** Click **"Save and Continue"**

**5.** On the **Scopes** screen → do **NOT** add anything → **"Save and Continue"**

**6.** On the **Test Users** screen → click **"+ Add Users"** → type your Gmail → **"Add"** → **"Save and Continue"**

**7.** Click **"Back to Dashboard"** ✅

---

### 8.4 — Create OAuth 2.0 Credentials

**1.** Left sidebar → **APIs & Services** → **Credentials**

**2.** Click **"+ Create Credentials"** → **"OAuth client ID"**

**3.** Application type → select **"Desktop app"**

**4.** Name → type anything (e.g. `leads-client`) → click **Create**

**5.** Popup appears → click **"Download JSON"**

**6.** The file downloads with a long name like:

```
client_secret_123456789-abc.apps.googleusercontent.com.json
```

**7.** **Rename it** to exactly: `credentials.json`

**8.** **Move it** into your project root — same folder as `README.md`:

```
google_leads_extractor\
├── credentials.json   ← PUT IT HERE
└── README.md
```

---

### 8.5 — First-Time Gmail Authorization (One Time Only)

In VS Code terminal (with `(.venv)` active):

```bash
python src\gmail_auto_sender.py
```

**What happens:**

**1.** A browser window opens automatically *(if not, a URL appears in terminal — paste it in your browser)*

**2.** You see this warning — it is **completely normal and safe:**

```
┌────────────────────────────────────────────┐
│  Google hasn't verified this app           │
│                                            │
│  [Back to safety]     [Advanced ▼]         │
└────────────────────────────────────────────┘

→ Click "Advanced"
→ Click "Go to [app name] (unsafe)"
→ Click "Continue"
```

**3.** Browser shows: *"The authentication flow has completed."* — close the tab.

**4.** In VS Code Explorer panel — you should now see `token.json` in the project root. ✅

> ✅ You now have `credentials.json` + `token.json`. Gmail is fully configured. You never need to redo this unless you delete `token.json`.

---

## ⚙️ 09 — Add API Key & File Path to Scripts

### Add the Serper API Key

**1.** In VS Code Explorer → click `google_leads_serper_fetch1.py` to open it

**2.** Press `Ctrl + F` → search for `SERPER_API_KEY`

**3.** Replace the placeholder:

```python
# BEFORE:
SERPER_API_KEY = 'YOUR_API_KEY_HERE'

# AFTER — paste your real key:
SERPER_API_KEY = 'a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2'
```

**4.** Press `Ctrl + S` to save ✅

---

### Set the linkedin.txt File Path

**1.** Open `output5\linkedin_extractor\extract_contacts.py` in VS Code

**2.** Find the file path variable and update it:

```python
# Set this to your actual full Windows path:
FILE_PATH = r"C:\Users\YourName\Desktop\google_leads_extractor\output5\linkedin_extractor\linkedin.txt"
```

**3.** Press `Ctrl + S` ✅

> 💡 **Easy way to get the exact path:** Open File Explorer → navigate to the `linkedin_extractor` folder → hold `Shift` + right-click any empty space → click **"Copy as path"** → paste into the script. Add `r` before the opening quote: `r"C:\..."` to prevent Windows backslash errors.

> ⚠️ Never push `google_leads_serper_fetch1.py` to GitHub with a real API key in it. Replace it with `'YOUR_API_KEY_HERE'` before committing.

---

## 🔎 10 — LinkedIn Manual Collection

> ⚠️ **Done by you manually before every pipeline run.** LinkedIn blocks all automated scraping. This manual approach keeps your account safe.

---

### Step 10.1 — Log Into LinkedIn

Go to [linkedin.com](https://www.linkedin.com) → sign in.

---

### Step 10.2 — Boolean Search for Recruiter Posts

Click the **LinkedIn search bar** → paste a query → press Enter:

**🔥 Best performing — Data Science & AI/ML:**

```
("email me" OR "send your resume" OR "send your CV") AND ("Data Scientist" OR "Data Science")
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

```
"Technical Recruiter" "Data Science" "Google" "USA"
```

**Hashtag searches:**

```
#hiring #datascientist #usa
#hiring #AIengineer #usa
#genai #usa #jobs
#datascience #recruiter #hiring
```

---

### Step 10.3 — Filter to Posts + Recent Date

**1.** Click the **"Posts"** tab below the search bar

**2.** Find the **"Date posted"** filter → select **"Past week"** or **"Past 24 hours"**

---

### Step 10.4 — Expand Posts

**1.** Scroll through results — look for posts with `@` symbols or email mentions

**2.** Click **"...see more"** on each relevant post — emails are often in the collapsed part

**3.** Expand **30–50 posts** per session

> 💡 Expand posts in-place on the results page — don't open new tabs. This way `Ctrl+A` captures all of them at once.

---

### Step 10.5 — Copy All Content

**1.** Scroll back to the top of the page

**2.** Click once on a blank area (not a button)

**3.** Press `Ctrl + A` — selects everything visible

**4.** Press `Ctrl + C` — copies it all

---

### Step 10.6 — Save as `linkedin.txt`

**1.** Press `Win + R` → type `notepad` → Enter

**2.** Press `Ctrl + V` to paste

**3.** Click **File → Save As**:
   - Navigate to: `google_leads_extractor` → `output5` → `linkedin_extractor`
   - File name: `linkedin.txt`
   - Save as type: `Text Documents (*.txt)`
   - Click **Save**

**File must be saved here:**

```
google_leads_extractor/
└── output5/
    └── linkedin_extractor/
        ├── linkedin.txt          ← ✅ YOUR FILE GOES HERE
        └── extract_contacts.py
```

> ⚠️ **Windows double-extension trap:** Notepad sometimes saves as `linkedin.txt.txt`.
> Check: File Explorer → View tab → enable **"File name extensions"**. If you see `.txt.txt` → right-click → Rename → remove the extra `.txt`.

---

## 🚀 11 — Run the Pipeline

**Pre-run checklist:**

- [ ] `(.venv)` is visible in your terminal prompt
- [ ] `credentials.json` in project root
- [ ] `token.json` in project root
- [ ] `linkedin.txt` saved in `output5\linkedin_extractor\`
- [ ] Serper API key added to `google_leads_serper_fetch1.py`
- [ ] File path updated in `extract_contacts.py`

---

### Option A — Each Script Individually

```bash
# STEP 1: Extract emails from linkedin.txt
python -u output5\linkedin_extractor\extract_contacts.py
# → output5\leads_emails.txt

# STEP 2: Scrape Google via Serper API
python -u google_leads_serper_fetch1.py
# → output5\google_emails.txt

# STEP 3: Merge and deduplicate
python -u src\merge_emails.py
# → output5\all_emails.txt

# STEP 4: Send outreach emails
python -u src\gmail_auto_sender.py
# → output5\sent_log.txt
```

---

### Option B — Full Pipeline in One Command

```bash
python -u src\daily_pipeline.py
```

---

### Expected Output

```
[1/4] Reading linkedin.txt...
      → Found 24 unique emails → saved to leads_emails.txt ✓

[2/4] Querying Serper API...
      → Found 19 emails → saved to google_emails.txt ✓

[3/4] Merging & deduplicating...
      → 38 unique emails → saved to all_emails.txt ✓

[4/4] Sending emails...
      [████████████████████] 38/38 sent
      → sent_log.txt updated ✓

Pipeline complete ✓
```

> ⚠️ Before running the Gmail sender for real — open `src\gmail_auto_sender.py` and confirm the email subject, body, and your name are correct. Run a test to yourself first (Step 13).

---

## ⏰ 12 — Automate Daily Execution

### Windows Task Scheduler

**1.** Press `Win + S` → search **"Task Scheduler"** → open it

**2.** Right panel → **"Create Basic Task"**

**3.** Name: `Leads Pipeline Daily` → Next

**4.** Trigger: **Daily** → Next

**5.** Time: e.g. `9:00:00 AM` → Next

**6.** Action: **"Start a program"** → Next

**7.** Fill in:

| Field | Value |
|-------|-------|
| **Program/script** | `C:\Users\YourName\Desktop\google_leads_extractor\.venv\Scripts\python.exe` |
| **Add arguments** | `src\daily_pipeline.py` |
| **Start in** | `C:\Users\YourName\Desktop\google_leads_extractor` |

> 💡 Find your exact Python path — in VS Code terminal run `where python`. Copy the path containing `.venv\Scripts\python.exe`.

**8.** Click **Finish**

**9.** Right-click the task → **"Run"** → confirm it works ✅

---

## ✔️ 13 — Verify Everything Worked

| File | Location | What to Check |
|------|----------|--------------|
| `leads_emails.txt` | `output5/` | Email addresses, one per line |
| `google_emails.txt` | `output5/` | Emails from Google scraping |
| `all_emails.txt` | `output5/` | Merged, deduplicated list |
| `sent_log.txt` | `output5/` | Emails sent outreach |
| `token.json` | project root | File exists = Gmail auth OK |

### Test Before Going Live

**1.** Add your own email to `output5\all_emails.txt`

**2.** Run `python -u src\gmail_auto_sender.py`

**3.** Check your inbox — confirm email arrives and looks correct

**4.** Open `output5\sent_log.txt` → delete all content → save the empty file

**5.** Run the full pipeline for real ✅

---

## 🔧 14 — Troubleshooting

### ❌ `'python' is not recognized`
**Cause:** Python not added to PATH. **Fix:** Reinstall Python → check "Add Python to PATH" on first screen.

---

### ❌ `ModuleNotFoundError: No module named 'requests'`
**Cause:** Virtual environment not activated. **Fix:**
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

---

### ❌ `FileNotFoundError: linkedin.txt not found`
**Cause:** File missing, named `linkedin.txt.txt`, or wrong path in script. **Fix:** Check extension in File Explorer. Rename if needed. Update `FILE_PATH` in `extract_contacts.py`.

---

### ❌ `credentials.json not found`
**Cause:** Wrong filename or wrong folder. **Fix:** File must be named exactly `credentials.json` in the same folder as `README.md`.

---

### ❌ `"Google hasn't verified this app"` in browser
**This is normal and safe.** Click **"Advanced"** → **"Go to [app name] (unsafe)"** → **"Continue"**.

---

### ❌ `Token has been expired or revoked`
**Fix:**
```bash
del token.json
python src\gmail_auto_sender.py
# Re-authorize in browser
```

---

### ❌ `leads_emails.txt` is empty
**Cause:** Posts copied had no visible email addresses. **Fix:** Use queries with `("@")`. Click **"see more"** on each post before `Ctrl+A`. Filter to **"Past 24 hours"**.

---

### ❌ Gmail sender sends 0 emails
**Cause:** All emails already in `sent_log.txt` (prevents duplicates — works as intended). **Fix for reset:**
```
Open output5\sent_log.txt → delete all content → save empty file → run again
```

---

## 🔒 15 — Security Checklist

- [ ] `token.json` added to `.gitignore`
- [ ] `credentials.json` added to `.gitignore`
- [ ] Serper API key replaced with placeholder before GitHub push
- [ ] Email template confirmed in `gmail_auto_sender.py`
- [ ] Tested with your own email first
- [ ] Daily send volume under **100 emails/day** to avoid Gmail spam flags
- [ ] Only targeting people who publicly posted their email on LinkedIn

### Recommended `.gitignore`

```
token.json
credentials.json
output5/sent_log.txt
.venv/
```

---

<div align="center">

---

### 🎉 You're All Set

**Your daily workflow going forward:**

```
1. LinkedIn Boolean search → copy posts → save linkedin.txt
2. python -u src\daily_pipeline.py
3. Done.
```

---

*Setup Guide v1.0 · Google Leads Extractor & Automated Outreach System*
*Windows 10/11 + VS Code + Python 3.8+*

</div>
