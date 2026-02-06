"""Gap analyzer module using OpenRouter API."""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GAP_API_KEY = os.getenv("GAP_API_KEY") or os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

GAP_PROMPT = """You are an expert career advisor analyzing the gap between academic curricula and industry job requirements.

Analyze the provided curriculum against the job description and provide:

## Gap Analysis Report

### Job Requirements Summary
[Brief summary of key requirements from the job description]

### Skills Coverage Analysis

#### ✅ Well-Covered Skills
- [Skill 1]: [Which course covers it]
- [Skill 2]: [Which course covers it]

#### ⚠️ Partially Covered Skills
- [Skill 1]: [Current coverage level and what's missing]
- [Skill 2]: [Current coverage level and what's missing]

#### ❌ Missing Skills/Topics
- [Skill 1]: [Why it's important for this role]
- [Skill 2]: [Why it's important for this role]

### Recommended Additions
1. [Specific course or topic to add]
2. [Specific course or topic to add]
3. [Specific course or topic to add]

### Industry Readiness Score
[X/10] - [Brief justification]

### Action Items for Students
1. [Certification/Course to pursue]
2. [Project idea related to the role]
3. [Additional skill to develop]

Be specific and actionable. Focus on practical recommendations."""


def analyze_gap(curriculum_summary: str, job_description: str) -> str:
    """Analyze gap between curriculum and job requirements."""
    
    if not GAP_API_KEY or GAP_API_KEY == "your_openrouter_api_key_here":
        return "⚠️ Please set GAP_API_KEY (or OPENROUTER_API_KEY) in your .env file."
    
    try:
        headers = {
            "Authorization": f"Bearer {GAP_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "CurrHub Gap Analyzer"
        }
        
        user_message = f"""Analyze the following:

CURRICULUM:
{curriculum_summary}

JOB DESCRIPTION:
{job_description}

Provide a detailed gap analysis."""
        
        messages = [
            {"role": "system", "content": GAP_PROMPT},
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
            return f"⚠️ API error {response.status_code}: Unable to analyze gap."
            
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except Exception as e:
        return f"Error: {str(e)[:100]}"
