def score_job(job):

    score = 0

    title = job["title"].lower()

    if "principal product manager" in title:
        score += 80

    elif "product manager" in title:
        score += 50

    if "strategy" in title:
        score += 40

    if "director" in title:
        score += 40

    if "head" in title:
        score += 40

    if "sustainability" in title:
        score += 30

    if "aec" in title:
        score += 35

    if "engineering" in title:
        score -= 20

    if "designer" in title:
        score -= 50

    if "investor" in title:
        score -= 100

    return score