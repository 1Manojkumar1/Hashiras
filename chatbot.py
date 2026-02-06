"""Chatbot module for curriculum assistance using OpenRouter API."""
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = """You are CurrBot, an expert curriculum assistant for CurrHub - an AI-powered curriculum generation platform.

IMPORTANT RULES:
1. NEVER say "I don't have" or "I don't have specific information"
2. NEVER say "please refer to" or "check the university website"
3. NEVER add disclaimers about not having data
4. ALWAYS provide helpful, detailed curriculum information confidently
5. If asked about a curriculum, provide a comprehensive typical structure

Your expertise:
- Curriculum design and course structures for all programs
- B.Tech, M.Tech, BCA, MCA, MBA, and other programs
- Indian university curriculum patterns (JNTU, OU, AICTE standards)
- Semester-wise subject breakdowns
- Electives, labs, and project requirements

When asked about curriculum:
- Provide semester-wise breakdown
- List core subjects and electives
- Include credits/hours if relevant
- Be specific and detailed

Available in our database: B.Tech (AI, Data Science, Cybersecurity), MBA (Marketing, Finance).
For other programs, provide typical curriculum structure based on standard patterns.

Keep responses clear and structured. Use bullet points for lists."""


def get_chat_response(user_message: str, conversation_history: list = None) -> str:
    """Generate a chat response using OpenRouter API."""
    
    # Check if API key is set
    if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == "your_openrouter_api_key_here":
        return "⚠️ Please set your OPENROUTER_API_KEY in the .env file. Get one free at openrouter.ai"
    
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "CurrHub"
        }
        
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
        
        payload = {
            "model": "openai/gpt-4o-mini",
            "messages": messages,
            "max_tokens": 500,
            "temperature": 0.7
        }
        
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        elif response.status_code == 402:
            return "⚠️ No credits. Add credits at openrouter.ai/credits"
        else:
            return f"⚠️ API error {response.status_code}"
            
    except requests.exceptions.Timeout:
        return "Response timed out. Please try again."
    except Exception as e:
        return f"Error: {str(e)[:100]}"
