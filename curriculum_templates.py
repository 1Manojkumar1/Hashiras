# Curriculum Templates Database
# This module provides templates for generating curricula for all program-domain combinations

from typing import Dict, Any, List

# ==========================================
# DOMAIN KNOWLEDGE TEMPLATES
# ==========================================
DOMAIN_TEMPLATES = {
    # TECH DOMAINS
    "Artificial Intelligence": {
        "category": "tech",
        "courses": ["Foundations of AI", "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision", "Reinforcement Learning", "AI Ethics", "Capstone: AI Systems"],
        "topics": ["Neural Networks", "Transformers", "CNNs", "RNNs", "Gradient Descent", "Backpropagation", "LLMs", "Federated Learning"],
        "careers": ["AI Engineer", "ML Engineer", "Data Scientist", "Research Scientist", "AI Product Manager"],
        "skills": ["Python", "TensorFlow", "PyTorch", "Linear Algebra", "Statistics"]
    },
    "Data Science": {
        "category": "tech",
        "courses": ["Introduction to Data Science", "Statistics & Probability", "Machine Learning", "Data Visualization", "Big Data Analytics", "MLOps", "Business Intelligence", "Capstone: Data Projects"],
        "topics": ["Regression Analysis", "Clustering", "Hypothesis Testing", "Feature Engineering", "Data Pipelines", "A/B Testing"],
        "careers": ["Data Scientist", "Data Analyst", "BI Analyst", "ML Engineer", "Analytics Consultant"],
        "skills": ["Python", "SQL", "Tableau", "Statistics", "Machine Learning"]
    },
    "Cybersecurity": {
        "category": "tech",
        "courses": ["Cybersecurity Fundamentals", "Network Security", "Cryptography", "Ethical Hacking", "Incident Response", "Cloud Security", "Security Operations", "Capstone: Security Audit"],
        "topics": ["OWASP Top 10", "Firewall Config", "SIEM", "Malware Analysis", "Penetration Testing", "Zero Trust"],
        "careers": ["Security Analyst", "Penetration Tester", "Security Engineer", "CISO", "Incident Responder"],
        "skills": ["Network Security", "Linux", "Python", "SIEM Tools", "Ethical Hacking"]
    },
    "Computer Science": {
        "category": "tech",
        "courses": ["Programming Fundamentals", "Data Structures", "Algorithms", "Operating Systems", "Database Systems", "Software Engineering", "Computer Networks", "Capstone: Software Project"],
        "topics": ["Sorting Algorithms", "Graph Theory", "Concurrency", "OOP", "SQL", "API Design"],
        "careers": ["Software Engineer", "Backend Developer", "Systems Architect", "DevOps Engineer", "Tech Lead"],
        "skills": ["Python", "Java", "SQL", "Data Structures", "System Design"]
    },
    "VLSI Design": {
        "category": "tech",
        "courses": ["Digital Electronics", "CMOS Technology", "Verilog HDL", "ASIC Design", "FPGA Programming", "Physical Design", "DFT", "Capstone: Chip Design"],
        "topics": ["RTL Verification", "Synthesis", "Floor Planning", "Clock Tree", "Timing Analysis", "Power Grid"],
        "careers": ["VLSI Engineer", "Design Engineer", "Verification Engineer", "Physical Design Engineer", "ASIC Architect"],
        "skills": ["Verilog", "SystemVerilog", "Cadence", "Synopsys", "FPGA"]
    },
    "Machine Learning": {
        "category": "tech",
        "courses": ["ML Fundamentals", "Supervised Learning", "Unsupervised Learning", "Deep Learning", "NLP", "Computer Vision", "MLOps", "Capstone: ML Systems"],
        "topics": ["Linear Regression", "Decision Trees", "Neural Networks", "CNNs", "Transfer Learning", "Model Deployment"],
        "careers": ["ML Engineer", "Data Scientist", "AI Researcher", "MLOps Engineer", "Applied Scientist"],
        "skills": ["Python", "Scikit-learn", "TensorFlow", "PyTorch", "Statistics"]
    },
    "Cloud Computing": {
        "category": "tech",
        "courses": ["Cloud Fundamentals", "AWS Architecture", "Azure Services", "Kubernetes", "Serverless", "Cloud Security", "DevOps", "Capstone: Cloud Migration"],
        "topics": ["EC2", "S3", "Lambda", "Docker", "CI/CD", "Infrastructure as Code"],
        "careers": ["Cloud Architect", "DevOps Engineer", "SRE", "Cloud Consultant", "Platform Engineer"],
        "skills": ["AWS", "Azure", "Kubernetes", "Terraform", "Docker"]
    },
    "Web Development": {
        "category": "tech",
        "courses": ["HTML/CSS", "JavaScript", "React/Vue", "Node.js", "Databases", "API Development", "DevOps Basics", "Capstone: Full Stack App"],
        "topics": ["REST APIs", "React Hooks", "SQL", "Authentication", "Responsive Design", "Performance"],
        "careers": ["Frontend Developer", "Backend Developer", "Full Stack Developer", "UI Engineer", "Web Architect"],
        "skills": ["JavaScript", "React", "Node.js", "SQL", "Git"]
    },
    # BUSINESS DOMAINS
    "Marketing": {
        "category": "business",
        "courses": ["Marketing Management", "Consumer Behavior", "Digital Marketing", "Brand Management", "Marketing Analytics", "Sales Strategy", "IMC", "Capstone: Marketing Plan"],
        "topics": ["STP", "SWOT", "SEO/SEM", "Social Media", "Content Marketing", "Analytics"],
        "careers": ["Marketing Manager", "Brand Manager", "Digital Marketing Director", "CMO", "Growth Manager"],
        "skills": ["Digital Marketing", "Analytics", "Brand Strategy", "Communication", "SEO"]
    },
    "Finance": {
        "category": "business",
        "courses": ["Corporate Finance", "Financial Markets", "Investment Analysis", "Risk Management", "Financial Modeling", "Derivatives", "Valuation", "Capstone: Investment Portfolio"],
        "topics": ["DCF", "WACC", "Portfolio Theory", "Options", "Bond Valuation", "M&A"],
        "careers": ["Financial Analyst", "Investment Banker", "Portfolio Manager", "CFO", "Risk Manager"],
        "skills": ["Financial Modeling", "Excel", "Valuation", "Risk Analysis", "CFA Prep"]
    },
    "Human Resources": {
        "category": "business",
        "courses": ["HR Management", "Talent Acquisition", "Compensation & Benefits", "Employee Relations", "HR Analytics", "Organizational Development", "Labor Laws", "Capstone: HR Strategy"],
        "topics": ["Recruitment", "Performance Management", "Training", "HRIS", "Culture", "Diversity"],
        "careers": ["HR Manager", "Talent Acquisition Lead", "HR Business Partner", "CHRO", "L&D Manager"],
        "skills": ["HR Analytics", "Communication", "Labor Law", "HRIS", "Leadership"]
    },
    "Operations": {
        "category": "business",
        "courses": ["Operations Management", "Supply Chain", "Quality Management", "Lean Six Sigma", "Project Management", "Logistics", "Procurement", "Capstone: Process Optimization"],
        "topics": ["Inventory Management", "JIT", "TQM", "Process Mapping", "KPIs", "Forecasting"],
        "careers": ["Operations Manager", "Supply Chain Manager", "Process Engineer", "COO", "Logistics Director"],
        "skills": ["Lean Six Sigma", "Project Management", "Analytics", "ERP", "Process Optimization"]
    },
    "Business Analytics": {
        "category": "business",
        "courses": ["Analytics Fundamentals", "Statistics for Business", "Predictive Modeling", "Data Visualization", "Decision Science", "Big Data", "Machine Learning for Business", "Capstone: Analytics Project"],
        "topics": ["Regression", "Forecasting", "Dashboards", "SQL", "Python", "Optimization"],
        "careers": ["Business Analyst", "Data Analyst", "Analytics Manager", "Decision Scientist", "BI Developer"],
        "skills": ["SQL", "Python", "Tableau", "Statistics", "Excel"]
    },
    # SCIENCE DOMAINS
    "Physics": {
        "category": "science",
        "courses": ["Classical Mechanics", "Electromagnetism", "Quantum Mechanics", "Thermodynamics", "Statistical Mechanics", "Optics", "Nuclear Physics", "Capstone: Research Project"],
        "topics": ["Newton's Laws", "Maxwell Equations", "Schrodinger", "Entropy", "Wave-Particle Duality", "Relativity"],
        "careers": ["Physicist", "Research Scientist", "Data Scientist", "Quant Analyst", "Lab Director"],
        "skills": ["Mathematical Modeling", "Python", "Lab Skills", "Data Analysis", "Research"]
    },
    "Chemistry": {
        "category": "science",
        "courses": ["General Chemistry", "Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Analytical Chemistry", "Biochemistry", "Spectroscopy", "Capstone: Research"],
        "topics": ["Reactions", "Synthesis", "Thermodynamics", "Spectroscopy", "Kinetics", "Bonding"],
        "careers": ["Chemist", "Research Scientist", "Lab Manager", "Quality Analyst", "Pharma Scientist"],
        "skills": ["Lab Techniques", "Spectroscopy", "Data Analysis", "Safety", "Research"]
    },
    "Mathematics": {
        "category": "science",
        "courses": ["Calculus", "Linear Algebra", "Abstract Algebra", "Real Analysis", "Probability", "Statistics", "Numerical Methods", "Capstone: Research"],
        "topics": ["Derivatives", "Matrices", "Groups", "Limits", "Distributions", "Optimization"],
        "careers": ["Mathematician", "Data Scientist", "Quant", "Actuary", "Research Scientist"],
        "skills": ["Mathematical Modeling", "Python", "Statistics", "Logic", "Research"]
    },
    "Biology": {
        "category": "science",
        "courses": ["Cell Biology", "Genetics", "Molecular Biology", "Ecology", "Biochemistry", "Microbiology", "Evolution", "Capstone: Research"],
        "topics": ["DNA", "Gene Expression", "Ecosystems", "Protein Synthesis", "Metabolism", "Biodiversity"],
        "careers": ["Biologist", "Research Scientist", "Biotech Scientist", "Lab Manager", "Science Writer"],
        "skills": ["Lab Techniques", "Data Analysis", "Research", "Bioinformatics", "Scientific Writing"]
    },
    "Biotechnology": {
        "category": "science",
        "courses": ["Biotechnology Fundamentals", "Genetic Engineering", "Bioprocessing", "Bioinformatics", "Immunology", "Pharma Biotech", "Biosafety", "Capstone: Biotech Project"],
        "topics": ["PCR", "Cloning", "Fermentation", "Sequence Analysis", "Antibodies", "Drug Development"],
        "careers": ["Biotech Scientist", "Research Associate", "Bioprocess Engineer", "Bioinformatician", "QA Specialist"],
        "skills": ["Lab Techniques", "Bioinformatics", "Data Analysis", "GMP", "Research"]
    },
    # ENGINEERING DOMAINS
    "Mechanical Engineering": {
        "category": "engineering",
        "courses": ["Engineering Mechanics", "Thermodynamics", "Fluid Mechanics", "Machine Design", "Manufacturing", "Heat Transfer", "Vibrations", "Capstone: Design Project"],
        "topics": ["Stress Analysis", "Heat Exchangers", "CAD", "FEA", "CNC", "Kinematics"],
        "careers": ["Mechanical Engineer", "Design Engineer", "Manufacturing Engineer", "Project Engineer", "R&D Engineer"],
        "skills": ["CAD/CAM", "FEA", "Thermodynamics", "Manufacturing", "Project Management"]
    },
    "Civil Engineering": {
        "category": "engineering",
        "courses": ["Structural Analysis", "Geotechnical Engineering", "Transportation", "Hydraulics", "Construction Management", "Environmental Engineering", "Design Codes", "Capstone: Infrastructure Project"],
        "topics": ["Beam Design", "Soil Mechanics", "Highway Design", "Water Treatment", "Project Planning", "Safety"],
        "careers": ["Civil Engineer", "Structural Engineer", "Project Manager", "Construction Manager", "Urban Planner"],
        "skills": ["AutoCAD", "Structural Analysis", "Project Management", "Cost Estimation", "Safety"]
    },
    "Electrical Engineering": {
        "category": "engineering",
        "courses": ["Circuit Theory", "Electronics", "Power Systems", "Control Systems", "Signal Processing", "Electrical Machines", "Power Electronics", "Capstone: EE Project"],
        "topics": ["AC/DC Analysis", "Amplifiers", "Transformers", "PID Control", "DSP", "Motors"],
        "careers": ["Electrical Engineer", "Power Engineer", "Control Engineer", "Design Engineer", "Systems Engineer"],
        "skills": ["Circuit Design", "MATLAB", "Power Systems", "Control Systems", "Simulation"]
    },
    "Electronics": {
        "category": "engineering",
        "courses": ["Electronic Devices", "Analog Circuits", "Digital Electronics", "Microprocessors", "Communication Systems", "Embedded Systems", "VLSI Basics", "Capstone: Electronics Project"],
        "topics": ["Transistors", "Op-Amps", "Logic Gates", "Microcontrollers", "Modulation", "PCB Design"],
        "careers": ["Electronics Engineer", "Embedded Engineer", "Hardware Engineer", "RF Engineer", "Design Engineer"],
        "skills": ["Circuit Design", "PCB", "Embedded C", "Verilog", "Testing"]
    },
    "Robotics": {
        "category": "engineering",
        "courses": ["Robot Mechanics", "Control Systems", "Sensors & Actuators", "Computer Vision", "Motion Planning", "AI for Robotics", "ROS", "Capstone: Robot Design"],
        "topics": ["Kinematics", "PID Control", "SLAM", "Path Planning", "Object Detection", "Manipulation"],
        "careers": ["Robotics Engineer", "Automation Engineer", "Control Engineer", "Research Scientist", "Systems Integrator"],
        "skills": ["ROS", "Python", "Control Systems", "Computer Vision", "Mechanical Design"]
    },
    # HEALTHCARE DOMAINS
    "Healthcare": {
        "category": "health",
        "courses": ["Healthcare Systems", "Medical Terminology", "Health Informatics", "Public Health", "Healthcare Policy", "Clinical Practice", "Healthcare Management", "Capstone: Healthcare Project"],
        "topics": ["Patient Care", "HIPAA", "EHR Systems", "Epidemiology", "Quality Improvement", "Leadership"],
        "careers": ["Healthcare Administrator", "Health Informatics Specialist", "Clinical Manager", "Public Health Analyst", "Quality Manager"],
        "skills": ["Healthcare Systems", "Data Analysis", "Compliance", "Leadership", "Communication"]
    },
    # OTHER DOMAINS
    "Digital Marketing": {
        "category": "business",
        "courses": ["Digital Marketing Fundamentals", "SEO/SEM", "Social Media Marketing", "Content Marketing", "Email Marketing", "Analytics", "E-commerce", "Capstone: Digital Campaign"],
        "topics": ["Google Ads", "Facebook Ads", "SEO", "Content Strategy", "Analytics", "Conversion"],
        "careers": ["Digital Marketing Manager", "SEO Specialist", "Social Media Manager", "Content Strategist", "Growth Hacker"],
        "skills": ["Google Analytics", "SEO", "Social Media", "Content Creation", "Paid Ads"]
    },
    "Project Management": {
        "category": "business",
        "courses": ["PM Fundamentals", "Agile/Scrum", "Risk Management", "Stakeholder Management", "Budgeting", "Quality Management", "PMP Prep", "Capstone: Project Simulation"],
        "topics": ["WBS", "Gantt Charts", "Sprint Planning", "Risk Register", "Earned Value", "Retrospectives"],
        "careers": ["Project Manager", "Scrum Master", "Program Manager", "PMO Director", "Agile Coach"],
        "skills": ["Agile", "MS Project", "Communication", "Risk Management", "Leadership"]
    },
}

# Program type metadata
PROGRAM_METADATA = {
    "B.Tech": {"level": "Undergraduate", "semesters": 8, "credits": 4},
    "M.Tech": {"level": "Graduate", "semesters": 4, "credits": 4},
    "B.Sc": {"level": "Undergraduate", "semesters": 6, "credits": 3},
    "M.Sc": {"level": "Graduate", "semesters": 4, "credits": 3},
    "MBA": {"level": "Graduate", "semesters": 4, "credits": 3},
    "BBA": {"level": "Undergraduate", "semesters": 6, "credits": 3},
    "PhD": {"level": "Doctoral", "semesters": 8, "credits": 4},
    "Diploma": {"level": "Undergraduate", "semesters": 4, "credits": 3},
    "Associate Degree": {"level": "Undergraduate", "semesters": 4, "credits": 3},
    "Certification": {"level": "Professional", "semesters": 2, "credits": 2},
}

def generate_curriculum_from_template(data: Dict[str, Any]) -> Dict[str, Any]:
    """Generate a curriculum using domain templates."""
    program_type = data.get("program_type", "B.Tech")
    domain = data.get("domain", "Computer Science")
    academic_level = data.get("academic_level", "Undergraduate")
    duration = data.get("duration_semesters", 8)
    accreditation = data.get("accreditation_body", "NAAC")
    
    # Get domain template (default to Computer Science)
    template = DOMAIN_TEMPLATES.get(domain, DOMAIN_TEMPLATES.get("Computer Science"))
    program_meta = PROGRAM_METADATA.get(program_type, PROGRAM_METADATA["B.Tech"])
    
    # Limit semesters to requested duration
    num_semesters = min(duration, program_meta["semesters"])
    courses_per_sem = 3 if num_semesters >= 4 else 2
    
    # Generate courses by semester
    courses_by_semester = {}
    course_list = template["courses"]
    topics_pool = template["topics"]
    
    course_idx = 0
    for sem in range(1, num_semesters + 1):
        sem_courses = []
        for c in range(courses_per_sem):
            if course_idx >= len(course_list):
                course_idx = 0  # Cycle through courses
            
            course_name = f"{domain}: {course_list[course_idx]}"
            course_code = f"{domain[:2].upper()}{100*sem + c + 1}"
            
            # Determine category
            if sem == 1:
                cat = "Foundational"
            elif sem == num_semesters:
                cat = "Capstone"
            else:
                cat = "Core Requirement"
            
            # Generate unique weekly topics for THIS course
            # Each course gets topics based on its name + domain topics
            course_specific_topics = [
                f"Introduction to {course_list[course_idx]}",
                f"Core Concepts of {course_list[course_idx]}",
                f"Advanced {course_list[course_idx]} Techniques",
                f"Practical Applications of {course_list[course_idx]}",
                f"Case Studies in {course_list[course_idx]}",
                f"Industry Tools for {course_list[course_idx]}",
                f"Research Trends in {course_list[course_idx]}",
                f"Capstone Project: {course_list[course_idx]}"
            ]
            
            # Mix domain topics with course-specific topics
            weekly_topics = []
            for w in range(1, 7):
                if w <= 2:
                    # First 2 weeks: course-specific intro
                    topic_title = course_specific_topics[w - 1]
                elif w <= 4:
                    # Middle weeks: domain topics (use unique index)
                    unique_idx = (course_idx * 6 + w) % len(topics_pool)
                    topic_title = topics_pool[unique_idx]
                else:
                    # Last weeks: advanced course topics
                    topic_title = course_specific_topics[w]
                
                weekly_topics.append({
                    "week": w,
                    "title": topic_title,
                    "description": f"Week {w}: In-depth study of {topic_title} within {course_list[course_idx]}.",
                    "resources": [f"Textbook Ch. {w}", f"Lab Exercise {w}", f"Case Study {w}"]
                })
            
            sem_courses.append({
                "course_code": course_code,
                "course_name": course_name,
                "category": cat,
                "description": f"Comprehensive study of {course_list[course_idx]} in the context of {domain}. Students develop both theoretical understanding and practical skills.",
                "credits": program_meta["credits"],
                "prerequisites": [f"{domain[:2].upper()}101"] if sem > 1 else [],
                "weekly_topics": weekly_topics,
                "outcomes": [
                    {"outcome": f"Apply {course_list[course_idx]} concepts to solve real-world problems", "bloom_level": "Apply", "code": f"{accreditation}-PO1"},
                    {"outcome": f"Evaluate {course_list[course_idx]} solutions critically", "bloom_level": "Evaluate", "code": f"{accreditation}-PO2"}
                ]
            })
            course_idx += 1
        
        courses_by_semester[f"Semester {sem}"] = sem_courses
    
    return {
        "program_title": f"{program_type} in {domain}",
        "program_type": program_type,
        "domain": domain,
        "academic_level": academic_level,
        "total_semesters": num_semesters,
        "program_rationale": f"This {program_type} in {domain} is designed to meet the growing industry demand for {domain} professionals. The curriculum provides rigorous theoretical foundations combined with hands-on practical experience, preparing graduates for leadership roles in the field.",
        "target_careers": template["careers"],
        "accreditation_aligned": f"Aligned with {accreditation} Standards",
        "courses_by_semester": courses_by_semester,
        "recommended_skills": template["skills"],
        "industry_alignment_notes": f"This curriculum is aligned with current industry trends in {domain} and meets {accreditation} accreditation requirements.",
        "optimization_tips": [
            f"Consider adding electives in emerging {domain} technologies",
            f"Include industry internship for practical experience"
        ]
    }
