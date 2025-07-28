def classify_headings(heading_candidates):
    """
    Classifies heading candidates into H1, H2, H3 based on font size.
    Skips garbage lines and uses size ranking.
    """
    if not heading_candidates:
        return "", []

    # Get unique font sizes ranked from largest to smallest
    font_sizes = sorted({round(h["font_size"], 1) for h in heading_candidates}, reverse=True)

    font_to_level = {}
    if len(font_sizes) > 0:
        font_to_level[font_sizes[0]] = "H1"
    if len(font_sizes) > 1:
        font_to_level[font_sizes[1]] = "H2"
    if len(font_sizes) > 2:
        font_to_level[font_sizes[2]] = "H3"

    outline = []
    title = ""

    for heading in heading_candidates:
        font_size = round(heading["font_size"], 1)
        level = font_to_level.get(font_size)

        if level:
            text = heading["text"]

            # ❌ Ignore bullet points just in case (extra safety)
            if text.strip().startswith("•") or text.strip() == "•":
                continue

            # ✅ Add to outline
            entry = {
                "level": level,
                "text": text,
                "page": heading["page_num"]
            }
            outline.append(entry)

            # Use first H1 as title
            if level == "H1" and not title:
                title = text

    return title, outline
