import asyncio
from ai_engine import generate_curriculum_with_gemini

test_data = {
    "program_type": "B.Tech",
    "domain": "Quantum Computing",
    "academic_level": "Undergraduate",
    "duration_semesters": 2,
    "accreditation_body": "ABET"
}

print("Starting AI Curriculum Generation Test...")
result = generate_curriculum_with_gemini(test_data)

if "[Demo]" in result.get("program_title", ""):
    print("FAILED: Still getting fallback data.")
else:
    print("SUCCESS: Received AI-generated content!")
    print(f"Title: {result.get('program_title')}")
    print(f"Rationale: {result.get('program_rationale', '')[:100]}...")
