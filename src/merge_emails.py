from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output5"
OUT.mkdir(parents=True, exist_ok=True)

LINKEDIN = OUT / "leads_emails.txt"
GOOGLE = OUT / "google_emails.txt"
MERGED = OUT / "all_emails.txt"

BLOCKED = {"gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com"}

def load(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8", errors="ignore").splitlines() if line.strip()}

def is_allowed(email: str) -> bool:
    if "@" not in email:
        return False
    domain = email.split("@")[-1].lower()
    return domain not in BLOCKED

linkedin_emails = {e for e in load(LINKEDIN) if is_allowed(e)}
google_emails = {e for e in load(GOOGLE) if is_allowed(e)}

merged = sorted(linkedin_emails | google_emails)

MERGED.write_text("\n".join(merged) + ("\n" if merged else ""), encoding="utf-8")

print("--- MERGE DONE ---")
print("LinkedIn:", len(linkedin_emails))
print("Google:", len(google_emails))
print("Merged unique:", len(merged))
print("Saved:", MERGED)
