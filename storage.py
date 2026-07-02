import json

FILE_NAME = "jobs_seen.json"


def load_seen_jobs():

    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)

    except:

        return []


def save_seen_jobs(jobs):

    with open(FILE_NAME, "w") as f:

        json.dump(
            jobs,
            f,
            indent=2
        )