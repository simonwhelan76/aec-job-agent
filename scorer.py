def score_job(job):

    score = 0

    title = job["title"].lower()

    if "product" in title:
        score += 30

    if "strategy" in title:
        score += 30

    if "principal" in title:
        score += 15

    if "director" in title:
        score += 20

    if "sustainability" in title:
        score += 25

    if "engineering" in title:
        score -= 10

    return score