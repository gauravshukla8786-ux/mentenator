function sendMessage() {
  let userInput = document.getElementById('user-input');
  let message = userInput.value.trim();
  if (!message) return;

  let chatBox = document.getElementById('chat-box');
  chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;

  // ✅ Fixed: Use GET request matching the Flask route
  fetch('/get?msg=' + encodeURIComponent(message))
    .then(res => res.text())
    .then(response => {
      chatBox.innerHTML += `<p><strong>Bot:</strong> ${response}</p>`;
      chatBox.scrollTop = chatBox.scrollHeight;
      userInput.value = '';
    });
}
