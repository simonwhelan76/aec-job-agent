import requests
from bs4 import BeautifulSoup


def get_jobs():

    url = "https://careers.procore.com/jobs/search"

    response = requests.get(url)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    jobs = []

    include = [
        "director",
        "senior director",
        "head",
        "vp",
        "vice president",
        "principal product",
        "product manager",
        "product strategy",
        "strategy",
        "sustainability"
    ]

    exclude = [
    "designer",
    "engineering manager",
    "engineer",
    "developer",
    "marketing",
    "support",
    "recruiter",
    "analyst",
    "tax",
    "account",
    "account management",
    "sales",
    "investor",
    "finance"
    ]

    for link in soup.find_all("a"):

        title = link.get_text(strip=True)

        if len(title) < 10:
            continue

        if "meet our teams" in title.lower():
            continue

        href = link.get("href")

        if not href:
            continue

        title_lower = title.lower()

        if not any(word in title_lower for word in include):
            continue

        if any(word in title_lower for word in exclude):
            continue

        jobs.append({
            "company": "Procore",
            "title": title,
            "url": href
        })

    return jobs