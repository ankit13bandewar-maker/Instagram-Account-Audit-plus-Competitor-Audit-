import re
import html
import base64

def build_payload(html_path, css_path, js_path, logo_path, out_path, default_palette="light"):
    # Read HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Load and Base64 embed logo
    try:
        with open(logo_path, 'rb') as f:
            logo_b64 = base64.b64encode(f.read()).decode('utf-8')
            logo_data_url = f"data:image/png;base64,{logo_b64}"
    except Exception as e:
        print(f"Warning loading logo: {e}")
        logo_data_url = "Bloomxlogo.png"

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html_content, re.DOTALL | re.IGNORECASE)
    if body_match:
        body_inner = body_match.group(1)
        # remove scripts from the extracted body if they are there
        body_inner = re.sub(r'<script.*?>.*?</script>', '', body_inner, flags=re.DOTALL | re.IGNORECASE)
    else:
        body_inner = html_content # fallback
        
    # Replace relative logo image source with embedded base64 data URL
    body_inner = body_inner.replace('src="Bloomxlogo.png"', f'src="{logo_data_url}"')

    # Read CSS
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
        
    # Remove the basic encapsulation since we are using an iframe
    css_content = css_content.replace('body {', 'body { margin: 0; padding: 0; ')
    
    # Read JS
    with open(js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
        
    # Add iframe auto-resizer to the JS payload
    iframe_resizer_js = """
// IFRAME RESIZER LOGIC
document.addEventListener("DOMContentLoaded", function() {
    const observer = new ResizeObserver(() => {
        window.parent.postMessage({ type: 'audit-resize', height: document.documentElement.scrollHeight + 20 }, '*');
    });
    observer.observe(document.body);
    
    // Also trigger on click/interactions just in case
    document.body.addEventListener("click", () => {
        setTimeout(() => {
            window.parent.postMessage({ type: 'audit-resize', height: document.documentElement.scrollHeight + 20 }, '*');
        }, 100);
    });
});
"""
    js_content += "\n" + iframe_resizer_js
                 
    # Assemble inner HTML for the iframe
    inner_html = f"""<!DOCTYPE html>
<html lang="en" data-palette="{default_palette}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
{css_content}
</style>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="audit-dashboard-root-wrapper" style="background: var(--bg, #EFF0F3); color: var(--text, #13141A); margin: 0; padding: 0; overflow-x: hidden;">
{body_inner}
<script>
{js_content}
</script>
</body>
</html>
"""
    
    # Escape the inner HTML for the srcdoc attribute
    escaped_inner_html = html.escape(inner_html)
    
    # Assemble the final WordPress widget wrapper
    final_output = f"""
<!-- 
  ==============================================================
  INSTAGRAM AUDIT DASHBOARD - WORDPRESS/ELEMENTOR READY PAYLOAD
  100% Isolated from Theme CSS via Auto-Resizing Iframe
  ==============================================================
-->

<div id="bloomx-audit-widget-container" style="width: 100%; min-height: 800px; display: block; overflow: hidden; background: transparent;">
  
  <!-- Loading Placeholder -->
  <div id="bloomx-audit-loader" style="text-align: center; padding: 40px; font-family: sans-serif; color: #6b7280;">
    <div style="display: inline-block; width: 40px; height: 40px; border: 3px solid #e5e7eb; border-top-color: #3b82f6; border-radius: 50%; animation: bloomx-spin 1s linear infinite;"></div>
    <div style="margin-top: 16px; font-weight: 500;">Loading Audit Tool...</div>
  </div>
  
  <!-- Isolated iframe payload -->
  <iframe 
    id="bloomx-audit-iframe"
    sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox allow-forms allow-top-navigation-by-user-activation"
    style="width: 100%; height: 800px; border: none; overflow: hidden; display: none;" 
    scrolling="no"
    srcdoc="{escaped_inner_html}">
  </iframe>
</div>

<style>
@keyframes bloomx-spin {{ to {{ transform: rotate(360deg); }} }}
</style>

<script>
// Host page listener for iframe auto-resizing
window.addEventListener('message', function(e) {{
    if (e.data && e.data.type === 'audit-resize') {{
        var iframe = document.getElementById('bloomx-audit-iframe');
        if (iframe) {{
            iframe.style.height = e.data.height + 'px';
        }}
    }}
}});

// Show iframe after slight delay to ensure scripts are initialized
setTimeout(function() {{
    document.getElementById('bloomx-audit-loader').style.display = 'none';
    document.getElementById('bloomx-audit-iframe').style.display = 'block';
}}, 500);
</script>
"""

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
        
    print(f"Compilation successful: {out_path}")

def main():
    css_path = 'new-ui-ux-frontend/style.css'
    js_path = 'new-ui-ux-frontend/app.js'
    logo_path = 'new-ui-ux-frontend/Bloomxlogo.png'

    # Build Standard
    build_payload(
        html_path='new-ui-ux-frontend/index.html',
        css_path=css_path,
import re
import html
import base64

def build_payload(html_path, css_path, js_path, logo_path, out_path, default_palette="light"):
    # Read HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Load and Base64 embed logo
    try:
        with open(logo_path, 'rb') as f:
            logo_b64 = base64.b64encode(f.read()).decode('utf-8')
            logo_data_url = f"data:image/png;base64,{logo_b64}"
    except Exception as e:
        print(f"Warning loading logo: {e}")
        logo_data_url = "Bloomxlogo.png"

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html_content, re.DOTALL | re.IGNORECASE)
    if body_match:
        body_inner = body_match.group(1)
        # remove scripts from the extracted body if they are there
        body_inner = re.sub(r'<script.*?>.*?</script>', '', body_inner, flags=re.DOTALL | re.IGNORECASE)
    else:
        body_inner = html_content # fallback
        
    # Replace relative logo image source with embedded base64 data URL
    body_inner = body_inner.replace('src="Bloomxlogo.png"', f'src="{logo_data_url}"')

    # Read CSS
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
        
    # Remove the basic encapsulation since we are using an iframe
    css_content = css_content.replace('body {', 'body { margin: 0; padding: 0; ')
    
    # Read JS
    with open(js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
        
    # Add iframe auto-resizer to the JS payload
    iframe_resizer_js = """
// IFRAME RESIZER LOGIC
document.addEventListener("DOMContentLoaded", function() {
    const observer = new ResizeObserver(() => {
        window.parent.postMessage({ type: 'audit-resize', height: document.documentElement.scrollHeight + 20 }, '*');
    });
    observer.observe(document.body);
    
    // Also trigger on click/interactions just in case
    document.body.addEventListener("click", () => {
        setTimeout(() => {
            window.parent.postMessage({ type: 'audit-resize', height: document.documentElement.scrollHeight + 20 }, '*');
        }, 100);
    });
});
"""
    js_content += "\n" + iframe_resizer_js
                 
    # Assemble inner HTML for the iframe
    inner_html = f"""<!DOCTYPE html>
<html lang="en" data-palette="{default_palette}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
{css_content}
</style>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="audit-dashboard-root-wrapper" style="background: var(--bg, #EFF0F3); color: var(--text, #13141A); margin: 0; padding: 0; overflow-x: hidden;">
{body_inner}
<script>
{js_content}
</script>
</body>
</html>
"""
    
    # Escape the inner HTML for the srcdoc attribute
    escaped_inner_html = html.escape(inner_html)
    
    # Assemble the final WordPress widget wrapper
    final_output = f"""
<!-- 
  ==============================================================
  INSTAGRAM AUDIT DASHBOARD - WORDPRESS/ELEMENTOR READY PAYLOAD
  100% Isolated from Theme CSS via Auto-Resizing Iframe
  ==============================================================
-->

<div id="bloomx-audit-widget-container" style="width: 100%; min-height: 800px; display: block; overflow: hidden; background: transparent;">
  
  <!-- Loading Placeholder -->
  <div id="bloomx-audit-loader" style="text-align: center; padding: 40px; font-family: sans-serif; color: #6b7280;">
    <div style="display: inline-block; width: 40px; height: 40px; border: 3px solid #e5e7eb; border-top-color: #3b82f6; border-radius: 50%; animation: bloomx-spin 1s linear infinite;"></div>
    <div style="margin-top: 16px; font-weight: 500;">Loading Audit Tool...</div>
  </div>
  
  <!-- Isolated iframe payload -->
  <iframe 
    id="bloomx-audit-iframe"
    sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox allow-forms allow-top-navigation-by-user-activation"
    style="width: 100%; height: 800px; border: none; overflow: hidden; display: none;" 
    scrolling="no"
    srcdoc="{escaped_inner_html}">
  </iframe>
</div>

<style>
@keyframes bloomx-spin {{ to {{ transform: rotate(360deg); }} }}
</style>

<script>
// Host page listener for iframe auto-resizing
window.addEventListener('message', function(e) {{
    if (e.data && e.data.type === 'audit-resize') {{
        var iframe = document.getElementById('bloomx-audit-iframe');
        if (iframe) {{
            iframe.style.height = e.data.height + 'px';
        }}
    }}
}});

// Show iframe after slight delay to ensure scripts are initialized
setTimeout(function() {{
    document.getElementById('bloomx-audit-loader').style.display = 'none';
    document.getElementById('bloomx-audit-iframe').style.display = 'block';
}}, 500);
</script>
"""

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
        
    print(f"Compilation successful: {out_path}")

def main():
    css_path = 'new-ui-ux-frontend/style.css'
    js_path = 'new-ui-ux-frontend/app.js'
    logo_path = 'new-ui-ux-frontend/Bloomxlogo.png'

    # Build Standard
    build_payload(
        html_path='new-ui-ux-frontend/index.html',
        css_path=css_path,
        js_path=js_path,
        logo_path=logo_path,
        out_path='final-wordpress-code.html',
        default_palette="light"
    )

    # Build Pro
    build_payload(
        html_path='new-ui-ux-frontend/index-pro.html',
        css_path=css_path,
        js_path=js_path,
        logo_path=logo_path,
        out_path='final-wordpress-code-pro.html',
        default_palette="light"
    )

if __name__ == '__main__':
    main()
