"""Resource Hub module for curating learning resources using OpenRouter API."""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

RESOURCE_API_KEY = os.getenv("RESOURCE_API_KEY") or os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

RESOURCE_PROMPT = """You are an expert educational resource curator. For the given course, provide curated learning resources.

Output EXACTLY in this JSON format (no extra text):
{
  "moocs": [
    {"title": "Course Title", "platform": "Coursera/edX/NPTEL/Udemy", "url": "https://...", "instructor": "Name"},
    {"title": "Course Title", "platform": "Platform", "url": "https://...", "instructor": "Name"},
    {"title": "Course Title", "platform": "Platform", "url": "https://...", "instructor": "Name"}
  ],
  "books": [
    {"title": "Book Title", "author": "Author Name", "edition": "Xth Edition, Year", "isbn": "ISBN-XX"},
    {"title": "Book Title", "author": "Author Name", "edition": "Xth Edition, Year", "isbn": "ISBN-XX"},
    {"title": "Book Title", "author": "Author Name", "edition": "Xth Edition, Year", "isbn": "ISBN-XX"}
  ],
  "youtube": [
    {"title": "Playlist/Channel Name", "creator": "Creator Name", "url": "https://youtube.com/...", "videos": "XX videos"},
    {"title": "Playlist/Channel Name", "creator": "Creator Name", "url": "https://youtube.com/...", "videos": "XX videos"},
    {"title": "Playlist/Channel Name", "creator": "Creator Name", "url": "https://youtube.com/...", "videos": "XX videos"}
  ]
}

Provide REAL, EXISTING resources with accurate URLs. Focus on highly-rated, popular resources."""


def get_course_resources(course_name: str, domain: str = "") -> dict:
    """Get curated learning resources for a course."""
    
    if not RESOURCE_API_KEY or RESOURCE_API_KEY == "your_openrouter_api_key_here":
        return {
            "error": "Please set RESOURCE_API_KEY in your .env file.",
            "moocs": [], "books": [], "youtube": []
        }
    
    try:
        headers = {
            "Authorization": f"Bearer {RESOURCE_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "CurrHub Resources"
        }
        
        user_message = f"Provide learning resources for the course: {course_name}"
        if domain:
            user_message += f" (Domain: {domain})"
        
        messages = [
            {"role": "system", "content": RESOURCE_PROMPT},
            {"role": "user", "content": user_message}
        ]
        
        payload = {
            "model": "openai/gpt-4o-mini",
            "messages": messages,
            "max_tokens": 1200,
            "temperature": 0.7
        }
        
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            content = data["choices"][0]["message"]["content"].strip()
            
            # Parse JSON from response
            import json
            # Handle potential markdown code blocks
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            return json.loads(content)
        else:
            return {
                "error": f"API error {response.status_code}",
                "moocs": [], "books": [], "youtube": []
            }
            
    except Exception as e:
        return {
            "error": str(e)[:100],
            "moocs": [], "books": [], "youtube": []
        }
