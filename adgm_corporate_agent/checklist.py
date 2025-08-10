import json
import os

DATA_FILE = os.path.join("knowledge_base", "adgm_document_sources.json")

def load_document_sources():
    """Load the full ADGM document data source JSON."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def detect_process(doc_texts):
    """Detect process based on combined text content."""
    text_combined = " ".join(doc_texts).lower()
    if "incorporation" in text_combined or "articles of association" in text_combined:
        return "Company Formation & Governance"
    elif "employment" in text_combined or "contract" in text_combined:
        return "Employment & HR"
    elif "data protection" in text_combined or "policy document" in text_combined:
        return "Data Protection"
    elif "annual accounts" in text_combined or "filings" in text_combined:
        return "Compliance & Filings"
    else:
        return "Unknown"

def get_required_documents(process):
    """Return list of required documents for given process category."""
    data = load_document_sources()
    if process == "Unknown":
        return []
    return [d["document_type"] for d in data if process.lower() in d["category"].lower()]

def check_missing_documents(process, uploaded_doc_names):
    """Return list of required documents that are missing from uploaded documents."""
    required = get_required_documents(process)
    missing = [doc for doc in required if doc not in uploaded_doc_names]
    return missing
