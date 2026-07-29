content = open('new-ui-ux-frontend/app.js', 'r', encoding='utf-8').read()
idx = content.find('const downloadPdfBtn =')
if idx != -1:
    content = content[:idx] + '''const downloadPdfBtn = document.getElementById('download-pdf-btn');
if (downloadPdfBtn) {
  downloadPdfBtn.addEventListener('click', () => {
    const handleElem = document.getElementById('profile-handle');
    let handle = handleElem ? handleElem.textContent.replace('@', '').trim() : '';
    if (handle && handle !== 'username') {
      window.open('pdf-template.html?handle=' + encodeURIComponent(handle), '_blank');
    } else {
      alert('Please run an audit first.');
    }
  });
}'''
    open('new-ui-ux-frontend/app.js', 'w', encoding='utf-8').write(content)
