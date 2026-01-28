import re
from pathlib import Path

# -----------------------------
# PATH SETUP (IMPORTANT)
# -----------------------------
SCRIPT_DIR = Path(__file__).parent            # output5/linkedin_extractor
OUTPUT5_DIR = SCRIPT_DIR.parent               # output5/

INPUT_FILE = SCRIPT_DIR / "linkedin_group.txt"

EMAIL_OUTPUT = OUTPUT5_DIR / "leads_emails.txt"
PHONE_OUTPUT = OUTPUT5_DIR / "leads_phones.txt"

BLOCKED_DOMAINS = {
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "hotmail.com",
    "icloud.com"
}

# -----------------------------
# READ INPUT FILE
# -----------------------------
if not INPUT_FILE.exists():
    raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

raw_text = INPUT_FILE.read_text(encoding="utf-8", errors="ignore")

print("Total characters:", len(raw_text))

# -----------------------------
# EXTRACT EMAILS
# -----------------------------
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
all_emails = set(re.findall(email_pattern, raw_text))

filtered_emails = sorted(
    email for email in all_emails
    if email.split("@")[-1].lower() not in BLOCKED_DOMAINS
)

print("Total emails found:", len(all_emails))
print("Filtered business emails:", len(filtered_emails))

# -----------------------------
# EXTRACT PHONE NUMBERS
# -----------------------------
phone_pattern = r"(\+1[\s-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
phones = sorted(set(m.group() for m in re.finditer(phone_pattern, raw_text)))

print("Phone numbers found:", len(phones))

# -----------------------------
# SAVE OUTPUTS (PROJECT-2 READY)
# -----------------------------
EMAIL_OUTPUT.write_text("\n".join(filtered_emails), encoding="utf-8")
PHONE_OUTPUT.write_text("\n".join(phones), encoding="utf-8")

print("Files saved successfully:")
print(f" - {EMAIL_OUTPUT}")
print(f" - {PHONE_OUTPUT}")