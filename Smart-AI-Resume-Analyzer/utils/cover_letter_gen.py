import os
import google.generativeai as genai
from dotenv import load_dotenv

class CoverLetterGenerator:
    def __init__(self):
        load_dotenv(os.path.join('utils', '.env'))
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
        if self.google_api_key:
            genai.configure(api_key=self.google_api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')

    def generate(self, resume_text, job_description):
        if not self.google_api_key:
            return 'Error: GOOGLE_API_KEY is not configured.'
        
        prompt = f"""
        Act as an expert career coach and professional copywriter.
        Based on the following resume text and job description, write a compelling, professional, and tailored cover letter.
        The cover letter should highlight the candidate's most relevant skills and experiences from the resume that match the job description.
        Make it sound natural, confident, and engaging.
        
        Resume Text:
        {resume_text}
        
        Job Description:
        {job_description}
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f'An error occurred while generating the cover letter: {str(e)}'
