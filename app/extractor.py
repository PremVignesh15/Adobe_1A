import fitz  # PyMuPDF

def extract_text_and_layout(pdf_path):
    """
    Extracts real text (not from images) from a PDF file.
    Returns a list of dictionaries per page (with page number starting from 0).
    """
    doc = fitz.open(pdf_path)
    pages_data = []

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        blocks = page.get_text("dict")["blocks"]

        page_items = []

        for block in blocks:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                line_text = ""
                font_sizes = []
                positions = []

                for span in line["spans"]:
                    text = span["text"].strip()
                    font_size = span["size"]
                    x0, y0, x1, y1 = span["bbox"]

                    # ⛔ Skip empty or whitespace
                    if not text:
                        continue

                    # ⛔ Skip if span has image-like origin
                    if span.get("origin", 0) == 1:
                        continue

                    # ⛔ Optional: Skip small font (probably not headings)
                    if font_size < 9:
                        continue

                    # ⛔ Optional: Skip text very close to top/bottom (footer/header/banners)
                    if y0 < 50 or y0 > 750:
                        continue

                    line_text += text + " "
                    font_sizes.append(font_size)
                    positions.append((x0, y0))

                if line_text.strip():
                    avg_font_size = sum(font_sizes) / len(font_sizes)
                    x, y = positions[0] if positions else (0, 0)

                    page_items.append({
                        "text": line_text.strip(),
                        "font_size": avg_font_size,
                        "position": (x, y),
                        "page_num": page_index  # ✅ start from 0
                    })

        pages_data.append({
            "page_number": page_index,  # ✅ start from 0
            "items": page_items
        })

    return pages_data
