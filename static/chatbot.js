// Chatbot functionality
document.addEventListener('DOMContentLoaded', function() {
  const chatToggle = document.getElementById('chatToggle');
  const chatWindow = document.getElementById('chatWindow');
  const chatClose = document.getElementById('chatClose');
  const chatInput = document.getElementById('chatInput');
  const chatSend = document.getElementById('chatSend');
  const chatMessages = document.getElementById('chatMessages');

  // Toggle chat window
  chatToggle.addEventListener('click', function() {
    chatWindow.classList.toggle('active');
    if (chatWindow.classList.contains('active')) {
      chatInput.focus();
    }
  });

  chatClose.addEventListener('click', function() {
    chatWindow.classList.remove('active');
  });

  // Send message on Enter
  chatInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  chatSend.addEventListener('click', sendMessage);

  function sendMessage() {
    const message = chatInput.value.trim();
    if (!message) return;

    // Add user message
    addMessage(message, 'user');
    chatInput.value = '';

    // Show typing indicator
    const typingId = showTyping();

    // Send to backend
    fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
      removeTyping(typingId);
      addMessage(data.response, 'bot');
    })
    .catch(err => {
      removeTyping(typingId);
      addMessage('Sorry, I encountered an error. Please try again.', 'bot');
    });
  }

  function addMessage(text, sender) {
    const msg = document.createElement('div');
    msg.className = `chat-message ${sender}`;
    
    if (sender === 'bot') {
      msg.innerHTML = `
        <div class="message-content">${formatMessage(text)}</div>
        <div class="message-actions">
          <button class="action-btn copy-btn" title="Copy">
            <i class="fas fa-copy"></i>
          </button>
          <button class="action-btn download-btn" title="Download">
            <i class="fas fa-download"></i>
          </button>
        </div>
      `;
      
      // Add copy functionality
      const copyBtn = msg.querySelector('.copy-btn');
      copyBtn.addEventListener('click', () => copyText(text, copyBtn));
      
      // Add download functionality
      const downloadBtn = msg.querySelector('.download-btn');
      downloadBtn.addEventListener('click', () => downloadText(text));
    } else {
      msg.innerHTML = `<div class="message-content">${formatMessage(text)}</div>`;
    }
    
    chatMessages.appendChild(msg);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function copyText(text, btn) {
    navigator.clipboard.writeText(text).then(() => {
      btn.innerHTML = '<i class="fas fa-check"></i>';
      btn.classList.add('success');
      setTimeout(() => {
        btn.innerHTML = '<i class="fas fa-copy"></i>';
        btn.classList.remove('success');
      }, 2000);
    });
  }

  function downloadText(text) {
    const blob = new Blob([text], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `currbot-response-${Date.now()}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function formatMessage(text) {
    return text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/\n/g, '<br>')
      .replace(/• /g, '&bull; ');
  }

  function showTyping() {
    const id = 'typing-' + Date.now();
    const typing = document.createElement('div');
    typing.className = 'chat-message bot typing';
    typing.id = id;
    typing.innerHTML = `
      <div class="message-content">
        <span class="dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
      </div>
    `;
    chatMessages.appendChild(typing);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return id;
  }

  function removeTyping(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
  }

  // Add welcome message
  setTimeout(() => {
    addMessage("👋 Hi! I'm CurrBot, your curriculum assistant. How can I help you today?", 'bot');
  }, 500);
});
