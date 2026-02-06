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
document.addEventListener('DOMContentLoaded', function () {
  const programTypeSelect = document.getElementById('program_type');
  const domainSelect = document.getElementById('domain');

  if (programTypeSelect && domainSelect) {
    programTypeSelect.addEventListener('change', function () {
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

  // Store curriculum data for flowchart
  storeCurriculumData(result);

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
          ${courses.map((course, idx) => `
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

              <div class="course-actions">
                <button class="btn-syllabus" onclick="generateSyllabus('${course.course_name.replace(/'/g, "\\'")}')">
                  <i class="fas fa-book-open"></i> Syllabus
                </button>
                <button class="btn-resources" onclick="getResources('${course.course_name.replace(/'/g, "\\'")}')">
                  <i class="fas fa-globe"></i> Resources
                </button>
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

// ==========================================
// FLOWCHART VISUALIZATION
// ==========================================
let currentCurriculumData = null;

// Store curriculum data when rendered
function storeCurriculumData(data) {
  currentCurriculumData = data;
}

function showFlowchart() {
  if (!currentCurriculumData) {
    alert('Please generate a curriculum first.');
    return;
  }

  const modal = document.getElementById('flowchartModal');
  const container = document.getElementById('flowchartContainer');

  // Generate Mermaid flowchart code
  const mermaidCode = generateMermaidCode(currentCurriculumData);
  
  // Render the flowchart using mermaid.render
  mermaid.render('flowchartSvg', mermaidCode).then(({ svg }) => {
    container.innerHTML = svg;
    modal.style.display = 'flex';
  }).catch(err => {
    console.error('Mermaid error:', err);
    container.innerHTML = '<p style="color: #ef4444;">Error rendering flowchart. Please try again.</p>';
    modal.style.display = 'flex';
  });
}

function closeFlowchart() {
  const modal = document.getElementById('flowchartModal');
  modal.style.display = 'none';
}

function generateMermaidCode(data) {
  let code = 'graph TD\n';

  // Add program title as root
  const programId = 'P0';
  code += `  ${programId}["🎓 ${data.program_title}"]\n`;

  // Add semesters and courses from courses_by_semester
  const semesters = Object.entries(data.courses_by_semester || {});
  semesters.forEach(([semesterName, courses], semIdx) => {
    const semId = `S${semIdx + 1}`;
    code += `  ${semId}["📚 ${semesterName}"]\n`;
    code += `  ${programId} --> ${semId}\n`;

    // Add courses for each semester
    courses.forEach((course, courseIdx) => {
      const courseId = `C${semIdx}_${courseIdx}`;
      const courseName = course.course_name.length > 25
        ? course.course_name.substring(0, 22) + '...'
        : course.course_name;
      code += `  ${courseId}["${courseName}"]\n`;
      code += `  ${semId} --> ${courseId}\n`;
    });

    // Connect semesters sequentially
    if (semIdx > 0) {
      code += `  S${semIdx} -.-> ${semId}\n`;
    }
  });

  return code;
}

// Close modal on outside click
document.addEventListener('click', function (e) {
  const modal = document.getElementById('flowchartModal');
  const syllabusModal = document.getElementById('syllabusModal');
  if (e.target === modal) {
    closeFlowchart();
  }
  if (e.target === syllabusModal) {
    closeSyllabus();
  }
});

// ==========================================
// SYLLABUS GENERATION
// ==========================================
async function generateSyllabus(courseName) {
  // Get program and domain from stored data
  const program = currentCurriculumData?.program_title || 'Computer Science';
  const domain = currentCurriculumData?.domain || 'Technology';

  // Show modal with loading
  const modal = document.getElementById('syllabusModal');
  const content = document.getElementById('syllabusContent');
  const title = document.getElementById('syllabusTitle');

  title.textContent = courseName;
  content.innerHTML = `
    <div style="text-align: center; padding: 3rem;">
      <i class="fas fa-spinner fa-spin" style="font-size: 2rem; color: #6366f1;"></i>
      <p style="margin-top: 1rem; color: var(--text-muted);">Generating detailed syllabus...</p>
    </div>
  `;
  modal.style.display = 'flex';

  try {
    const response = await fetch('/generate-syllabus', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        course_name: courseName,
        program: program,
        domain: domain
      })
    });

    const data = await response.json();
    content.innerHTML = formatSyllabusMarkdown(data.syllabus);

  } catch (error) {
    content.innerHTML = `<p style="color: #ef4444;">Error generating syllabus. Please try again.</p>`;
  }
}

function closeSyllabus() {
  document.getElementById('syllabusModal').style.display = 'none';
}

function formatSyllabusMarkdown(text) {
  return text
    .replace(/## (.*)/g, '<h3 style="color: #6366f1; margin-top: 1.5rem;">$1</h3>')
    .replace(/### (.*)/g, '<h4 style="margin-top: 1.25rem;">$1</h4>')
    .replace(/#### (.*)/g, '<h5 style="color: var(--text-muted); margin-top: 1rem;">$1</h5>')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n- /g, '<br>• ')
    .replace(/\n\d+\. /g, (match) => '<br>' + match.trim() + ' ')
    .replace(/\n\n/g, '<br><br>')
    .replace(/\n/g, '<br>');
}

function copySyllabus() {
  const text = document.getElementById('syllabusContent').innerText;
  navigator.clipboard.writeText(text).then(() => {
    alert('Syllabus copied to clipboard!');
  });
}

function downloadSyllabus() {
  const text = document.getElementById('syllabusContent').innerText;
  const title = document.getElementById('syllabusTitle').textContent;
  const blob = new Blob([text], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `syllabus-${title.replace(/\s+/g, '-').toLowerCase()}.txt`;
  a.click();
  URL.revokeObjectURL(url);
}

// ==========================================
// RESOURCE HUB
// ==========================================
async function getResources(courseName) {
  const domain = currentCurriculumData?.domain || '';
  
  const modal = document.getElementById('resourceModal');
  const content = document.getElementById('resourceContent');
  const title = document.getElementById('resourceTitle');
  
  title.textContent = courseName;
  content.innerHTML = `
    <div style="text-align: center; padding: 3rem;">
      <i class="fas fa-spinner fa-spin" style="font-size: 2rem; color: #6366f1;"></i>
      <p style="margin-top: 1rem; color: var(--text-muted);">Finding best learning resources...</p>
    </div>
  `;
  modal.style.display = 'flex';
  
  try {
    const response = await fetch('/get-resources', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ course_name: courseName, domain: domain })
    });
    
    const data = await response.json();
    content.innerHTML = renderResources(data);
    
  } catch (error) {
    content.innerHTML = `<p style="color: #ef4444;">Error fetching resources. Please try again.</p>`;
  }
}

function closeResources() {
  document.getElementById('resourceModal').style.display = 'none';
}

function renderResources(data) {
  if (data.error) {
    return `<p style="color: #f59e0b;">⚠️ ${data.error}</p>`;
  }
  
  return `
    <div class="resource-tabs">
      <button class="tab-btn active" onclick="switchTab('moocs')"><i class="fas fa-graduation-cap"></i> MOOCs</button>
      <button class="tab-btn" onclick="switchTab('books')"><i class="fas fa-book"></i> Books</button>
      <button class="tab-btn" onclick="switchTab('youtube')"><i class="fab fa-youtube"></i> YouTube</button>
    </div>
    
    <div id="tab-moocs" class="tab-content active">
      ${data.moocs && data.moocs.length ? data.moocs.map(m => `
        <div class="resource-item">
          <div class="resource-icon mooc"><i class="fas fa-play-circle"></i></div>
          <div class="resource-info">
            <a href="${m.url}" target="_blank" class="resource-title">${m.title}</a>
            <span class="resource-meta"><i class="fas fa-university"></i> ${m.platform} • ${m.instructor || 'Various'}</span>
          </div>
          <a href="${m.url}" target="_blank" class="resource-link"><i class="fas fa-external-link-alt"></i></a>
        </div>
      `).join('') : '<p class="no-resources">No MOOCs found</p>'}
    </div>
    
    <div id="tab-books" class="tab-content">
      ${data.books && data.books.length ? data.books.map(b => `
        <div class="resource-item">
          <div class="resource-icon book"><i class="fas fa-book"></i></div>
          <div class="resource-info">
            <span class="resource-title">${b.title}</span>
            <span class="resource-meta"><i class="fas fa-user"></i> ${b.author} • ${b.edition || ''}</span>
          </div>
        </div>
      `).join('') : '<p class="no-resources">No books found</p>'}
    </div>
    
    <div id="tab-youtube" class="tab-content">
      ${data.youtube && data.youtube.length ? data.youtube.map(y => `
        <div class="resource-item">
          <div class="resource-icon youtube"><i class="fab fa-youtube"></i></div>
          <div class="resource-info">
            <a href="${y.url}" target="_blank" class="resource-title">${y.title}</a>
            <span class="resource-meta"><i class="fas fa-user"></i> ${y.creator} • ${y.videos || ''}</span>
          </div>
          <a href="${y.url}" target="_blank" class="resource-link"><i class="fas fa-external-link-alt"></i></a>
        </div>
      `).join('') : '<p class="no-resources">No playlists found</p>'}
    </div>
  `;
}

function switchTab(tabName) {
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
  
  event.target.closest('.tab-btn').classList.add('active');
  document.getElementById(`tab-${tabName}`).classList.add('active');
}