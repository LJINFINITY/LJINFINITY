import os

skills = [
    # Row 1
    ("Rust", "#000000", "#FFF"), ("C++", "#00599C", "#FFF"), ("Python", "#3776AB", "#FFF"), ("TypeScript", "#3178C6", "#FFF"), ("JavaScript", "#F7DF1E", "#000"), ("Go", "#00ADD8", "#FFF"), ("Java", "#ED8B00", "#FFF"),
    # Row 2
    ("PyTorch", "#EE4C2C", "#FFF"), ("TensorFlow", "#FF6F00", "#FFF"), ("OpenCV", "#5C3EE8", "#FFF"), ("Hugging Face", "#FFD21E", "#000"), ("Vercel AI", "#000000", "#FFF"), ("LangChain", "#1C3C3C", "#FFF"), ("CUDA", "#76B900", "#000"),
    # Row 3
    ("React", "#61DAFB", "#000"), ("Next.js", "#000000", "#FFF"), ("Vite", "#646CFF", "#FFF"), ("Vue.js", "#4FC08D", "#FFF"), ("Tailwind", "#06B6D4", "#FFF"), ("Expo", "#000000", "#FFF"), ("Redux", "#764ABC", "#FFF"),
    # Row 4
    ("Linux", "#FCC624", "#000"), ("Quickshell", "#2E3440", "#FFF"), ("QML", "#41CD52", "#FFF"), ("Lua", "#2C2D72", "#FFF"), ("Bash", "#4EAA25", "#FFF"), ("Arch Linux", "#1793D1", "#FFF"), ("Fedora", "#51A2DA", "#FFF"),
    # Row 5
    ("Node.js", "#339933", "#FFF"), ("Express", "#000000", "#FFF"), ("FastAPI", "#009688", "#FFF"), ("GraphQL", "#E10098", "#FFF"), ("REST API", "#02569B", "#FFF"), ("WebSockets", "#010101", "#FFF"), ("Micro", "#000000", "#FFF"),
    # Row 6
    ("PostgreSQL", "#4169E1", "#FFF"), ("Redis", "#DC382D", "#FFF"), ("SQLite", "#003B57", "#FFF"), ("Supabase", "#3ECF8E", "#FFF"), ("Firebase", "#FFCA28", "#000"), ("MongoDB", "#47A248", "#FFF"), ("Neo4j", "#008CC1", "#FFF"),
    # Row 7
    ("Docker", "#2496ED", "#FFF"), ("Kubernetes", "#326CE5", "#FFF"), ("Git", "#F05032", "#FFF"), ("GitHub Actions", "#2088FF", "#FFF"), ("AWS", "#232F3E", "#FFF"), ("Vercel", "#000000", "#FFF"), ("Cloudflare", "#F38020", "#FFF"),
    # Row 8
    ("Neovim", "#57A143", "#FFF"), ("VS Code", "#007ACC", "#FFF"), ("Hyprland", "#00A6A6", "#FFF"), ("Wayland", "#000000", "#FFF"), ("Zsh", "#F1502F", "#FFF"), ("Tmux", "#1BB91F", "#FFF"), ("Figma", "#F24E1E", "#FFF"),
    # Row 9
    ("Swift", "#F05138", "#FFF"), ("Kotlin", "#7F52FF", "#FFF"), ("Assembly", "#6E4C13", "#FFF"), ("Ollama", "#000000", "#FFF"), ("NumPy", "#013243", "#FFF"), ("Pandas", "#150458", "#FFF"), ("Scikit-Learn", "#F7931E", "#FFF")
]

def generate_svg():
    cols = 7
    badge_w, badge_h = 115, 36
    gap_x, gap_y = 12, 12
    padding_x, padding_y = 15, 20

    total_w = cols * badge_w + (cols - 1) * gap_x + padding_x * 2
    rows = (len(skills) + cols - 1) // cols
    total_h = rows * badge_h + (rows - 1) * gap_y + padding_y * 2

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="{total_h}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&amp;display=swap');

      .skill-pill {{
        font-family: 'Share Tech Mono', monospace, sans-serif;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
      }}

      @keyframes floatAnim {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-7px); }}
        100% {{ transform: translateY(0px); }}
      }}

      .float-group {{
        animation: floatAnim 4s ease-in-out infinite;
      }}

      .badge-bg {{
        rx: 8px;
        ry: 8px;
        stroke: rgba(255, 255, 255, 0.15);
        stroke-width: 1px;
      }}
    </style>
  </defs>

'''

    for i, (name, bg, fg) in enumerate(skills):
        r = i // cols
        c = i % cols
        x = padding_x + c * (badge_w + gap_x)
        y = padding_y + r * (badge_h + gap_y)
        
        # Staggered floating delay for smooth undulating wave effect
        delay = round((c * 0.3 + r * 0.4) % 3.0, 2)
        
        center_x = x + badge_w // 2
        center_y = y + badge_h // 2 + 4

        svg_content += f'''  <g class="float-group" style="animation-delay: {delay}s;">
    <rect x="{x}" y="{y}" width="{badge_w}" height="{badge_h}" fill="{bg}" class="badge-bg" />
    <text x="{center_x}" y="{center_y}" fill="{fg}" text-anchor="middle" class="skill-pill">{name}</text>
  </g>
'''

    svg_content += "</svg>\n"

    output_path = "/home/lj/Work/Me/tech_stack_wall.svg"
    with open(output_path, "w") as f:
        f.write(svg_content)
    print(f"Successfully generated massive floating tech_stack_wall.svg at {output_path}!")

if __name__ == "__main__":
    generate_svg()
