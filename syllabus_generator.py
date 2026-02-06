"""Syllabus generator module using OpenRouter API."""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

SYLLABUS_API_KEY = os.getenv("SYLLABUS_API_KEY") or os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

SYLLABUS_PROMPT = """You are an expert academic curriculum designer. Generate a detailed syllabus for the given course.

Output format (use exact structure):
## Course: [Course Name]
### Course Overview
[2-3 sentence description]

### Learning Outcomes
1. [LO1]
2. [LO2]
3. [LO3]
4. [LO4]

### Unit-wise Breakdown

#### Unit 1: [Topic]
- [Subtopic 1]
- [Subtopic 2]
- [Subtopic 3]
Hours: [X]

#### Unit 2: [Topic]
- [Subtopic 1]
- [Subtopic 2]
- [Subtopic 3]
Hours: [X]

#### Unit 3: [Topic]
- [Subtopic 1]
- [Subtopic 2]
- [Subtopic 3]
Hours: [X]

#### Unit 4: [Topic]
- [Subtopic 1]
- [Subtopic 2]
- [Subtopic 3]
Hours: [X]

#### Unit 5: [Topic]
- [Subtopic 1]
- [Subtopic 2]
- [Subtopic 3]
Hours: [X]

### Reference Books
1. [Book 1]
2. [Book 2]
3. [Book 3]

### Assessment Pattern
- Internal: 40%
- External: 60%

Be specific and detailed. Use actual topics relevant to the course."""


def generate_syllabus(course_name: str, program: str, domain: str) -> str:
    """Generate detailed syllabus for a course."""
    
    if not SYLLABUS_API_KEY or SYLLABUS_API_KEY == "your_openrouter_api_key_here":
        return "⚠️ Please set SYLLABUS_API_KEY (or OPENROUTER_API_KEY) in your .env file."
    
    try:
        headers = {
            "Authorization": f"Bearer {SYLLABUS_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "CurrHub Syllabus"
        }
        
        user_message = f"Generate a detailed syllabus for the course: {course_name}\nProgram: {program}\nDomain: {domain}"
        
        messages = [
            {"role": "system", "content": SYLLABUS_PROMPT},
            {"role": "user", "content": user_message}
        ]
        
        payload = {
            "model": "openai/gpt-4o-mini",
            "messages": messages,
            "max_tokens": 1500,
            "temperature": 0.7
        }
        
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        else:
            return f"⚠️ API error {response.status_code}: Unable to generate syllabus."
            
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except Exception as e:
        return f"Error: {str(e)[:100]}"
