import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

df = pd.read_csv('output/resume_scores.csv')

def send_feedback_email(to_email, name, score, education_score, experience_score, ai_score, tech_score, feedback):
    from_email = "atrikeshmishra2002@gmail.com"
    password = "vhic ibak ojgd irxn" 
    msg = MIMEMultipart()
    msg['From'] = "Atrikesh Mishra"
    msg['To'] = to_email
    msg['Subject'] = "CV Feedback - ElintAI"

    body = f"""
    Dear {name},

    Thank you for submitting your resume. After reviewing it, here’s the detailed feedback:

    CV Score: {score}/100

    Component-wise Breakdown:
    - Education: {education_score}/20
    - Experience: {experience_score}/20
    - AI Skill: {ai_score}/30
    - Tech Skill: {tech_score}/30

    Personalized Comment:
    {feedback}

    Best regards,
    Atrikesh Mishra
    """

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def send_feedback_to_all(df):
    for index, row in df.iterrows():
        send_feedback_email(
            row['original_email'],
            row['original_name'],
            row['CV Score'],
            row['Education Score'],
            row['Experience Score'],
            row['AI Skill Score'],
            row['Tech Skill Score'],
            row['Feedback']
        )

def delete_uploaded_resumes(folder_path="resumes"):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print(" All resumes deleted after sending emails.")
    except Exception as e:
        print(f" Failed to delete resumes: {e}")


send_feedback_to_all(df)
delete_uploaded_resumes()