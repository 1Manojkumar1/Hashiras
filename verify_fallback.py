from ai_engine import generate_curriculum_with_gemini

test_cases = [
    {"domain": "Quantum Computing", "expected_cat": "tech", "expected_topic": "Asymptotic Analysis"},
    {"domain": "Strategic MBA", "expected_cat": "business", "expected_topic": "SWOT Analysis"},
    {"domain": "Advanced Nursing", "expected_cat": "health", "expected_topic": "Clinical Protocol Design"}
]

print("🚀 Starting Domain-Specific Fallback Verification...")

for case in test_cases:
    data = {
        "program_type": "B.Tech" if case["expected_cat"] == "tech" else "Master",
        "domain": case["domain"],
        "academic_level": "Undergraduate",
        "duration_semesters": 2,
        "accreditation_body": "ABET"
    }
    
    # We force the fallback path by passing it directly to generate_mock_fallback
    # or just calling the main function and letting the AI fail (which it likely will due to quota)
    from ai_engine import generate_mock_fallback
    result = generate_mock_fallback(data)
    
    print(f"\n--- Testing Domain: {case['domain']} ---")
    print(f"Program Title: {result['program_title']}")
    sem1_courses = result['courses_by_semester']['Semester 1']
    print(f"Sample Course: {sem1_courses[0]['course_name']}")
    week1_topic = sem1_courses[0]['weekly_topics'][0]['title']
    print(f"Week 1 Topic: {week1_topic}")
    
    if any(t['title'] == case['expected_topic'] for c in sem1_courses for t in c['weekly_topics']):
        print(f"✅ PASSED: Found expected topic '{case['expected_topic']}'")
    else:
        # Check all semesters
        found = False
        for sem, courses in result['courses_by_semester'].items():
            for c in courses:
                for t in c['weekly_topics']:
                    if t['title'] == case['expected_topic']:
                        found = True
                        break
        if found:
            print(f"✅ PASSED: Found expected topic '{case['expected_topic']}' in a subsequent semester/course.")
        else:
            print(f"❌ FAILED: Topic '{case['expected_topic']}' not found in output.")
