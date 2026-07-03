def score_job(job):

    score = 0

    title = job["title"].lower()

    # Autodesk ecosystem

    if "forma" in title:
        score += 120

    if "revit" in title:
        score += 100

    # Product leadership

    if "principal product manager" in title:
        score += 80

    elif "product manager" in title:
        score += 50

    if "product owner" in title:
        score += 40

    if "product management" in title:
        score += 50

    # Strategy

    if "strategist" in title:
        score += 50

    if "strategy" in title:
        score += 50

    # Leadership

    if "vice president" in title:
        score += 60

    if "director" in title:
        score += 50

    if "head" in title:
        score += 40

    # Sustainability

    if "sustainability" in title:
        score += 30

    # Penalties

    if "designer" in title:
        score -= 50

    if "investor" in title:
        score -= 100

    if "engineering" in title:
        score -= 20

    if "software" in title:
        score -= 20

    if "developer" in title:
        score -= 30

    if "account manager" in title:
        score -= 50

    if "sales" in title:
        score -= 50

    return score