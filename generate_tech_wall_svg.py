import os
import random

skills = [
    ("Rust", "#000000", "#FFF"), ("C++", "#00599C", "#FFF"), ("Python", "#3776AB", "#FFF"), ("TypeScript", "#3178C6", "#FFF"), ("JavaScript", "#F7DF1E", "#000"), ("Go", "#00ADD8", "#FFF"), ("Java", "#ED8B00", "#FFF"),
    ("PyTorch", "#EE4C2C", "#FFF"), ("TensorFlow", "#FF6F00", "#FFF"), ("OpenCV", "#5C3EE8", "#FFF"), ("Hugging Face", "#FFD21E", "#000"), ("Vercel AI", "#000000", "#FFF"), ("LangChain", "#1C3C3C", "#FFF"), ("CUDA", "#76B900", "#000"),
    ("React", "#61DAFB", "#000"), ("Next.js", "#000000", "#FFF"), ("Vite", "#646CFF", "#FFF"), ("Vue.js", "#4FC08D", "#FFF"), ("Tailwind", "#06B6D4", "#FFF"), ("Expo", "#000000", "#FFF"), ("Redux", "#764ABC", "#FFF"),
    ("Linux", "#FCC624", "#000"), ("Quickshell", "#2E3440", "#FFF"), ("QML", "#41CD52", "#FFF"), ("Lua", "#2C2D72", "#FFF"), ("Bash", "#4EAA25", "#FFF"), ("Arch Linux", "#1793D1", "#FFF"), ("Fedora", "#51A2DA", "#FFF"),
    ("Node.js", "#339933", "#FFF"), ("Express", "#000000", "#FFF"), ("FastAPI", "#009688", "#FFF"), ("GraphQL", "#E10098", "#FFF"), ("REST API", "#02569B", "#FFF"), ("WebSockets", "#010101", "#FFF"), ("Micro", "#000000", "#FFF"),
    ("PostgreSQL", "#4169E1", "#FFF"), ("Redis", "#DC382D", "#FFF"), ("SQLite", "#003B57", "#FFF"), ("Supabase", "#3ECF8E", "#FFF"), ("Firebase", "#FFCA28", "#000"), ("MongoDB", "#47A248", "#FFF"), ("Neo4j", "#008CC1", "#FFF"),
    ("Docker", "#2496ED", "#FFF"), ("Kubernetes", "#326CE5", "#FFF"), ("Git", "#F05032", "#FFF"), ("GitHub Actions", "#2088FF", "#FFF"), ("AWS", "#232F3E", "#FFF"), ("Vercel", "#000000", "#FFF"), ("Cloudflare", "#F38020", "#FFF"),
    ("Neovim", "#57A143", "#FFF"), ("VS Code", "#007ACC", "#FFF"), ("Hyprland", "#00A6A6", "#FFF"), ("Wayland", "#000000", "#FFF"), ("Zsh", "#F1502F", "#FFF"), ("Tmux", "#1BB91F", "#FFF"), ("Figma", "#F24E1E", "#FFF"),
    ("Swift", "#F05138", "#FFF"), ("Kotlin", "#7F52FF", "#FFF"), ("Assembly", "#6E4C13", "#FFF"), ("Ollama", "#000000", "#FFF"), ("NumPy", "#013243", "#FFF"), ("Pandas", "#150458", "#FFF"), ("Scikit-Learn", "#F7931E", "#FFF")
]

def generate_scattered_svg():
    random.seed(42) # Deterministic scattered layout

    cols = 7
    badge_w, badge_h = 115, 36
    gap_x, gap_y = 18, 22
    padding_x, padding_y = 30, 30

    total_w = cols * badge_w + (cols - 1) * gap_x + padding_x * 2 # ~940px
    rows = (len(skills) + cols - 1) // cols
    total_h = rows * badge_h + (rows - 1) * gap_y + padding_y * 2 + 50 # ~560px

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="{total_h}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&amp;display=swap');

      .skill-pill {{
        font-family: 'Share Tech Mono', monospace, sans-serif;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.5px;
      }}

      @keyframes floatA {{
        0% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
        50% {{ transform: translate(-4px, -10px) rotate(calc(var(--rot) + 2deg)); }}
        100% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
      }}

      @keyframes floatB {{
        0% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
        50% {{ transform: translate(6px, -8px) rotate(calc(var(--rot) - 3deg)); }}
        100% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
      }}

      @keyframes floatC {{
        0% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
        50% {{ transform: translate(-5px, 8px) rotate(calc(var(--rot) + 1.5deg)); }}
        100% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
      }}

      .badge-bg {{
        rx: 10px;
        ry: 10px;
        stroke: rgba(255, 255, 255, 0.2);
        stroke-width: 1px;
      }}
    </style>
  </defs>

'''

    for i, (name, bg, fg) in enumerate(skills):
        r = i // cols
        c = i % cols

        # Scatter offsets
        offset_x = random.randint(-14, 14)
        offset_y = random.randint(-12, 12)
        rot_deg = round(random.uniform(-4.5, 4.5), 1)

        x = padding_x + c * (badge_w + gap_x) + offset_x
        y = padding_y + r * (badge_h + gap_y) + offset_y

        center_x = x + badge_w // 2
        center_y = y + badge_h // 2 + 4

        # Select floating animation variant
        anim_type = ["floatA", "floatB", "floatC"][i % 3]
        dur = round(random.uniform(3.5, 5.2), 2)
        delay = round(random.uniform(0.1, 2.5), 2)

        transform_origin = f"{x + badge_w // 2}px {y + badge_h // 2}px"

        svg_content += f'''  <g style="--rot: {rot_deg}deg; animation: {anim_type} {dur}s ease-in-out infinite; animation-delay: {delay}s; transform-origin: {transform_origin};">
    <rect x="{x}" y="{y}" width="{badge_w}" height="{badge_h}" fill="{bg}" class="badge-bg" />
    <text x="{center_x}" y="{center_y}" fill="{fg}" text-anchor="middle" class="skill-pill">{name}</text>
  </g>
'''

    svg_content += "</svg>\n"

    output_path = "/home/lj/Work/Me/tech_stack_wall.svg"
    with open(output_path, "w") as f:
        f.write(svg_content)
    print(f"Successfully generated SCATTERED FLOATING tech_stack_wall.svg at {output_path}!")

if __name__ == "__main__":
    generate_scattered_svg()
