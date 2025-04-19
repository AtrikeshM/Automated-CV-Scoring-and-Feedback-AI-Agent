import pandas as pd

# Define keywords for scoring
ai_keywords = ['machine learning', 'deep learning', 'artificial intelligence', 'neural networks', 'NLP', 'computer vision']
programming_keywords = ['python', 'c++', 'java', 'sql', 'tensorflow', 'pandas', 'numpy']

def keyword_score(text, keywords):
    """Score based on keyword matches"""
    if pd.isna(text):
        return 0
    text = text.lower()
    matches = sum(1 for word in keywords if word in text)
    return min(matches * 10, 30)

def score_resume(row):
    education_score = 20 if 'b.tech' in str(row['text']).lower() or 'bachelor' in str(row['text']).lower() else 10
    experience_score = 20 if 'experience' in str(row['text']).lower() else 10

    ai_score = keyword_score(row['text'], ai_keywords)
    tech_score = keyword_score(row['text'], programming_keywords)

    total_score = education_score + experience_score + ai_score + tech_score
    feedback = []

    if education_score < 15:
        feedback.append("Consider improving education section.")
    if ai_score < 10:
        feedback.append("Add more AI-related keywords or projects.")
    if tech_score < 10:
        feedback.append("Add more technical skills.")

    return pd.Series({
        'total_score': total_score, 
        'CV Score': total_score,     
        'Education Score': education_score,
        'Experience Score': experience_score,
        'AI Skill Score': ai_score,
        'Tech Skill Score': tech_score,
        'Feedback': '; '.join(feedback)
    })


def main():
    df = pd.read_csv('output/resume_data.csv')
    scored_df = df.join(df.apply(score_resume, axis=1))
    scored_df.to_csv('output/resume_scores.csv', index=False)
    print(" Resume scoring completed. Data saved to: output/resume_scores.csv")

if __name__ == "__main__":
    main()

