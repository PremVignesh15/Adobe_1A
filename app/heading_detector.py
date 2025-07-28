def detect_heading_candidates(pages_data):
    """
    Detects valid heading candidates by filtering out bullets, long lines, and small font.
    """
    heading_candidates = []

    for page in pages_data:
        for item in page["items"]:
            text = item["text"]
            font_size = item["font_size"]
            x, y = item["position"]
            page_num = item["page_num"]

            # 🚫 Skip bullet points (like '•') or lines starting with bullets
            if text.strip().startswith("•") or text.strip() == "•":
                continue

            # 🚫 Skip too long (probably paragraph)
            if len(text) > 100:
                continue

            # 🚫 Skip short lowercase-only lines
            if len(text) < 3:
                continue

            heading_candidates.append({
                "text": text.strip(),
                "font_size": font_size,
                "position": (x, y),
                "page_num": page_num
            })

    return heading_candidates
