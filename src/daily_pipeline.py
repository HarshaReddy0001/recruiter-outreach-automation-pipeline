import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---- EDIT THESE IF YOUR FILE NAMES DIFFER ----
LINKEDIN_EXTRACTOR = ROOT / "output5" / "linkedin_extractor" / "extract_contacts.py"

# Pick the ONE google script you actually want to run:
GOOGLE_SCRIPT = ROOT / "src" / "google_leads_serper_fetch1.py"

MERGE_SCRIPT = ROOT / "src" / "merge_emails.py"
MAILER_SCRIPT = ROOT / "src" / "gmail_auto_sender.py"
# ---------------------------------------------

def run(cmd, step_name=""):
    print(f"\n==============================")
    print(f"STEP: {step_name}")
    print("RUN:", " ".join(str(x) for x in cmd))
    print("==============================\n")

    p = subprocess.run(cmd, cwd=ROOT, text=True)
    if p.returncode != 0:
        raise SystemExit(p.returncode)

def main():
    python = sys.executable

    # 0) quick sanity checks
    if not LINKEDIN_EXTRACTOR.exists():
        raise FileNotFoundError(f"LinkedIn extractor not found: {LINKEDIN_EXTRACTOR}")
    if not GOOGLE_SCRIPT.exists():
        raise FileNotFoundError(f"Google script not found: {GOOGLE_SCRIPT}")
    if not MERGE_SCRIPT.exists():
        raise FileNotFoundError(f"Merge script not found: {MERGE_SCRIPT}")
    if not MAILER_SCRIPT.exists():
        raise FileNotFoundError(f"Mailer script not found: {MAILER_SCRIPT}")

    # 1) LinkedIn -> output5/leads_emails.txt
    run([python, str(LINKEDIN_EXTRACTOR)], "LinkedIn Extractor (leads_emails.txt)")

    # 2) Google -> output5/google_emails.txt
    run([python, str(GOOGLE_SCRIPT)], "Google Serper (google_emails.txt)")

    # 3) Merge -> output5/all_emails.txt
    run([python, str(MERGE_SCRIPT)], "Merge Emails (all_emails.txt)")

    # 4) Send emails -> reads output5/all_emails.txt
    run([python, str(MAILER_SCRIPT)], "Gmail Auto Sender (send emails)")

    print("\n✅ DAILY PIPELINE DONE ✅")

if __name__ == "__main__":
    main()
