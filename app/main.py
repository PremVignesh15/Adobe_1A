import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from extractor import extract_text_and_layout
from heading_detector import detect_heading_candidates
from heading_classifier import classify_headings
from json_writer import write_json_output




IN_DOCKER = os.environ.get("IN_DOCKER", "0") == "1"

if IN_DOCKER:
    INPUT_DIR = "/app/input"
    OUTPUT_DIR = "/app/output"
else:
    INPUT_DIR = os.path.join(os.getcwd(), "input")
    OUTPUT_DIR = os.path.join(os.getcwd(), "output")
def process_pdf(pdf_path, output_path):
    
    pages_data = extract_text_and_layout(pdf_path)

    
    heading_candidates = detect_heading_candidates(pages_data)

    
    title, structured_outline = classify_headings(heading_candidates)

    
    write_json_output(title, structured_outline, output_path)

def main():
    
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            json_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(OUTPUT_DIR, json_filename)

            print(f"🔍 Processing {filename}...")
            process_pdf(pdf_path, output_path)

    print("✅ All PDFs processed successfully!")

if __name__ == "__main__":
    main()
