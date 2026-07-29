import re
with open('new-ui-ux-frontend/pdf-template.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\\`', '`')
content = content.replace('\\${', '${')
content = content.replace('?', '•') # also fix that weird character

with open('new-ui-ux-frontend/pdf-template.html', 'w', encoding='utf-8') as f:
    f.write(content)
