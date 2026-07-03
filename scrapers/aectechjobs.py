from playwright.sync_api import sync_playwright


def get_jobs():

    jobs = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            "https://aectechjobs.com/search",
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(5000)

        links = page.locator("a")

        count = links.count()

        for i in range(count):

            try:

                title = links.nth(i).inner_text().strip()

                href = links.nth(i).get_attribute("href")

                if not title:
                    continue

                title_lower = title.lower()

                exclude = [
                    "designer",
                    "design lead",
                    "ux",
                    "ui",
                    "marketing",
                    "sales",
                    "recruiter",
                    "finance",
                    "investor"
                ]

                if any(word in title_lower for word in exclude):
                    continue

                keywords = [
                    "director",
                    "principal",
                    "product",
                    "strategy",
                    "sustainability",
                    "head"
                ]

                if any(k in title_lower for k in keywords):

                    jobs.append({
                        "company": "AEC Tech Jobs",
                        "title": title,
                        "url": href
                    })

            except:
                pass

        browser.close()

    return jobs