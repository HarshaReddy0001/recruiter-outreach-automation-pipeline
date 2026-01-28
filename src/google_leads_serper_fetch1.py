import re, time, json
from pathlib import Path
from urllib.parse import urlparse

import requests
import trafilatura

SERPER_API_KEY = "YOUR serper.dev API key"

QUERIES = [
    '"send resume to" "data scientist" USA',
    '"email your resume" "data scientist" USA',
    '"data scientist" staffing agency email USA',
    '"data scientist" recruitment agency email USA',
    '"data scientist" consulting email USA',
    '"data scientist" "send your resume to" USA',
    '"data scientist" "resume to" email USA',
    '"data scientist" recruiter email USA',
]

NUM_RESULTS_PER_QUERY = 20
SERPER_DELAY = 2.0

FETCH_DELAY = 1.0
FETCH_TIMEOUT = 20
MAX_LINKS_TOTAL = 200  # cap to save time/credits

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output5"
OUTPUT_DIR.mkdir(exist_ok=True)

OUT_RESULTS = OUTPUT_DIR / "serper_results.json"
OUT_EMAILS = OUTPUT_DIR / "google_emails.txt"
OUT_PHONES = OUTPUT_DIR / "leads_phones.txt"
OUT_FETCH_LOG = OUTPUT_DIR / "fetch_log.json"

BLOCKED_EMAIL_DOMAINS = {
    "gmail.com","yahoo.com","outlook.com","hotmail.com","icloud.com",
    "aol.com","protonmail.com","live.com","msn.com"
}

SKIP_DOMAINS = {
    "linkedin.com","www.linkedin.com",
    "indeed.com","www.indeed.com",
    "glassdoor.com","www.glassdoor.com",
    "ziprecruiter.com","www.ziprecruiter.com",
    "monster.com","www.monster.com",
    "theladders.com","www.theladders.com",
    "dice.com","www.dice.com",
    "careerbuilder.com","www.careerbuilder.com",
    "simplyhired.com","www.simplyhired.com",
    "quora.com","www.quora.com",
}

SKIP_URL_SUBSTRINGS = [
    "myworkdayjobs", "workday", "greenhouse.io", "lever.co",
    "icims", "successfactors", "smartrecruiters", "dayforce"
]

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PHONE_RE = re.compile(r"(\+1[\s-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

def normalize_obfuscated(text: str) -> str:
    text = re.sub(r"\s*\[at\]\s*|\s*\(at\)\s*|\s+at\s+", "@", text, flags=re.I)
    text = re.sub(r"\s*\[dot\]\s*|\s*\(dot\)\s*|\s+dot\s+", ".", text, flags=re.I)
    return text

def is_allowed_email(email: str) -> bool:
    domain = email.split("@")[-1].lower().strip()
    return domain not in BLOCKED_EMAIL_DOMAINS

def should_skip_link(link: str) -> bool:
    if not link:
        return True
    u = link.lower()
    netloc = urlparse(link).netloc.lower()
    if netloc in SKIP_DOMAINS or any(netloc.endswith(d) for d in SKIP_DOMAINS):
        return True
    if any(s in u for s in SKIP_URL_SUBSTRINGS):
        return True
    return False

def serper_search(query: str, n: int):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}
    payload = {"q": query, "num": n}
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    if r.status_code != 200:
        print("SERPER ERROR:", r.status_code, r.text)
        raise SystemExit(1)
    return r.json()

def extract_contacts(text: str, emails: set, phones: set):
    if not text:
        return
    text = normalize_obfuscated(text)
    for e in EMAIL_RE.findall(text):
        if is_allowed_email(e):
            emails.add(e.lower())
    for m in PHONE_RE.finditer(text):
        phones.add(m.group(0).strip())

def fetch_page_text(url: str) -> str:
    downloaded = trafilatura.fetch_url(url, timeout=FETCH_TIMEOUT)
    if not downloaded:
        return ""
    return trafilatura.extract(downloaded) or ""

def main():
    if "PASTE_YOUR_SERPER_KEY_HERE" in SERPER_API_KEY:
        raise ValueError("Add your Serper key first.")

    emails, phones = set(), set()
    all_rows = []
    links = []

    # 1) Serper
    for i, q in enumerate(QUERIES, 1):
        print(f"[{i}/{len(QUERIES)}] {q}")
        data = serper_search(q, NUM_RESULTS_PER_QUERY)

        for item in data.get("organic", []):
            title = item.get("title","") or ""
            snippet = item.get("snippet","") or ""
            link = item.get("link","") or ""

            all_rows.append({"query": q, "title": title, "snippet": snippet, "link": link})

            # Extract from snippet/title (free)
            extract_contacts(f"{title}\n{snippet}\n{link}", emails, phones)

            if link and not should_skip_link(link):
                links.append(link)

        time.sleep(SERPER_DELAY)

    OUT_RESULTS.write_text(json.dumps(all_rows, indent=2), encoding="utf-8")

    # 2) Fetch each result page once (big yield)
    links = list(dict.fromkeys(links))[:MAX_LINKS_TOTAL]  # dedupe preserve order
    print(f"\nLinks to fetch (1 page each): {len(links)}")

    fetch_log = []
    for idx, url in enumerate(links, 1):
        try:
            txt = fetch_page_text(url)
            before_e, before_p = len(emails), len(phones)
            extract_contacts(txt, emails, phones)

            fetch_log.append({
                "url": url,
                "status": "OK" if txt else "NO_TEXT",
                "chars": len(txt),
                "new_emails": len(emails) - before_e,
                "new_phones": len(phones) - before_p,
            })
        except Exception as e:
            fetch_log.append({"url": url, "status": "ERROR", "error": str(e)})

        if idx % 10 == 0:
            print(f"Fetched {idx}/{len(links)} | emails={len(emails)} phones={len(phones)}")
        time.sleep(FETCH_DELAY)

    OUT_FETCH_LOG.write_text(json.dumps(fetch_log, indent=2), encoding="utf-8")

    OUT_EMAILS.write_text("\n".join(sorted(emails)) + ("\n" if emails else ""), encoding="utf-8")
    OUT_PHONES.write_text("\n".join(sorted(phones)) + ("\n" if phones else ""), encoding="utf-8")

    print("\n--- DONE ---")
    print("Emails:", len(emails))
    print("Phones:", len(phones))
    print("Saved:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
