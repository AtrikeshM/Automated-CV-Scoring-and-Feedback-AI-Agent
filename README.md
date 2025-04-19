**Project Name: Automated CV Scoring and Feedback AI Agent**

**Short Description:**
This project automates the entire process of collecting resumes, analyzing and scoring them using AI, and sending personalized feedback to candidates via email. It eliminates manual effort in resume screening and delivers instant, insightful feedback to applicants.

**Tech Stack:**
**Python 3.11**
**Pandas** – for data handling and score storage
**Scikit-learn / Spacy / Custom ML Models** – for resume parsing and scoring (as needed)
**Tkinter** – for GUI-based resume upload
**smtplib & email.message** – for sending emails
**Subprocess** – to trigger scripts programmatically
**OS / Shutil** – file handling
**PDF/DOCX Parsers (e.g. PyMuPDF, python-docx)** – for resume reading

**How to Run It:**
1. Install dependencies
2. resumes/ – where resumes will be uploaded and output/ – where the scores CSV will be saved
3. Run the **main.py** file to upload and trigger pipeline:
4. Make sure you have enabled App Passwords for Gmail

 **Features:**
GUI-based Resume Upload
Automated Pipeline: Resume → Score → Email
Intelligent CV Scoring
Personalized Email Feedback
Auto Cleanup of resumes post-email
Minimal Manual Effort, Fully Automated Workflow
Gmail App Password based secure email sending
