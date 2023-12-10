function loadPage(pageName) {
    const mainContent = document.getElementById('main-content');
    fetch(pageName)
      .then(response => response.text())
      .then(html => {
        mainContent.innerHTML = html;
      })
      .catch(error => console.error('Error:', error));
  }