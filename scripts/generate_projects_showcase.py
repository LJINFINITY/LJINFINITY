import html

def generate_projects_svg():
    width = 900
    height = 236
    
    projects = [
        {
            "id": "01",
            "name": "URIEL AI ASSISTANT",
            "tag": "AUTONOMOUS AGENT ORCHESTRATOR",
            "desc_lines": [
                "Self-correcting personal AI assistant",
                "equipped with multi-agent orchestration,",
                "tool reasoning loops & persistent memory."
            ],
            "stack": ["Python", "Multi-Agent", "PyTorch"],
            "color": "#00F0FF",
            "status": "PRODUCTION",
            "status_color": "#10B981"
        },
        {
            "id": "02",
            "name": "ENOCH SHELL (MYSHELL)",
            "tag": "BESPOKE LINUX DESKTOP RIG",
            "desc_lines": [
                "Feature-rich custom desktop environment",
                "built from scratch with Quickshell to my",
                "exact ergonomic workflow & aesthetic."
            ],
            "stack": ["Quickshell", "QML", "Lua", "Hyprland"],
            "color": "#C084FC",
            "status": "DAILY RIG",
            "status_color": "#A855F7"
        },
        {
            "id": "03",
            "name": "ARC TRACKER",
            "tag": "LIFE ARCS & MILESTONES",
            "desc_lines": [
                "Personal life tracking & reflection engine",
                "to monitor lifelong milestone arcs,",
                "project journals & developer telemetry."
            ],
            "stack": ["Python", "SQLite", "Analytics"],
            "color": "#34D399",
            "status": "STABLE",
            "status_color": "#38BDF8"
        }
    ]

    card_w = 280
    gap = 16
    start_x = 16

    cards_svg = ""
    for idx, p in enumerate(projects):
        cx = start_x + idx * (card_w + gap)
        
        stack_pills = ""
        pill_x = 16
        for tech in p["stack"]:
            tw = len(tech) * 7 + 16
            stack_pills += f'''
        <rect x="{pill_x}" y="148" width="{tw}" height="20" rx="4" fill="#161B22" stroke="#30363D" stroke-width="1"/>
        <text x="{pill_x + tw//2}" y="162" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#E2E8F0">{tech}</text>'''
            pill_x += tw + 8

        desc_svg = ""
        for line_idx, line in enumerate(p["desc_lines"]):
            escaped_line = html.escape(line)
            desc_svg += f'''<text x="16" y="{86 + line_idx * 16}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" fill="#94A3B8">{escaped_line}</text>\n'''

        cards_svg += f'''
    <g transform="translate({cx}, 16)">
      <!-- Card Body -->
      <rect width="{card_w}" height="204" rx="10" fill="#0D1117" stroke="#21262D" stroke-width="1.2"/>
      
      <!-- Top Colored Accent Bar -->
      <path d="M 0 10 C 0 4.477 4.477 0 10 0 L {card_w-10} 0 C {card_w-4.477} 0 {card_w} 4.477 {card_w} 10 L {card_w} 14 L 0 14 Z" fill="{p["color"]}" opacity="0.85"/>

      <!-- Corner Brackets -->
      <path d="M 8 26 L 8 18 L 16 18" stroke="{p["color"]}" stroke-width="1.5" fill="none" />
      <path d="M {card_w-8} 26 L {card_w-8} 18 L {card_w-16} 18" stroke="{p["color"]}" stroke-width="1.5" fill="none" />
      <path d="M 8 188 L 8 196 L 16 196" stroke="{p["color"]}" stroke-width="1.5" fill="none" />
      <path d="M {card_w-8} 188 L {card_w-8} 196 L {card_w-16} 196" stroke="{p["color"]}" stroke-width="1.5" fill="none" />

      <!-- Title & ID -->
      <text x="16" y="38" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="800" fill="#F0F6FC" letter-spacing="0.5px">[{p["id"]}] {html.escape(p["name"])}</text>
      <text x="16" y="54" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="{p["color"]}" letter-spacing="1px">// {html.escape(p["tag"])}</text>

      <!-- Divider -->
      <line x1="16" y1="64" x2="{card_w-16}" y2="64" stroke="#21262D" stroke-width="1"/>

      <!-- Description lines -->
      {desc_svg}

      <!-- Stack Pills -->
      {stack_pills}

      <!-- Status Footer -->
      <g transform="translate(16, 188)">
        <circle cx="4" cy="4" r="3.5" fill="{p["status_color"]}"/>
        <text x="14" y="7.5" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="{p["status_color"]}">{p["status"]}</text>
        <text x="{card_w-32}" y="7.5" text-anchor="end" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600" fill="#64748B">ACTIVE REPO ↗</text>
      </g>
    </g>'''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@600;700;800&amp;display=swap');
    </style>
  </defs>

  <!-- Container Box -->
  <rect width="{width}" height="{height}" rx="12" fill="#0A0E14" stroke="#21262D" stroke-width="1"/>

  {cards_svg}
</svg>'''

    with open("/home/lj/Projects/gitreadme/assets/projects_showcase.svg", "w") as f:
        f.write(svg)
    print("Generated /home/lj/Projects/gitreadme/assets/projects_showcase.svg successfully!")

if __name__ == "__main__":
    generate_projects_svg()
