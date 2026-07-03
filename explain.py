def explain_job(job):

    title = job["title"].lower()

    reasons = []

    if "product" in title:
        reasons.append("Product leadership")

    if "strategy" in title:
        reasons.append("Strategy focus")

    if "principal" in title:
        reasons.append("Seniority match")

    if "director" in title:
        reasons.append("Leadership role")

    return ", ".join(reasons)