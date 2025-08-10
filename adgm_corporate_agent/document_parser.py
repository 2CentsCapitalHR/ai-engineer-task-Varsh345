import docx

def extract_text(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def classify_document(text):
    text = text.lower()
    if "articles of association" in text:
        return "Articles of Association"
    elif "memorandum of association" in text or "memorandum" in text:
        return "Memorandum of Association"
    elif "board resolution" in text or "board resolutions" in text:
        return "Board Resolutions"
    elif "shareholder resolution" in text:
        return "Shareholder Resolution – Amendment of Articles"
    elif "register of members" in text or "registers" in text:
        return "Registers"
    elif "ubo" in text:
        return "UBO"
    else:
        return "Unknown"
