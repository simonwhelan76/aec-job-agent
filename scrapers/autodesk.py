from playwright.sync_api import sync_playwright


def get_jobs():

    jobs = []

    keywords = [
        "product manager",
        "director",
        "strategy",
        "product owner",
        "head",
        "vice president",
        "product management",
        "strategist"
    ]

    exclude = [
        "designer",
        "marketing",
        "talent acquisition",
        "recruiter",
        "developer",
        "engineer"
    ]

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            "https://autodesk.wd1.myworkdayjobs.com/Ext",
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(10000)

        links = page.locator("a")

        count = links.count()

        for i in range(count):

            try:

                title = links.nth(i).inner_text().strip()

                if not title:
                    continue

                title_lower = title.lower()

                if any(word in title_lower for word in exclude):
                    continue

                if any(word in title_lower for word in keywords):

                    href = links.nth(i).get_attribute("href")

                    if href and href.startswith("/"):
                        href = "https://autodesk.wd1.myworkdayjobs.com" + href

                    jobs.append({
                        "company": "Autodesk",
                        "title": title,
                        "url": href
                    })

            except:
                pass

        browser.close()

    return jobs