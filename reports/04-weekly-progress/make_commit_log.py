#!/usr/bin/env python3
"""Build commit_log.csv and commits_per_day.csv from git history.
Run from the repository root:  python3 reports/04-weekly-progress/make_commit_log.py
"""
import csv, re, subprocess, collections, os

OUT = os.path.join("reports", "04-weekly-progress")
ROLE = {
    "bohra0022": "Backend upload, Redux part 1, reports",
    "choubisavishvas-web": "Branch Manager pages",
    "iamvkb7": "Cashier pages",
    "tanyasingh077": "Onboarding page",
    "subhash8729": "Repository and frontend folder setup",
    "Subhash Dhaka": "Repository and frontend folder setup",
}
AREA = {"pos-backend": "Backend", "pos-frontend-vite": "Frontend", "reports": "Reports"}

raw = subprocess.run(
    ["git", "log", "--reverse", "--date=short", "--name-only",
     "--format=%x1e%h%x1f%an%x1f%ad%x1f%s"],
    capture_output=True, text=True, check=True).stdout

rows, per_day = [], collections.Counter()
for rec in raw.split("\x1e")[1:]:
    head, *files = rec.strip("\n").split("\n")
    h, author, day, msg = head.split("\x1f", 3)
    files = [f for f in files if f.strip()]
    m = re.match(r"^\s*(\w+)(\([^)]*\))?:", msg)
    typ = "merge" if msg.startswith("Merge") else (m.group(1).lower() if m else "other")
    tops = collections.Counter(AREA.get(f.split("/")[0], "Docs") for f in files)
    area = tops.most_common(1)[0][0] if tops else ("Merge" if typ == "merge" else "Other")
    rows.append([h, day, author, ROLE.get(author, ""), msg.strip(), typ, area,
                 len(files), "; ".join(files[:3])])
    per_day[(day, author)] += 1

with open(os.path.join(OUT, "commit_log.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["No", "Commit hash", "Date", "Author", "Team role", "Commit message",
                "Type", "Area", "Files changed", "Example files"])
    for i, r in enumerate(rows, 1):
        w.writerow([i] + r)

with open(os.path.join(OUT, "commits_per_day.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["Date", "Author", "Commits"])
    for (day, author), n in sorted(per_day.items()):
        w.writerow([day, author, n])

print(f"{len(rows)} commits written to {OUT}/commit_log.csv")
for a, n in collections.Counter(r[2] for r in rows).most_common():
    print(f"  {n:3d}  {a}")
