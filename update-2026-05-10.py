# -*- coding: utf-8 -*-
import json
import urllib.request
import re
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            html = resp.read(50000).decode('utf-8', errors='ignore')
            match = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html)
            if not match:
                match = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html)
            return match.group(1) if match else ""
    except:
        return ""

# Load new issues from companion JSON
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "new-issues-2026-05-10.json"), "r", encoding="utf-8") as f:
    new_issues = json.load(f)

# Fetch og:images and update
for issue in new_issues:
    for src in issue.get("sources", []):
        img = get_og_image(src["url"])
        src["image"] = img
        print(f"  {src['url'][:60]}... -> {img[:80] if img else '(none)'}")
    # Set cover to first source image
    first_img = next((s["image"] for s in issue["sources"] if s.get("image")), "")
    issue["cover"] = first_img

# Read existing issues
issues_path = os.path.join(script_dir, "issues.json")
with open(issues_path, "r", encoding="utf-8") as f:
    raw = f.read()
issues = json.loads(raw)

# Remove existing 2026-05-10
issues = [i for i in issues if i.get("date") != "2026-05-10"]
issues = new_issues + issues

with open(issues_path, "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\nDone! Total issues: {len(issues)}")
