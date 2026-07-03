def score_job(job):

    score = 0

    title = job["title"].lower()

    if "product" in title:
        score += 20

    if "product manager" in title:
        score += 30

    if "principal" in title:
        score += 25

    if "director" in title:
        score += 30

    if "strategy" in title:
        score += 30

    if "sustainability" in title:
        score += 30

    if "head" in title:
        score += 20

    if "aec" in title:
        score += 40

    if "engineering" in title:
        score -= 15

    if "investor" in title:
        score -= 50

    if "designer" in title:
        score -= 50

    return score