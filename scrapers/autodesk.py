from playwright.sync_api import sync_playwright


def get_jobs():

    jobs = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            "https://autodesk.wd1.myworkdayjobs.com/Ext",
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(10000)

        content = page.content()

        print("AUTODESK PAGE LOADED")
        print("PAGE LENGTH:", len(content))

        browser.close()

    return jobs