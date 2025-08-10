# ADGM Corporate Agent
## Overview
An AI-powered assistant to help verify legal documents for Abu Dhabi Global Market (ADGM) compliance. It automatically detects the legal process, checks if all required documents are uploaded, finds issues in documents, and generates annotated documents and reports.

## Features:
- Automatic process detection (e.g., Company Formation & Governance)
-  Checklist verification for required documents
- Detection of issues like missing signatures or wrong jurisdiction clauses
- Annotated document generation highlighting issues
- JSON report generation summarizing uploaded documents and issues found
- User-friendly web interface using Streamlit

## Setup Instructions
### Requirements
-   Python 3.8 or higher
-   Windows, macOS, or Linux
### Installation Steps
1. Clone the repository
2. Create and activate a Python virtual environment.
3. Install dependencies
   pip install -r requirements.txt
4. Run the Streamlit app
    streamlit run app.py
5. Open the link provided by Streamlit in browser and start uploading your documents.

## Usage
1. Upload .docx legal documents via the file uploader.
2. The app will detect the process, verify document checklist, and find issues.
3. View results on the page.
4. Download annotated documents and a JSON report using the buttons.