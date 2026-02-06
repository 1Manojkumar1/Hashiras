import os
import json
import re
from typing import Dict, Any
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY in .env file!")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

def extract_json_from_response(text: str) -> dict:
    """
    Robustly extract valid JSON from LLM response.
    Handles plain JSON, markdown code blocks, and embedded JSON.
    """
    if not text or not text.strip():
        raise ValueError("Empty response")

    # Try direct parsing first
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass

    # Try to find JSON inside ```json ... ``` or ``` ... ```
    code_block_match = re.search(r"```(?:json)?\s*({.*?})\s*```", text, re.DOTALL | re.IGNORECASE)
    if code_block_match:
        try:
            return json.loads(code_block_match.group(1))
        except json.JSONDecodeError:
            pass

    # Try to find the outermost {...} object
    curly_match = re.search(r"({.*})", text, re.DOTALL)
    if curly_match:
        try:
            return json.loads(curly_match.group(1))
        except json.JSONDecodeError:
            pass

    raise ValueError("No valid JSON object found in response")

# ==========================================
# DATABASE-FIRST LOOKUP
# ==========================================
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "curriculum_database.json")

def load_curriculum_database() -> Dict[str, Any]:
    """Load the local curriculum database JSON file."""
    try:
        with open(DATABASE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Database load failed: {e}")
        return {}

def lookup_curriculum_in_database(data: Dict[str, Any]) -> Dict[str, Any] | None:
    """
    Check if a curriculum exists in the local database.
    Returns the curriculum dict if found, None otherwise.
    """
    db = load_curriculum_database()
    
    # Create lookup key: "program_type_domain"
    program_type = data.get("program_type", "")
    domain = data.get("domain", "")
    lookup_key = f"{program_type}_{domain}"
    
    if lookup_key in db:
        print(f"[DATABASE HIT] Found curriculum for: {lookup_key}")
        curriculum = db[lookup_key].copy()
        
        # Override with user-specified values
        curriculum["academic_level"] = data.get("academic_level", curriculum.get("academic_level"))
        curriculum["total_semesters"] = min(data.get("duration_semesters", 8), curriculum.get("total_semesters", 8))
        curriculum["accreditation_aligned"] = f"Aligned with {data.get('accreditation_body', 'Global')} Standards"
        
        return curriculum
    
    print(f"[DATABASE MISS] No match for: {lookup_key}, checking templates...")
    return None

def generate_curriculum_with_gemini(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a full curriculum. 
    Priority: 1) Local JSON Database → 2) Template Generator → 3) Gemini API → 4) Smart Fallback
    """
    # STEP 1: Check local JSON database first
    db_result = lookup_curriculum_in_database(data)
    if db_result:
        return db_result
    
    # STEP 2: Use template-based generator (covers ALL domain combinations)
    try:
        from curriculum_templates import generate_curriculum_from_template, DOMAIN_TEMPLATES
        domain = data.get("domain", "")
        if domain in DOMAIN_TEMPLATES:
            print(f"[TEMPLATE HIT] Generating from template for: {domain}")
            return generate_curriculum_from_template(data)
    except ImportError:
        print("[TEMPLATE MISS] Template module not found, proceeding to AI")
    
    # STEP 3: If not in templates, use Gemini API
    prompt = f"""
You are an Elite Academic Curriculum Architect and Industry Strategist. 
Generate a comprehensive, high-resolution academic program based on these parameters:

- Program Type: {data['program_type']}
- Domain: {data['domain']}
- Academic Level: {data['academic_level']}
- Intended Duration: {data['duration_semesters']} semesters
- Accreditation Standard: {data['accreditation_body']}

### ADVANCED REQUIREMENTS:
1. **Academic Rigor**: The curriculum must reflect state-of-the-art research and 2026-era industry standards. Use high-level academic terminology.
2. **Domain Specificity**: Ensure every course name, description, and topic is hyper-relevant to {data['domain']}. Avoid generic placeholders.
3. **Weekly Resolution**: Provide **6–8 weeks** of detailed, progressive lesson plans per course. Each week must have a specific, measurable learning target.
4. **Professional Rationale**: Write a compelling **program_rationale** (2 paragraphs) that explains how this specific curriculum addresses the current "skills gap" in {data['domain']} and its impact on the global economy.
5. **Career Trajectories**: Identify 5 high-impact **target_careers** with corresponding seniority levels (e.g., "Principal AI Architect", "Senior Policy Analyst").
6. **Bloom's Taxonomy Alignment**: Ensure learning outcomes are mapped to higher-order thinking (Analyze, Evaluate, Create).
7. **Accreditation Mapping**: Explicitly reference {data['accreditation_body']} standards (e.g., "PO/CO Mapping") in the outcome codes.

### OUTPUT STRUCTURE:
Output ONLY a single valid JSON object. Do not include markdown code blocks or extra text.
{{
  "program_title": "Full Degree Name",
  "program_type": "{data['program_type']}",
  "domain": "{data['domain']}",
  "academic_level": "{data['academic_level']}",
  "total_semesters": number,
  "program_rationale": "Detailed academic vision...",
  "target_careers": ["Career 1", "Career 2", ...],
  "accreditation_aligned": "Formal alignment statement...",
  "courses_by_semester": {{
    "Semester 1": [
      {{
        "course_code": "CODE101",
        "course_name": "Advanced Course Title",
        "category": "Core/Specialization/Foundational",
        "description": "Rigorous 3-sentence summary...",
        "credits": number,
        "prerequisites": ["CODE000"],
        "weekly_topics": [
          {{
            "week": 1,
            "title": "Rigorous Topic",
            "description": "Scientific/Technical focus...",
            "resources": ["Peer-reviewed journal", "Industry Whitepaper"]
          }}
        ],
        "outcomes": [
          {{
            "outcome": "Measurable high-level outcome...",
            "bloom_level": "Create/Analyze",
            "code": "ACC-CRIT-1"
          }}
        ]
      }}
    ]
  }},
  "recommended_skills": ["Expertise 1", "Expertise 2", ...],
  "industry_alignment_notes": "Critique of how this meets current trends...",
  "optimization_tips": ["Future-proofing suggestion 1", ...]
}}
"""

    try:
        # Using the latest Gemini 2.0 model for speed and robustness
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)

        if not response or not response.text:
            raise ValueError("No response from AI")

        result = extract_json_from_response(response.text)
        return result

    except Exception as e:
        import traceback
        # Write to a persistent log for debugging
        with open("ai_debug.log", "a") as f:
            f.write(f"\n--- AI FAILURE ---\n{str(e)}\n{traceback.format_exc()}\n")
        print(f"AI generation path failed, switching to Smart Fallback. See ai_debug.log")
        return generate_mock_fallback(data)


def generate_mock_fallback(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Hyper-Advanced 'Smart Fallback' with Domain Categorization Engine.
    Mimics Elite AI output by mapping domains to realistic academic modules.
    """
    domain_raw = data.get("domain", "General Studies").lower()
    p_type = data.get("program_type", "Degree")
    level = data.get("academic_level", "Undergraduate")
    semesters = min(data.get("duration_semesters", 4), 8)
    
    # Domain Knowledge Map (Granular)
    knowledge_map = {
        # Specialized Tech Domains
        "ai": {
            "foundations": ["Linear Algebra for ML", "Probability & Statistics", "Python for AI"],
            "core": ["Machine Learning Fundamentals", "Deep Learning Architectures", "Natural Language Processing", "Computer Vision"],
            "advanced": ["Reinforcement Learning", "Generative AI", "AI Ethics & Governance", "Edge AI"],
            "topics": ["Neural Network Backpropagation", "Transformer Models", "CNN & RNN Architectures", "Gradient Descent Optimization", "Large Language Models", "Federated Learning"]
        },
        "data_science": {
            "foundations": ["Statistics & Probability", "Data Wrangling with Pandas", "SQL Mastery"],
            "core": ["Exploratory Data Analysis", "Machine Learning for DS", "Data Visualization", "Feature Engineering"],
            "advanced": ["Big Data Analytics", "Time Series Forecasting", "MLOps & Deployment", "A/B Testing"],
            "topics": ["Regression Analysis", "Clustering Algorithms", "Hypothesis Testing", "Dashboard Design", "Data Pipelines", "Model Interpretability"]
        },
        "cybersecurity": {
            "foundations": ["Networking Fundamentals", "Operating System Security", "Cryptography Basics"],
            "core": ["Ethical Hacking", "Security Operations", "Cloud Security", "Threat Intelligence"],
            "advanced": ["Penetration Testing", "Incident Response", "Zero Trust Architecture", "Security Automation"],
            "topics": ["OWASP Top 10", "Firewall Configuration", "SIEM Analysis", "Malware Analysis", "Identity Management", "Vulnerability Assessment"]
        },
        "vlsi": {
            "foundations": ["Digital Electronics", "CMOS Technology", "Verilog HDL"],
            "core": ["ASIC Design Flow", "FPGA Programming", "Physical Design", "Timing Analysis"],
            "advanced": ["Low Power Design", "Design for Testability", "SoC Architecture", "Nanoscale CMOS"],
            "topics": ["Synthesis & Optimization", "Floor Planning", "Clock Tree Synthesis", "RTL Verification", "Static Timing Analysis", "Power Grid Analysis"]
        },
        # General Tech
        "tech": {
            "foundations": ["Computational Logic", "Data Structures", "Algorithm Design"],
            "core": ["System Architecture", "Database Management", "Software Engineering", "Network Security"],
            "advanced": ["Machine Learning", "Distributed Systems", "Cloud Computing", "AI Ethics"],
            "topics": ["Asymptotic Analysis", "SQL Optimization", "Concurrent Programming", "Microservices", "API Integration", "Scalability Patterns"]
        },
        # Business
        "business": {
            "foundations": ["Microeconomics", "Business Communication", "Accounting Principles"],
            "core": ["Strategic Marketing", "Financial Management", "Operations Logistics", "Organizational Behavior"],
            "advanced": ["Corporate Governance", "Market Analytics", "International Finance", "Entrepreneurship"],
            "topics": ["Supply Chain Optimization", "SWOT Analysis", "Regression Modeling", "Crisis Management", "Venture Capital Valuation", "ESG Standards"]
        },
        # Health
        "health": {
            "foundations": ["Anatomy & Physiology", "Medical Terminology", "Health Psychology"],
            "core": ["Pathophysiology", "Pharmacology", "Clinical Assessment", "Epidemiology"],
            "advanced": ["Health Informatics", "Biostatistics", "Medical Ethics", "Healthcare Policy"],
            "topics": ["Patient Centered Care", "Molecular Diagnosis", "Drug Interaction Analysis", "HIPAA Compliance", "Global Health Trends", "Clinical Protocol Design"]
        },
        # Engineering
        "engineering": {
            "foundations": ["Engineering Mathematics", "Solid Mechanics", "Thermodynamics"],
            "core": ["Fluid Dynamics", "Control Systems", "Material Science", "CAD/CAM Modeling"],
            "advanced": ["Robotics Engineering", "Finite Element Analysis", "Structural Integrity", "Sustainable Design"],
            "topics": ["Stress-Strain Analysis", "Kinematics", "Heat Transfer", "Mechatronics", "Failure Mode Analysis", "Lean Manufacturing"]
        },
        # Science
        "science": {
            "foundations": ["Scientific Method", "Calculus for Science", "Experimental Techniques"],
            "core": ["Quantitative Analysis", "Organic Chemistry", "Quantum Mechanics", "Genetics"],
            "advanced": ["Nanotechnology", "Astrobiology", "Particle Physics", "Environmental Ethics"],
            "topics": ["Spectroscopy", "Statistical Thermodynamics", "Genetic Sequencing", "Subatomic Particles", "Ecosystem Dynamics", "Chemical Equilibrium"]
        }
    }

    # Granular Categorization Engine
    category = "tech"  # Default
    
    # Priority 1: Direct keyword match for specific popular domains
    if any(k in domain_raw for k in ["artificial intelligence", " ai ", "ai/ml", "machine learning", "deep learning"]):
        category = "ai"
    elif any(k in domain_raw for k in ["data science", "data analytics", "big data"]):
        category = "data_science"
    elif any(k in domain_raw for k in ["cyber", "security", "ethical hack", "infosec"]):
        category = "cybersecurity"
    elif any(k in domain_raw for k in ["vlsi", "asic", "fpga", "chip design", "semiconductor"]):
        category = "vlsi"
    # Priority 2: General category match
    elif any(k in domain_raw for k in ["busin", "manag", "mba", "marke", "finan", "econo"]):
        category = "business"
    elif any(k in domain_raw for k in ["health", "med", "nurs", "bio", "pharm", "clinic"]):
        category = "health"
    elif any(k in domain_raw for k in ["engin", "mech", "civil", "elect", "robot"]):
        category = "engineering"
    elif any(k in domain_raw for k in ["scien", "phys", "chem", "math"]):
        category = "science"
    
    sector = knowledge_map.get(category, knowledge_map["tech"])
    domain_proper = data.get("domain", "Advanced Technology")

    courses_by_semester = {}
    topic_pool = sector["topics"]
    
    for sem in range(1, semesters + 1):
        sem_courses = []
        # Number of courses per semester: 1-2 for short programs, 3 for standard
        num_courses = 3 if semesters >= 4 else 2
        
        for i in range(1, num_courses + 1):
            is_capstone = (sem == semesters and i == num_courses)
            is_foundational = (sem == 1 and i == 1)
            
            if is_capstone:
                course_name = f"Strategic Capstone: {domain_proper} Integration"
                pool = sector["advanced"]
                cat = "Capstone"
            elif is_foundational:
                course_name = f"Foundations of {domain_proper}"
                pool = sector["foundations"]
                cat = "Foundational"
            else:
                pool = sector["core"]
                module = pool[(sem + i) % len(pool)]
                course_name = f"{domain_proper} {module}"
                cat = "Core Requirement"

            course_code = f"{category[:2].upper()}{100*sem + i}"
            
            # Generate 6-8 specific topics derived from the pool
            weekly_topics = []
            for w in range(1, 7):
                t_idx = (sem * i * w) % len(topic_pool)
                topic_title = topic_pool[t_idx]
                weekly_topics.append({
                    "week": w,
                    "title": topic_title,
                    "description": f"Comprehensive analysis and practical implementation of {topic_title} in the context of {domain_proper}.",
                    "resources": [f"Academic Paper: {topic_title} in 2026", f"Industry Standard for {domain_proper}"]
                })

            course = {
                "course_code": course_code,
                "course_name": course_name,
                "category": cat,
                "description": f"This intensive course focuses on {course_name}, delivering a deep-dive into {topic_pool[0]} and {topic_pool[1]}. Students will master the core professional competencies required for {domain_proper} roles.",
                "credits": 4,
                "prerequisites": [f"{category[:2].upper()}101"] if sem > 1 else [],
                "weekly_topics": weekly_topics,
                "outcomes": [
                    {"outcome": f"Synthesize complex {domain_proper} theories into actionable strategies", "bloom_level": "Create", "code": "ABET-A1"},
                    {"outcome": f"Evaluate the efficacy of {domain_proper} implementations at scale", "bloom_level": "Evaluate", "code": "NAAC-B2"}
                ]
            }
            sem_courses.append(course)
        
        courses_by_semester[f"Semester {sem}"] = sem_courses

    return {
        "program_title": f"Professional {p_type} in {domain_proper}",
        "program_type": p_type,
        "domain": domain_proper,
        "academic_level": level,
        "total_semesters": semesters,
        "program_rationale": f"This elite {p_type} in {domain_proper} is specifically engineered to address the critical talent shortage in the {domain_proper} sector. The curriculum transitions from foundational theoretical rigor to advanced optimization, ensuring that graduates can navigate the complexities of 2026-era challenges with precision and strategic foresight.",
        "target_careers": [f"{domain_proper} Architect", f"Chief {domain_proper} Officer", f"Director of Strategy", f"Senior Researcher", f"Lead Engineer"],
        "accreditation_aligned": f"Fully aligned with {data.get('accreditation_body', 'Global')} 2026 Excellence Framework (Smart Fallback Mode)",
        "courses_by_semester": courses_by_semester,
        "recommended_skills": [f"Advanced {domain_proper} Modeling", "Strategic Roadmapping", "High-Stakes Technical Communication", "Systemic Optimization"],
        "industry_alignment_notes": f"Note: CurricuForge is currently in 'Smart Fallback' mode due to high AI traffic (Quota Limit). The curriculum is procedurally generated but remains specifically mapped to its academic sector.",
        "optimization_tips": [
            f"Increase focus on sustainability and lifecycle management within the {domain_proper} framework.",
            f"Adopt a cross-disciplinary approach by integrating modules from related fields."
        ]
    }