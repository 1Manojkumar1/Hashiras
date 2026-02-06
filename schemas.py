from pydantic import BaseModel
from typing import List, Optional

# ===== INPUT MODEL (used when user submits form) =====
class CurriculumRequest(BaseModel):
    program_type: str
    domain: str
    academic_level: str
    duration_semesters: int
    accreditation_body: str
    industry_keywords: Optional[str] = ""

# ===== OUTPUT MODELS (used in AI response) =====
class LearningOutcome(BaseModel):
    outcome: str
    bloom_level: str
    code: Optional[str] = None

class WeeklyTopic(BaseModel):
    week: int
    title: str
    description: str
    resources: List[str]

class Course(BaseModel):
    course_code: str
    course_name: str
    category: str  # Core, Elective, Labs, etc.
    description: str
    credits: int = 3
    weekly_topics: List[WeeklyTopic]
    outcomes: List[LearningOutcome]
    prerequisites: List[str] = []

class CurriculumResponse(BaseModel):
    program_title: str
    program_type: str
    domain: str
    academic_level: str
    total_semesters: int
    program_rationale: str
    target_careers: List[str]
    accreditation_aligned: str
    courses_by_semester: dict  # e.g., {"Semester 1": [...]}
    recommended_skills: List[str]
    industry_alignment_notes: str
    optimization_tips: List[str]