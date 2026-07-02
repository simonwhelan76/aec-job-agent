import requests
from bs4 import BeautifulSoup


def get_jobs():

    url = "https://autodesk.wd1.myworkdayjobs.com/en-US/Ext"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    keywords = [
        "director",
        "senior director",
        "manager",
        "senior manager",
        "product",
        "strategy",
        "sustainability",
        "head"
    ]

    for link in soup.find_all("a"):

        title = link.get_text(strip=True)

        href = link.get("href")

        if not title or not href:
            continue

        title_lower = title.lower()

        if any(word in title_lower for word in keywords):

            jobs.append({
                "company": "Autodesk",
                "title": title,
                "url": href
            })

    return jobs