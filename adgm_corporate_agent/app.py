import streamlit as st
from document_parser import extract_text, classify_document
from checklist import detect_process, check_missing_documents, get_required_documents
from redflag_detector import detect_issues
from annotator import annotate_docx
import json
import os
import re

st.title("ADGM Corporate Agent")

def sanitize_filename(name):
    # Replace spaces and special chars with underscore, safe for filenames
    return re.sub(r'[^A-Za-z0-9_-]', '_', name)

uploaded_files = st.file_uploader("Upload .docx files", type="docx", accept_multiple_files=True)

if uploaded_files:
    doc_texts = []
    doc_names = []
    all_issues = []

    for file in uploaded_files:
        text = extract_text(file)
        doc_type = classify_document(text)
        doc_texts.append(text)
        doc_names.append(doc_type)
        issues = detect_issues(doc_type, text)
        all_issues.extend(issues)

    process = detect_process(doc_texts)
    required_docs = get_required_documents(process)
    missing = check_missing_documents(process, doc_names)

    uploaded_required_docs = [doc for doc in doc_names if doc in required_docs]

    st.subheader("Checklist Results")
    st.write(f"Process: {process}")
    st.write(f"Uploaded: {len(uploaded_required_docs)} / Required: {len(required_docs)}")
    st.write(f"Missing: {missing}")

    st.subheader("Issues Found")
    st.json(all_issues)

    if st.button("Download Reviewed Docs"):
        os.makedirs("output", exist_ok=True)
        for file, doc_name in zip(uploaded_files, doc_names):
            issues_for_doc = [issue for issue in all_issues if issue["document"] == doc_name]
            safe_name = sanitize_filename(doc_name)
            out_path = f"output/reviewed_{safe_name}.docx"
            annotate_docx(file, issues_for_doc, out_path)
        st.success("Reviewed files saved in 'output' folder.")

    if st.button("Download JSON Report"):
        os.makedirs("output", exist_ok=True)
        report = {
            "process": process,
            "documents_uploaded": len(uploaded_required_docs),
            "required_documents": len(required_docs),
            "missing_document": missing,
            "issues_found": all_issues
        }
        with open("output/report.json", "w") as f:
            json.dump(report, f, indent=4)
        st.success("Report saved as output/report.json")
