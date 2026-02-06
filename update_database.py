"""Script to add remaining semesters to other programs."""
import json

# Load database
with open("curriculum_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

# Helper function to create a course
def course(code, name, cat, desc, prereqs, topics):
    return {
        "course_code": code, "course_name": name, "category": cat, "credits": 4 if "B.Tech" in code[:4] else 3,
        "prerequisites": prereqs, "description": desc,
        "weekly_topics": [{"week": i+1, "title": t, "description": f"Study of {t}"} for i, t in enumerate(topics)],
        "outcomes": [{"outcome": f"Apply {name} concepts", "bloom_level": "Apply", "code": "NBA-PO"}]
    }

# B.Tech Data Science - Semesters 2-8
DS_SEMS = {
    "Semester 2": [
        course("DS201", "Machine Learning", "Core Requirement", "ML fundamentals and algorithms", ["DS102"],
               ["ML Pipelines", "Linear Regression", "Classification", "Decision Trees", "Ensemble Methods", "Model Selection"]),
        course("DS202", "Database Systems", "Core Requirement", "SQL and data management", ["DS103"],
               ["Relational Databases", "SQL Queries", "Joins and Subqueries", "Normalization", "NoSQL Databases", "Data Warehousing"]),
        course("DS203", "Data Visualization", "Core Requirement", "Visual analytics and dashboards", ["DS103"],
               ["Visualization Principles", "Matplotlib & Seaborn", "Interactive Plots", "Dashboard Design", "Storytelling with Data", "Tableau/PowerBI"])
    ],
    "Semester 3": [
        course("DS301", "Advanced ML", "Specialization", "Deep learning and neural networks", ["DS201"],
               ["Neural Networks", "Deep Learning", "CNNs", "RNNs", "Transfer Learning", "AutoML"]),
        course("DS302", "Big Data Analytics", "Core Requirement", "Distributed computing for data", ["DS202"],
               ["Hadoop Ecosystem", "Spark Fundamentals", "MapReduce", "Data Lakes", "Stream Processing", "Cloud Data Platforms"]),
        course("DS303", "Statistical Modeling", "Core Requirement", "Advanced statistical methods", ["DS102"],
               ["Bayesian Statistics", "Regression Analysis", "Time Series", "Causal Inference", "Experimental Design", "A/B Testing"])
    ],
    "Semester 4": [
        course("DS401", "NLP for Data Science", "Elective", "Text analytics and NLP", ["DS301"],
               ["Text Preprocessing", "Sentiment Analysis", "Topic Modeling", "Word Embeddings", "Transformers", "Chatbots"]),
        course("DS402", "Time Series Analysis", "Core Requirement", "Forecasting methods", ["DS303"],
               ["Time Series Components", "ARIMA Models", "Exponential Smoothing", "Prophet", "LSTM for Forecasting", "Anomaly Detection"]),
        course("DS403", "Data Engineering", "Core Requirement", "Building data pipelines", ["DS302"],
               ["ETL Processes", "Airflow", "Data Quality", "Feature Stores", "Data Governance", "MLOps Basics"])
    ],
    "Semester 5": [
        course("DS501", "Deep Learning", "Specialization", "Advanced neural networks", ["DS301"],
               ["CNN Architectures", "Sequence Models", "Attention Mechanisms", "GANs", "Autoencoders", "Neural Architecture Search"]),
        course("DS502", "Business Intelligence", "Core Requirement", "BI tools and strategy", ["DS203"],
               ["BI Fundamentals", "KPI Design", "Executive Dashboards", "Self-Service BI", "Data Storytelling", "BI Strategy"]),
        course("DS503", "Ethics in Data Science", "Core Requirement", "Responsible data practices", [],
               ["Data Privacy", "Algorithmic Bias", "Fairness Metrics", "GDPR Compliance", "Explainable AI", "Ethical Guidelines"])
    ],
    "Semester 6": [
        course("DS601", "Recommendation Systems", "Elective", "Building recommender engines", ["DS301"],
               ["Collaborative Filtering", "Content-Based", "Matrix Factorization", "Deep Learning Recsys", "Evaluation Metrics", "A/B Testing Recs"]),
        course("DS602", "Cloud Computing for DS", "Core Requirement", "Cloud platforms for data", ["DS403"],
               ["AWS for Data Science", "Azure ML", "GCP BigQuery", "Serverless Analytics", "Cost Optimization", "Multi-Cloud Strategy"]),
        course("DS603", "Domain Elective", "Elective", "Industry-specific analytics", ["DS301"],
               ["Healthcare Analytics", "Financial Analytics", "Marketing Analytics", "Supply Chain Analytics", "IoT Analytics", "Sports Analytics"])
    ],
    "Semester 7": [
        course("DS701", "Industry Internship", "Practical", "16-week data science internship", [],
               ["Onboarding", "Problem Scoping", "Data Exploration", "Model Building", "Deployment", "Presentation"]),
        course("DS702", "Research Project", "Core Requirement", "Independent research in DS", ["DS501"],
               ["Literature Review", "Research Design", "Data Collection", "Analysis", "Paper Writing", "Peer Review"])
    ],
    "Semester 8": [
        course("DS801", "Capstone Project I", "Capstone", "Major industry project - Phase 1", [],
               ["Problem Definition", "Data Acquisition", "EDA", "Feature Engineering", "Baseline Models", "Progress Review"]),
        course("DS802", "Capstone Project II", "Capstone", "Major industry project - Phase 2", ["DS801"],
               ["Advanced Modeling", "Optimization", "Deployment", "Documentation", "Presentation", "Final Submission"])
    ]
}

# B.Tech Cybersecurity - Semesters 2-8  
CYB_SEMS = {
    "Semester 2": [
        course("CYB201", "Ethical Hacking", "Core Requirement", "Penetration testing fundamentals", ["CYB102"],
               ["Reconnaissance", "Scanning", "Exploitation", "Post-Exploitation", "Reporting", "Legal Considerations"]),
        course("CYB202", "Operating System Security", "Core Requirement", "Securing OS platforms", ["CYB101"],
               ["Linux Security", "Windows Security", "Hardening", "Patch Management", "Access Controls", "Logging"]),
        course("CYB203", "Programming for Security", "Core Requirement", "Security-focused programming", [],
               ["Python for Security", "Scripting", "Automation", "Tool Development", "Secure Coding", "Code Review"])
    ],
    "Semester 3": [
        course("CYB301", "Web Application Security", "Core Requirement", "Securing web applications", ["CYB201"],
               ["OWASP Top 10", "SQL Injection", "XSS", "CSRF", "Authentication Flaws", "Secure Development"]),
        course("CYB302", "Cloud Security", "Core Requirement", "Securing cloud environments", ["CYB102"],
               ["Cloud Architecture", "AWS Security", "Azure Security", "Container Security", "Serverless Security", "Cloud Compliance"]),
        course("CYB303", "Malware Analysis", "Specialization", "Analyzing malicious software", ["CYB202"],
               ["Malware Types", "Static Analysis", "Dynamic Analysis", "Reverse Engineering", "Sandboxing", "Threat Intel"])
    ],
    "Semester 4": [
        course("CYB401", "Digital Forensics", "Core Requirement", "Investigating cyber incidents", ["CYB303"],
               ["Forensic Methodology", "Evidence Collection", "Disk Forensics", "Memory Forensics", "Network Forensics", "Reporting"]),
        course("CYB402", "Incident Response", "Core Requirement", "Handling security incidents", ["CYB101"],
               ["IR Frameworks", "Detection", "Containment", "Eradication", "Recovery", "Lessons Learned"]),
        course("CYB403", "Security Operations", "Core Requirement", "SOC operations and monitoring", ["CYB102"],
               ["SOC Architecture", "SIEM", "Threat Hunting", "Alert Triage", "Playbooks", "Metrics"])
    ],
    "Semester 5": [
        course("CYB501", "Advanced Cryptography", "Specialization", "Modern cryptographic techniques", ["CYB103"],
               ["Elliptic Curves", "Zero Knowledge Proofs", "Homomorphic Encryption", "Post-Quantum Crypto", "Blockchain", "Crypto Protocols"]),
        course("CYB502", "Mobile Security", "Elective", "Securing mobile platforms", ["CYB201"],
               ["Android Security", "iOS Security", "Mobile Threats", "App Analysis", "MDM", "Mobile Forensics"]),
        course("CYB503", "Governance & Compliance", "Core Requirement", "Security governance frameworks", [],
               ["ISO 27001", "NIST Framework", "SOC 2", "PCI DSS", "HIPAA", "Audit Preparation"])
    ],
    "Semester 6": [
        course("CYB601", "IoT Security", "Elective", "Securing Internet of Things", ["CYB302"],
               ["IoT Architecture", "Device Security", "Protocol Security", "Firmware Analysis", "Industrial IoT", "Smart Home Security"]),
        course("CYB602", "Red Team Operations", "Specialization", "Advanced offensive security", ["CYB201"],
               ["Red Team Planning", "Initial Access", "Persistence", "Privilege Escalation", "Lateral Movement", "Exfiltration"]),
        course("CYB603", "Security Research", "Core Requirement", "Vulnerability research methods", ["CYB303"],
               ["Bug Bounty", "CVE Process", "Responsible Disclosure", "PoC Development", "Security Advisories", "Research Ethics"])
    ],
    "Semester 7": [
        course("CYB701", "Industry Internship", "Practical", "Security internship program", [],
               ["SOC Rotation", "Pen Testing", "Incident Response", "Compliance Review", "Tool Evaluation", "Final Report"]),
        course("CYB702", "Certification Prep", "Core Requirement", "Industry certification preparation", [],
               ["CEH Review", "CompTIA Security+", "OSCP Prep", "Practice Labs", "Mock Exams", "Certification Strategy"])
    ],
    "Semester 8": [
        course("CYB801", "Capstone: Security Audit", "Capstone", "Comprehensive security assessment", [],
               ["Scope Definition", "Vulnerability Assessment", "Penetration Testing", "Risk Analysis", "Report Writing", "Presentation"]),
        course("CYB802", "Emerging Security Trends", "Core Requirement", "Future of cybersecurity", [],
               ["AI in Security", "Quantum Threats", "Zero Trust", "Extended Detection", "Security Automation", "Career Planning"])
    ]
}

# MBA Marketing - Semesters 2-4
MKT_SEMS = {
    "Semester 2": [
        course("MKT601", "Brand Management", "Core Requirement", "Building and managing brands", ["MKT501"],
               ["Brand Equity", "Brand Positioning", "Brand Architecture", "Brand Extensions", "Brand Valuation", "Brand Audit"]),
        course("MKT602", "Marketing Analytics", "Core Requirement", "Data-driven marketing", ["MKT503"],
               ["Marketing Metrics", "Customer Analytics", "Attribution Modeling", "Marketing Mix Modeling", "CLV Analysis", "Predictive Marketing"]),
        course("MKT603", "Sales Management", "Core Requirement", "Managing sales operations", ["MKT501"],
               ["Sales Strategy", "Territory Management", "Sales Forecasting", "CRM Systems", "Sales Training", "Performance Management"])
    ],
    "Semester 3": [
        course("MKT701", "Global Marketing", "Core Requirement", "International marketing strategies", ["MKT501"],
               ["Market Entry Modes", "Cultural Adaptation", "Global Branding", "Pricing Strategies", "Distribution Networks", "Trade Barriers"]),
        course("MKT702", "Marketing Technology", "Elective", "MarTech stack management", ["MKT503"],
               ["Marketing Automation", "CRM Platforms", "CDP Systems", "Ad Tech", "Personalization Engines", "MarTech Integration"]),
        course("MKT703", "B2B Marketing", "Elective", "Business-to-business marketing", ["MKT501"],
               ["B2B Buying Process", "Account-Based Marketing", "Lead Generation", "Content Marketing", "Trade Shows", "Partner Marketing"])
    ],
    "Semester 4": [
        course("MKT801", "Marketing Strategy Capstone", "Capstone", "Integrated marketing capstone", ["MKT601"],
               ["Strategic Analysis", "Market Research", "Strategy Development", "Implementation Plan", "Budget Allocation", "Final Presentation"]),
        course("MKT802", "Social Media Marketing", "Elective", "Social media strategies", ["MKT503"],
               ["Platform Strategy", "Community Management", "Influencer Marketing", "Social Commerce", "Crisis Management", "Measurement"]),
        course("MKT803", "Retail Marketing", "Elective", "Omnichannel retail", ["MKT501"],
               ["Retail Strategy", "Store Design", "Category Management", "E-commerce", "Omnichannel Integration", "Customer Experience"])
    ]
}

# MBA Finance - Semesters 2-4
FIN_SEMS = {
    "Semester 2": [
        course("FIN601", "Financial Modeling", "Core Requirement", "Building financial models", ["FIN501"],
               ["Excel Mastery", "Three-Statement Models", "DCF Modeling", "LBO Models", "M&A Models", "Sensitivity Analysis"]),
        course("FIN602", "Risk Management", "Core Requirement", "Enterprise risk management", ["FIN502"],
               ["Risk Identification", "VaR and CVaR", "Credit Risk", "Market Risk", "Operational Risk", "Risk Reporting"]),
        course("FIN603", "Private Equity & VC", "Elective", "Alternative investments", ["FIN503"],
               ["PE Industry", "Deal Sourcing", "Due Diligence", "Valuation Methods", "Portfolio Management", "Exit Strategies"])
    ],
    "Semester 3": [
        course("FIN701", "Mergers & Acquisitions", "Core Requirement", "M&A strategy and execution", ["FIN601"],
               ["M&A Landscape", "Target Identification", "Valuation", "Deal Structuring", "Negotiation", "Integration"]),
        course("FIN702", "International Finance", "Core Requirement", "Global financial markets", ["FIN502"],
               ["FX Markets", "Currency Risk", "International Investing", "Cross-Border M&A", "Transfer Pricing", "Sovereign Risk"]),
        course("FIN703", "FinTech", "Elective", "Technology in finance", ["FIN502"],
               ["Digital Payments", "Blockchain", "Robo-Advisors", "InsurTech", "RegTech", "Open Banking"])
    ],
    "Semester 4": [
        course("FIN801", "Finance Strategy Capstone", "Capstone", "Integrated finance capstone", ["FIN701"],
               ["Case Analysis", "Valuation Project", "Strategy Formulation", "Implementation", "Risk Assessment", "Final Defense"]),
        course("FIN802", "Wealth Management", "Elective", "Personal financial planning", ["FIN503"],
               ["Financial Planning", "Asset Allocation", "Tax Planning", "Estate Planning", "Behavioral Finance", "Client Management"]),
        course("FIN803", "Quantitative Finance", "Elective", "Quantitative trading strategies", ["FIN503"],
               ["Quantitative Methods", "Algorithmic Trading", "Factor Investing", "Options Pricing", "Backtesting", "Execution"])
    ]
}

# Apply updates
for sem, courses in DS_SEMS.items():
    db["B.Tech_Data Science"]["courses_by_semester"][sem] = courses

for sem, courses in CYB_SEMS.items():
    db["B.Tech_Cybersecurity"]["courses_by_semester"][sem] = courses

for sem, courses in MKT_SEMS.items():
    db["MBA_Marketing"]["courses_by_semester"][sem] = courses
    
for sem, courses in FIN_SEMS.items():
    db["MBA_Finance"]["courses_by_semester"][sem] = courses

# Save
with open("curriculum_database.json", "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Updated all programs with complete semesters!")
print(f"  B.Tech Data Science: {len(db['B.Tech_Data Science']['courses_by_semester'])} semesters")
print(f"  B.Tech Cybersecurity: {len(db['B.Tech_Cybersecurity']['courses_by_semester'])} semesters")
print(f"  MBA Marketing: {len(db['MBA_Marketing']['courses_by_semester'])} semesters")
print(f"  MBA Finance: {len(db['MBA_Finance']['courses_by_semester'])} semesters")
