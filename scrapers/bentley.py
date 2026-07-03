from playwright.sync_api import sync_playwright


def get_jobs():

    jobs = []

    keywords = [
        "product manager",
        "director",
        "vice president",
        "head",
        "strategy",
        "manager"
    ]

    exclude = [
        "engineer",
        "developer",
        "government relations",
        "hr",
        "analyst",
        "sales representative",
        "product design"
    ]

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            "https://jobs.bentley.com/search/",
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(10000)

        links = page.locator("a")

        count = links.count()

        for i in range(count):

            try:

                title = links.nth(i).inner_text().strip()

                href = links.nth(i).get_attribute("href")

                if not title:
                    continue

                title_lower = title.lower()

                if any(word in title_lower for word in exclude):
                    continue

                if any(word in title_lower for word in keywords):

                    if href and href.startswith("/"):

                        href = "https://jobs.bentley.com" + href

                    jobs.append({
                        "company": "Bentley",
                        "title": title,
                        "url": href
                    })

            except:
                pass

        browser.close()

    return jobs