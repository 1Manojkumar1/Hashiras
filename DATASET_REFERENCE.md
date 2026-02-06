# CurricuForge Dataset Reference

This document contains all the configuration options available in the CurricuForge curriculum generator.

---

## Program Types

| Value | Display Name |
|-------|--------------|
| `B.Tech` | B.Tech |
| `M.Tech` | M.Tech |
| `B.Sc` | B.Sc |
| `M.Sc` | M.Sc |
| `MBA` | MBA |
| `BBA` | BBA |
| `PhD` | PhD |
| `Diploma` | Diploma |
| `Associate Degree` | Associate Degree |
| `Certification` | Professional Certification |

---

## Domains by Program Type

### B.Tech
- Artificial Intelligence
- Data Science
- Cybersecurity
- VLSI Design
- Computer Science
- Electronics
- Mechanical Engineering
- Civil Engineering
- Electrical Engineering

### M.Tech
- Artificial Intelligence
- Machine Learning
- Data Science
- Cybersecurity
- VLSI Design
- Embedded Systems
- Robotics
- Structural Engineering
- Power Systems

### B.Sc
- Computer Science
- Physics
- Chemistry
- Mathematics
- Biology
- Environmental Science
- Statistics
- Biotechnology

### M.Sc
- Data Science
- Physics
- Chemistry
- Mathematics
- Biotechnology
- Environmental Science
- Bioinformatics
- Applied Statistics

### MBA
- Marketing
- Finance
- Human Resources
- Operations
- Business Analytics
- Entrepreneurship
- International Business
- Supply Chain Management

### BBA
- Marketing
- Finance
- Human Resources
- Operations
- Entrepreneurship
- International Business

### PhD
- Artificial Intelligence
- Data Science
- Computer Science
- Physics
- Chemistry
- Biology
- Economics
- Management
- Engineering

### Diploma
- Computer Applications
- Web Development
- Mechanical Engineering
- Electrical Engineering
- Civil Engineering
- Electronics

### Associate Degree
- Computer Science
- Business Administration
- Healthcare
- Liberal Arts
- Engineering Technology

### Certification
- Data Science
- Cloud Computing
- Cybersecurity
- Digital Marketing
- Project Management
- Machine Learning
- Web Development

---

## Academic Levels

| Value | Display Name |
|-------|--------------|
| `Undergraduate` | Undergraduate |
| `Graduate` | Graduate |

---

## Duration (Semesters)

| Value | Display Name |
|-------|--------------|
| `1` | 1 Semester |
| `2` | 2 Semesters |
| `3` | 3 Semesters |
| `4` | 4 Semesters (Default) |
| `5` | 5 Semesters |
| `6` | 6 Semesters |
| `7` | 7 Semesters |
| `8` | 8 Semesters |
| `9` | 9 Semesters |
| `10` | 10 Semesters |
| `11` | 11 Semesters |
| `12` | 12 Semesters |

---

## Accreditation Bodies

| Value | Display Name | Region/Specialty |
|-------|--------------|------------------|
| `NAAC` | NAAC | India |
| `NBA` | NBA | India |
| `ABET` | ABET | International/Engineering |
| `AACSB` | AACSB | Business |
| `AMBA` | AMBA | MBA Programs |
| `EQUIS` | EQUIS | Business |
| `UGC` | UGC | India |
| `WASC` | WASC | USA |
| `SACSCOC` | SACSCOC | USA |
| `MSCHE` | MSCHE | USA |
| `BCS` | BCS | Computing |
| `Engineers Australia` | Engineers Australia | Australia/Engineering |
| `Other` | Other / General | General |

---

## AI Fallback Domain Categories

The Smart Fallback engine maps domains to these categories for topic generation:

| Category | Keywords Matched | Example Topics |
|----------|-----------------|----------------|
| `ai` | artificial intelligence, ai, machine learning, deep learning | Transformer Models, Neural Network Backpropagation, Large Language Models |
| `data_science` | data science, data analytics, big data | Clustering Algorithms, Regression Analysis, Model Interpretability |
| `cybersecurity` | cyber, security, ethical hack, infosec | OWASP Top 10, Firewall Configuration, Malware Analysis |
| `vlsi` | vlsi, asic, fpga, chip design, semiconductor | RTL Verification, Clock Tree Synthesis, Static Timing Analysis |
| `tech` | (default for tech domains) | Asymptotic Analysis, Microservices, API Integration |
| `business` | business, management, mba, marketing, finance, economics | SWOT Analysis, Crisis Management, ESG Standards |
| `health` | health, med, nursing, bio, pharma, clinic | Molecular Diagnosis, HIPAA Compliance, Clinical Protocol Design |
| `engineering` | engineering, mechanical, civil, electrical, robotics | Stress-Strain Analysis, Mechatronics, Lean Manufacturing |
| `science` | science, physics, chemistry, math | Spectroscopy, Genetic Sequencing, Chemical Equilibrium |
