// ==========================================
// CASCADING DROPDOWN: Program Type → Domain
// ==========================================
const domainsByProgram = {
  "B.Tech": ["Artificial Intelligence", "Data Science", "Cybersecurity", "VLSI Design", "Computer Science", "Electronics", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering"],
  "M.Tech": ["Artificial Intelligence", "Machine Learning", "Data Science", "Cybersecurity", "VLSI Design", "Embedded Systems", "Robotics", "Structural Engineering", "Power Systems"],
  "B.Sc": ["Computer Science", "Physics", "Chemistry", "Mathematics", "Biology", "Environmental Science", "Statistics", "Biotechnology"],
  "M.Sc": ["Data Science", "Physics", "Chemistry", "Mathematics", "Biotechnology", "Environmental Science", "Bioinformatics", "Applied Statistics"],
  "MBA": ["Marketing", "Finance", "Human Resources", "Operations", "Business Analytics", "Entrepreneurship", "International Business", "Supply Chain Management"],
  "BBA": ["Marketing", "Finance", "Human Resources", "Operations", "Entrepreneurship", "International Business"],
  "PhD": ["Artificial Intelligence", "Data Science", "Computer Science", "Physics", "Chemistry", "Biology", "Economics", "Management", "Engineering"],
  "Diploma": ["Computer Applications", "Web Development", "Mechanical Engineering", "Electrical Engineering", "Civil Engineering", "Electronics"],
  "Associate Degree": ["Computer Science", "Business Administration", "Healthcare", "Liberal Arts", "Engineering Technology"],
  "Certification": ["Data Science", "Cloud Computing", "Cybersecurity", "Digital Marketing", "Project Management", "Machine Learning", "Web Development"]
};

// Initialize cascading dropdown on DOM ready
document.addEventListener('DOMContentLoaded', function() {
  const programTypeSelect = document.getElementById('program_type');
  const domainSelect = document.getElementById('domain');

  if (programTypeSelect && domainSelect) {
    programTypeSelect.addEventListener('change', function() {
      const selectedProgram = this.value;
      
      // Clear existing options
      domainSelect.innerHTML = '';
      
      if (selectedProgram && domainsByProgram[selectedProgram]) {
        // Enable the dropdown and populate with relevant domains
        domainSelect.disabled = false;
        
        // Add placeholder
        const placeholder = document.createElement('option');
        placeholder.value = '';
        placeholder.textContent = '-- Select Domain --';
        domainSelect.appendChild(placeholder);
        
        // Add domain options
        domainsByProgram[selectedProgram].forEach(domain => {
          const option = document.createElement('option');
          option.value = domain;
          option.textContent = domain;
          domainSelect.appendChild(option);
        });
      } else {
        // Disable and reset if no program selected
        domainSelect.disabled = true;
        const placeholder = document.createElement('option');
        placeholder.value = '';
        placeholder.textContent = '-- First, select Program Type --';
        domainSelect.appendChild(placeholder);
      }
    });
  }
});

// ==========================================
// Handle form submission
// ==========================================
const form = document.getElementById('curriculumForm');
const backButton = document.getElementById('backButton');
const inputSection = document.getElementById('inputSection');
const resultSection = document.getElementById('resultSection');

if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
  
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);
    data.duration_semesters = parseInt(data.duration_semesters);
  
    // UI Elements
    const previewPanel = document.getElementById('previewPanel');
    const placeholderText = document.getElementById('placeholderText');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const previewContent = document.getElementById('previewContent');

    // 1. Switch View to Result
    if (inputSection) inputSection.style.display = 'none';
    if (resultSection) resultSection.style.display = 'block';

    // 2. Show Loading
    if (placeholderText) placeholderText.style.display = 'none';
    if (previewContent) previewContent.style.display = 'none';
    if (loadingIndicator) loadingIndicator.style.display = 'flex';
  
    try {
      const response = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
  
      if (!response.ok) {
        throw new Error('Failed to generate curriculum');
      }
  
      const result = await response.json();
      renderPreview(result);
    } catch (error) {
      console.error(error);
      if (loadingIndicator) loadingIndicator.style.display = 'none';
      
      // Error State
      previewPanel.innerHTML = `
        <button id="backButtonError" class="btn-secondary" style="margin-bottom: 2rem;">
            <i class="fas fa-arrow-left"></i> Back to Editor
        </button>
        <div class="placeholder-text">
          <i class="fas fa-exclamation-triangle" style="color:#ef4444;"></i>
          <p>Error: ${error.message}. Please try again.</p>
        </div>
      `;
      // Re-attach back button event since we wiped innerHTML
      document.getElementById('backButtonError').addEventListener('click', () => {
         window.location.reload(); // Simple reset for error state
      });
    }
  });
}

// Handle Back Button
if (backButton) {
  backButton.addEventListener('click', () => {
    // Switch View to Input
    if (resultSection) resultSection.style.display = 'none';
    if (inputSection) inputSection.style.display = 'block'; // Or 'block'/'flex' depending on layout
    // Optional: Scroll to top
    window.scrollTo(0, 0);
  });
}

function renderPreview(result) {
  const previewContent = document.getElementById('previewContent');
  const previewTitle = document.getElementById('previewTitle');
  const previewCourses = document.getElementById('previewCourses');
  const loadingIndicator = document.getElementById('loadingIndicator');

  if (loadingIndicator) loadingIndicator.style.display = 'none';

  if (!previewTitle || !previewCourses || !previewContent) {
    console.error("Critical DOM elements missing!");
    return;
  }

  previewTitle.textContent = result.program_title;

  // Add Program Rationale and Target Careers at the top
  let overviewHTML = `
    <div class="card rationale-card" style="margin-bottom: 2.5rem; border-top: 5px solid #6366f1;">
      <h2 style="font-size: 1.5rem; margin-bottom: 1rem;"><i class="fas fa-bullseye"></i> Program Rationale</h2>
      <p style="color: #475569; font-size: 1.1rem; line-height: 1.7; margin-bottom: 1.5rem;">${result.program_rationale}</p>
      
      <div class="career-paths">
        <strong style="display: block; margin-bottom: 0.75rem; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; color: #64748b;">Target Career Paths:</strong>
        <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
          ${result.target_careers.map(career => `<span class="topic-chip" style="background: #eef2ff; color: #4338ca; border: 1px solid #c7d2fe; font-weight: 700; padding: 0.5rem 1rem;">${career}</span>`).join('')}
        </div>
      </div>
    </div>
  `;

  let coursesHTML = overviewHTML;
  for (const [semester, courses] of Object.entries(result.courses_by_semester)) {
    coursesHTML += `
      <div class="semester-section">
        <div class="semester-header">
          <div class="semester-title">
            <i class="fas fa-graduation-cap"></i> ${semester}
          </div>
          <span class="course-count">${courses.length} Courses</span>
        </div>
        
        <div class="course-grid">
          ${courses.map(course => `
            <div class="course-card">
              <div class="card-header">
                <div>
                  <h3 style="margin-bottom: 0.25rem;">${course.course_name}</h3>
                  <span style="font-size: 0.8rem; font-weight: 800; color: #6366f1; text-transform: uppercase; letter-spacing: 0.5px;">${course.category}</span>
                </div>
                <span class="course-badge">${course.course_code}</span>
              </div>
              
              <div class="card-meta">
                <span><i class="fas fa-layer-group"></i> ${course.credits} Credits</span>
                <span><i class="far fa-clock"></i> 3h/week</span>
              </div>
              
              <p class="card-description">
                ${course.description}
              </p>
              
              <div class="topics-section">
                <strong>Course Roadmap (${course.weekly_topics.length} Weeks):</strong>
                <div class="topics-list">
                  ${course.weekly_topics.map(t =>
                    `<span class="topic-chip" title="${t.description}">W${t.week}: ${t.title}</span>`
                  ).join('')}
                </div>
              </div>

              <div class="outcomes-section" style="margin-top: 1rem; border-top: 1px dashed #e2e8f0; padding-top: 1rem;">
                <strong style="font-size: 0.85rem; color: #475569;">Learning Outcomes:</strong>
                <ul style="padding-left: 1.25rem; font-size: 0.85rem; color: #64748b; margin-top: 0.5rem;">
                   ${course.outcomes.map(o => `<li>${o.outcome}</li>`).join('')}
                </ul>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }
  previewCourses.innerHTML = coursesHTML;

  // Add Alignment Notes and Optimization Tips
  let extrasHTML = `
    <div class="card" style="margin-top: 2rem; border-left: 5px solid #10b981;">
      <h3 style="margin-bottom: 0.75rem;"><i class="fas fa-info-circle"></i> Industry Alignment & Validation</h3>
      <p style="color: #475569;">${result.industry_alignment_notes}</p>
    </div>
    
    <div class="card" style="margin-top: 1.5rem; border-left: 5px solid #f59e0b;">
      <h3 style="margin-bottom: 0.75rem;"><i class="fas fa-lightbulb"></i> Optimization Tips</h3>
      <ul style="padding-left: 1.5rem; color: #64748b; font-size: 0.95rem;">
        ${result.optimization_tips.map(tip => `<li style="margin-bottom: 0.5rem;">${tip}</li>`).join('')}
      </ul>
    </div>
  `;
  previewCourses.insertAdjacentHTML('beforeend', extrasHTML);

  previewContent.style.display = 'block';
  // Check for placeholder text just in case it wasn't hidden (e.g. if we skip the loading block logic above for some reason)
  const placeholderText = document.querySelector('.placeholder-text');
  if (placeholderText && placeholderText.id !== 'loadingIndicator') {
    placeholderText.style.display = 'none';
  }
}

function downloadPDF() {
  window.print();
}