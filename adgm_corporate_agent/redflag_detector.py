import re

ALLOWED_JURISDICTIONS = ["adgm", "abu dhabi courts", "abu dhabi global market"]

def detect_issues(doc_name, text):
    issues = []
    text_lower = text.lower()
    jurisdiction_found = any(jurisdiction in text_lower for jurisdiction in ALLOWED_JURISDICTIONS)

    clause_matches = re.findall(r"(Clause\s+[\d\.]+)\s*:\s*(.*jurisdiction.*)", text, re.IGNORECASE)
    jurisdiction_section = clause_matches[0][0] if clause_matches else "Jurisdiction Clause"

    if not jurisdiction_found:
        suggestion = "Update jurisdiction to ADGM Courts."
        if doc_name == "Board Resolutions":
            suggestion = "Ensure board resolutions reflect ADGM jurisdiction."
        elif doc_name == "Memorandum of Association":
            suggestion = "Update jurisdiction in MoA to ADGM Courts."

        issues.append({
            "document": doc_name,
            "section": jurisdiction_section,
            "issue": "Jurisdiction clause does not specify ADGM",
            "severity": "High",
            "suggestion": suggestion
        })

    if "signature" not in text_lower:
        issues.append({
            "document": doc_name,
            "section": "End",
            "issue": "Missing signature section",
            "severity": "Medium",
            "suggestion": "Add signature and date."
        })
    return issues
