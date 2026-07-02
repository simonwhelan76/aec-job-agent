from filters import passes_filter

jobs = [
    {
        "title": "Director, Product Strategy",
        "company": "Autodesk"
    },
    {
        "title": "Software Engineer",
        "company": "Bentley"
    },
    {
        "title": "Senior Sustainability Manager",
        "company": "Trimble"
    }
]

matching_jobs = []

for job in jobs:
    if passes_filter(job["title"]):
        matching_jobs.append(job)

print("Jobs found:")

for job in matching_jobs:
    print(f"- {job['title']} ({job['company']})")
