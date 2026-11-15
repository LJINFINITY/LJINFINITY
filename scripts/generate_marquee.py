import html

row1_items = [
    ("Rust", "#DEA584"),
    ("C++", "#F34B7D"),
    ("Python", "#3572A5"),
    ("TypeScript", "#3178C6"),
    ("Go", "#00ADD8"),
    ("PyTorch", "#EE4C2C"),
    ("LangChain", "#1C3C3C"),
    ("CUDA", "#76B900"),
    ("Hugging Face", "#FFD21E"),
    ("OpenCV", "#5C3EE8"),
    ("Linux", "#FCC624"),
    ("Hyprland", "#00A6A6"),
    ("Quickshell", "#5E81AC"),
    ("Neovim", "#57A143"),
    ("Bash", "#89E051"),
    ("DeepSeek", "#4D6BFE"),
    ("Anthropic", "#D97757"),
    ("OpenAI", "#10A37F")
]

row2_items = [
    ("React", "#61DAFB"),
    ("Next.js", "#FFFFFF"),
    ("Tailwind CSS", "#38BDF8"),
    ("Node.js", "#5FA04E"),
    ("FastAPI", "#059669"),
    ("PostgreSQL", "#336791"),
    ("Redis", "#DC382D"),
    ("Docker", "#2496ED"),
    ("Kubernetes", "#326CE5"),
    ("SQLite", "#003B57"),
    ("Supabase", "#3ECF8E"),
    ("GraphQL", "#E10098"),
    ("AWS", "#FF9900"),
    ("Git", "#F05032"),
    ("Tmux", "#1BB91F"),
    ("Kitty", "#FF6B6B"),
    ("Starship", "#DD4B39"),
    ("RTK", "#F43F5E")
]

def build_row_svg(items, y_offset, anim_name, direction, duration="35s"):
    pill_h = 36
    pill_padding = 14
    total_w = 0
    pills = []
    
    for name, color in items:
        # approximate width based on text
        text_len = len(name)
        w = max(90, text_len * 9 + 48)
        pills.append((name, color, w, total_w))
        total_w += w + pill_padding
        
    # We duplicate pills so loop is 100% seamless
    # Total width of one sequence is total_w
    # Animation moves from 0 to -total_w (left) or -total_w to 0 (right)
    
    group_content = ""
    for cycle in [0, 1]:
        cycle_x = cycle * total_w
        for name, color, w, x in pills:
            px = cycle_x + x
            group_content += f'''
      <g transform="translate({px}, 0)">
        <rect width="{w}" height="{pill_h}" rx="8" fill="#161B22" stroke="#30363D" stroke-width="1.2"/>
        <circle cx="18" cy="18" r="5" fill="{color}"/>
        <text x="32" y="23" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="13" font-weight="600" fill="#E6EDF3">{html.escape(name)}</text>
      </g>'''
            
    if direction == "left":
        keyframes = f'''
    @keyframes {anim_name} {{
      0%   {{ transform: translateX(0px); }}
      100% {{ transform: translateX(-{total_w}px); }}
    }}'''
    else:
        keyframes = f'''
    @keyframes {anim_name} {{
      0%   {{ transform: translateX(-{total_w}px); }}
      100% {{ transform: translateX(0px); }}
    }}'''
        
    row_markup = f'''
    <g transform="translate(0, {y_offset})">
      <g style="animation: {anim_name} {duration} linear infinite;">
        {group_content}
      </g>
    </g>'''
    
    return keyframes, row_markup, total_w

kf1, row1_svg, w1 = build_row_svg(row1_items, 10, "slideLeft", "left", "30s")
kf2, row2_svg, w2 = build_row_svg(row2_items, 56, "slideRight", "right", "34s")

svg_template = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 106" width="100%" height="106">
  <defs>
    <style>
      {kf1}
      {kf2}
    </style>
    
    <!-- Linear Gradients for Edge Fading -->
    <linearGradient id="fadeLeft" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0D1117" stop-opacity="1" />
      <stop offset="100%" stop-color="#0D1117" stop-opacity="0" />
    </linearGradient>
    <linearGradient id="fadeRight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0D1117" stop-opacity="0" />
      <stop offset="100%" stop-color="#0D1117" stop-opacity="1" />
    </linearGradient>
  </defs>

  <!-- Dark Background -->
  <rect width="850" height="106" fill="#0D1117" rx="12" stroke="#30363D" stroke-width="1"/>

  <!-- Clipping mask viewport -->
  <g clip-path="url(#marqueeClip)">
    <clipPath id="marqueeClip">
      <rect x="2" y="2" width="846" height="102" rx="10"/>
    </clipPath>
    
    {row1_svg}
    {row2_svg}
  </g>

  <!-- Left and Right Subtle Fade Overlays -->
  <rect x="2" y="2" width="70" height="102" fill="url(#fadeLeft)" pointer-events="none"/>
  <rect x="778" y="2" width="70" height="102" fill="url(#fadeRight)" pointer-events="none"/>
</svg>'''

with open("/home/lj/Projects/gitreadme/assets/marquee_stack.svg", "w") as f:
    f.write(svg_template)

print("Generated /home/lj/Projects/gitreadme/assets/marquee_stack.svg successfully!")
