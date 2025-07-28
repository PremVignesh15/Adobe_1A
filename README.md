# Adobe_1A
Adobe Hackathon 2025 – PDF Outline Extraction
Author: Prem Vignesh

Rounds Covered:
- Round 1A: Structured Outline from PDF using LLM

Round 1A: LLM-Based Approach
----------------------------
Goal:
Use a lightweight language model to extract a structured JSON outline from a PDF.
The outline must include:
- title
- Hierarchies like h1, h2, h3
- Order preserved as per reading flow

Approach:
- Convert PDF pages to text using PyMuPDF or pdfminer.six
- Split content into logical sections
- Use a multilingual BERT-based model (or lightweight LLM) with prompt-based parsing
- Extract structured tags like title, h1, etc.
- Merge and validate final JSON

Dependencies:
pip install transformers torch fitz

Sample Output:
{
  "title": "Document Title",
  "h1": [
    {
      "heading": "Main Section",
      "h2": [
        {
          "heading": "Subsection",
          "h3": ["Point A", "Point B"]
        }
      ]
    }
  ]
}
