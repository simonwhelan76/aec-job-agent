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

digest = """
AEC Leadership Job Digest

NEW JOBS FOUND

"""

for job in new_jobs:

    score = score_job(job)

    digest += f"""
Score: {score}

Company: {job['company']}
Title: {job['title']}
Link: {job['url']}

----------------------------------------

"""

print(digest)

EMAIL = "swhelan.fpro@gmail.com"
APP_PASSWORD = "fgpfhxfbbpfvwzyo"

if new_jobs:

    send_email(
        EMAIL,
        APP_PASSWORD,
        EMAIL,
        digest
    )