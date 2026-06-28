import os
import google.generativeai as genai
from dotenv import load_dotenv

class MockInterviewGenerator:
    def __init__(self):
        load_dotenv(os.path.join('utils', '.env'))
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
        if self.google_api_key:
            genai.configure(api_key=self.google_api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')

    def generate_questions(self, resume_text, role='General'):
        if not self.google_api_key:
            return 'Error: GOOGLE_API_KEY is not configured.'
            
        prompt = f"""
        Act as an expert technical recruiter and hiring manager.
        Based on the following resume text and the target role '{role}', generate a list of 10 targeted interview questions.
        Include a mix of:
        1. 4 Technical questions based on the specific skills mentioned in the resume.
        2. 3 Behavioral/Situational questions (STAR method).
        3. 3 Role-specific questions based on the candidate's past experience.
        
        For each question, also provide a brief 'What the interviewer is looking for' tip.
        Format the output nicely using Markdown.
        
        Resume Text:
        {resume_text}
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f'An error occurred while generating interview questions: {str(e)}'
