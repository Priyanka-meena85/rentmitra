# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Leaflet CSS and JS in <head>
leaflet_head = """  <!-- Leaflet Interactive Maps -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>
  <link rel="manifest" href="/manifest.json" />
"""

if 'leaflet.css' not in html:
    html = html.replace('</head>', leaflet_head + '\n</head>')

# 2. Add Leaflet price pin styling in <style>
custom_styles = """
    /* Leaflet Price Pin Badge */
    .leaflet-price-pin {
      background: #1C1917;
      color: #FDE68A;
      font-family: 'Fraunces', serif;
      font-weight: 800;
      font-size: 11px;
      padding: 4px 10px;
      border-radius: 9999px;
      border: 1.5px solid #C2410C;
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .leaflet-price-pin:hover {
      background: #C2410C;
      color: #FFFFFF;
      transform: scale(1.1);
    }
    /* Comparison Floating Bar */
    .compare-bar-enter {
      animation: slideUpCompare 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes slideUpCompare {
      from { transform: translateY(100%); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
"""

if '.leaflet-price-pin' not in html:
    html = html.replace('</style>', custom_styles + '\n</style>')

print("Step 1: Head & Styles prepared")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
