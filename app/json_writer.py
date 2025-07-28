import json

def write_json_output(title, outline, output_path):
    """
    Writes the final structured JSON output for the PDF.
    """
    result = {
        "title": title,
        "outline": outline
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"📄 Output written to: {output_path}")
