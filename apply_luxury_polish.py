import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Enhance aesthetic styling in <style> block
old_style_target = '''    body {
      background-color: #FFFBF5;
      color: #1C1917;
      font-family: 'Outfit', sans-serif;
      overflow-x: hidden;
    }'''

new_style_replacement = '''    body {
      background-color: #FFFBF5;
      color: #1C1917;
      font-family: 'Outfit', sans-serif;
      overflow-x: hidden;
      letter-spacing: -0.01em;
    }

    /* Subtle luxury mesh ambient background */
    body::before {
      content: "";
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at 15% 15%, rgba(254, 243, 199, 0.45) 0%, transparent 40%),
                  radial-gradient(circle at 85% 25%, rgba(255, 237, 213, 0.4) 0%, transparent 45%),
                  radial-gradient(circle at 50% 85%, rgba(254, 243, 199, 0.3) 0%, transparent 50%);
      pointer-events: none;
      z-index: -10;
    }

    /* Smooth focus rings & transitions */
    input:focus, select:focus, textarea:focus {
      outline: none;
      box-shadow: 0 0 0 3px rgba(194, 65, 12, 0.18);
      border-color: #C2410C !important;
    }

    /* Button active tactile feel */
    button, a {
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    button:active, a:active {
      transform: scale(0.98);
    }'''

html = html.replace(old_style_target, new_style_replacement, 1)

# Ensure all images have crisp shadow and smooth loading
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Professional styling upgrades added.")
