import os
from scrapers.procore import get_jobs as get_procore_jobs
from scrapers.aectechjobs import get_jobs as get_aectech_jobs
from emailer import send_email
from scorer import score_job

from storage import (
    load_seen_jobs,
    save_seen_jobs
)

jobs = []

jobs.extend(get_procore_jobs())
jobs.extend(get_aectech_jobs())

seen_jobs = load_seen_jobs()

new_jobs = []

for job in jobs:

    job_id = (
        job["company"]
        + "|"
        + job["title"]
    )

    if job_id not in seen_jobs:

        new_jobs.append(job)

        seen_jobs.append(job_id)

save_seen_jobs(seen_jobs)

new_jobs.sort(
    key=score_job,
    reverse=True
)

print(f"Total jobs scraped: {len(jobs)}")
print(f"New jobs found: {len(new_jobs)}")

digest = f"""
AEC Leadership Job Digest

Found {len(new_jobs)} new jobs

"""

for job in new_jobs:

    score = score_job(job)

    digest += f"""
[{score}] {job['title']}

Company: {job['company']}

{job['url']}

----------------------------------------

"""

print(digest)

EMAIL = os.environ["GMAIL_USER"]

APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

EMAIL_TO = os.environ["EMAIL_TO"]

print(f"Found {len(new_jobs)} new jobs")

print("About to load email settings")

EMAIL = os.environ["GMAIL_USER"]
APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
EMAIL_TO = os.environ["EMAIL_TO"]

print("Email settings loaded")
print(f"Sending to: {EMAIL_TO}")

try:

    print("Attempting email send")

    send_email(
        EMAIL,
        APP_PASSWORD,
        EMAIL_TO,
        digest
    )

    print("EMAIL SENT SUCCESSFULLY")

except Exception as e:

    print("EMAIL FAILED")
    print(str(e))