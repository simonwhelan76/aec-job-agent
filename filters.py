def passes_filter(title):

    title = title.lower()

    wanted = [
        "director",
        "senior director",
        "manager",
        "senior manager",
        "head",
        "product",
        "strategy",
        "sustainability"
    ]

    return any(word in title for word in wanted)
