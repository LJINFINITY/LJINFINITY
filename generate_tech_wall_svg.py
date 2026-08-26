import os
import random

skills = [
    # Languages & Systems
    ("Rust", "#000000", "#FFF"), ("C++", "#00599C", "#FFF"), ("Python", "#3776AB", "#FFF"), ("TypeScript", "#3178C6", "#FFF"), 
    ("JavaScript", "#F7DF1E", "#000"), ("Go", "#00ADD8", "#FFF"), ("Java", "#ED8B00", "#FFF"), ("Lua", "#2C2D72", "#FFF"), 
    ("Bash", "#4EAA25", "#FFF"), ("Zsh", "#F1502F", "#FFF"), ("C", "#A8B9CC", "#000"), ("Assembly", "#6E4C13", "#FFF"),
    
    # AI, Agents & ML
    ("PyTorch", "#EE4C2C", "#FFF"), ("TensorFlow", "#FF6F00", "#FFF"), ("OpenCV", "#5C3EE8", "#FFF"), ("Hugging Face", "#FFD21E", "#000"), 
    ("Vercel AI", "#000000", "#FFF"), ("LangChain", "#1C3C3C", "#FFF"), ("LlamaIndex", "#000000", "#FFF"), ("Ollama", "#000000", "#FFF"), 
    ("CUDA", "#76B900", "#000"), ("NumPy", "#013243", "#FFF"), ("Pandas", "#150458", "#FFF"), ("Scikit-Learn", "#F7931E", "#FFF"), 
    ("OpenAI API", "#412991", "#FFF"), ("Anthropic", "#D97757", "#FFF"), ("DeepSeek", "#4D6BFE", "#FFF"), ("Whisper", "#00A67E", "#FFF"),

    # Linux & Desktop Shell Rig
    ("Fedora", "#51A2DA", "#FFF"), ("Arch Linux", "#1793D1", "#FFF"), ("Hyprland", "#00A6A6", "#FFF"), ("Quickshell", "#2E3440", "#FFF"), 
    ("Wayland", "#000000", "#FFF"), ("QML", "#41CD52", "#FFF"), ("Matugen", "#E5A000", "#000"), ("Pipewire", "#2A52BE", "#FFF"), 
    ("Systemd", "#000000", "#FFF"), ("Neovim", "#57A143", "#FFF"), ("VS Code", "#007ACC", "#FFF"), ("Tmux", "#1BB91F", "#FFF"), 
    ("Kitty", "#000000", "#FFF"), ("Alacritty", "#F43E31", "#FFF"), ("Starship", "#DD4B39", "#FFF"), ("RTK", "#CE422B", "#FFF"),

    # Web, Mobile & Runtimes
    ("React", "#61DAFB", "#000"), ("Next.js", "#000000", "#FFF"), ("Vite", "#646CFF", "#FFF"), ("Vue.js", "#4FC08D", "#FFF"), 
    ("Svelte", "#FF3E00", "#FFF"), ("Tailwind", "#06B6D4", "#FFF"), ("Expo", "#000000", "#FFF"), ("Redux", "#764ABC", "#FFF"), 
    ("Node.js", "#339933", "#FFF"), ("Express", "#000000", "#FFF"), ("FastAPI", "#009688", "#FFF"), ("Django", "#092E20", "#FFF"), 
    ("Flask", "#000000", "#FFF"), ("GraphQL", "#E10098", "#FFF"), ("REST API", "#02569B", "#FFF"), ("WebSockets", "#010101", "#FFF"), 
    ("gRPC", "#244C5A", "#FFF"), ("Electron", "#47848F", "#FFF"), ("Tauri", "#FFC131", "#000"), ("Three.js", "#000000", "#FFF"),

    # DB, Cloud & Tools
    ("PostgreSQL", "#4169E1", "#FFF"), ("Redis", "#DC382D", "#FFF"), ("SQLite", "#003B57", "#FFF"), ("Supabase", "#3ECF8E", "#FFF"), 
    ("Firebase", "#FFCA28", "#000"), ("MongoDB", "#47A248", "#FFF"), ("Qdrant", "#DC2626", "#FFF"), ("ChromaDB", "#E11D48", "#FFF"), 
    ("Docker", "#2496ED", "#FFF"), ("Kubernetes", "#326CE5", "#FFF"), ("Git", "#F05032", "#FFF"), ("GitHub Actions", "#2088FF", "#FFF"), 
    ("AWS", "#232F3E", "#FFF"), ("Vercel", "#000000", "#FFF"), ("Netlify", "#00C7B7", "#000"), ("Cloudflare", "#F38020", "#FFF"), 
    ("NGINX", "#009639", "#FFF"), ("Postman", "#FF6C37", "#FFF"), ("Figma", "#F24E1E", "#FFF"), ("Uriel AI", "#6366F1", "#FFF"),
    ("Infinity Shell", "#3B82F6", "#FFF"), ("Arc Tracker", "#10B981", "#FFF")
]

def generate_random_scattered_svg():
    random.seed(1337) # High-quality random spread

    cols = 9
    badge_w, badge_h = 108, 34
    gap_x, gap_y = 16, 20
    padding_x, padding_y = 25, 25

    total_w = cols * badge_w + (cols - 1) * gap_x + padding_x * 2 # ~1090px
    rows = (len(skills) + cols - 1) // cols
    total_h = rows * badge_h + (rows - 1) * gap_y + padding_y * 2 + 40 # ~560px

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="{total_h}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&amp;display=swap');

      .skill-pill {{
        font-family: 'Share Tech Mono', monospace, sans-serif;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.3px;
      }}

      @keyframes floatA {{
        0% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
        50% {{ transform: translate(-8px, -12px) rotate(calc(var(--rot) + 3deg)); }}
        100% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
      }}

      @keyframes floatB {{
        0% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
        50% {{ transform: translate(10px, -10px) rotate(calc(var(--rot) - 4deg)); }}
        100% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
      }}

      @keyframes floatC {{
        0% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
        50% {{ transform: translate(-6px, 11px) rotate(calc(var(--rot) + 2.5deg)); }}
        100% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
      }}

      @keyframes floatD {{
        0% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
        50% {{ transform: translate(9px, 8px) rotate(calc(var(--rot) - 3deg)); }}
        100% {{ transform: translate(0px, 0px) rotate(var(--rot)); }}
      }}

      .badge-bg {{
        rx: 9px;
        ry: 9px;
        stroke: rgba(255, 255, 255, 0.22);
        stroke-width: 1px;
      }}
    </style>
  </defs>

'''

    for i, (name, bg, fg) in enumerate(skills):
        r = i // cols
        c = i % cols

        # Strong random scatter offsets
        offset_x = random.randint(-22, 22)
        offset_y = random.randint(-18, 18)
        rot_deg = round(random.uniform(-7.5, 7.5), 1)

        x = padding_x + c * (badge_w + gap_x) + offset_x
        y = padding_y + r * (badge_h + gap_y) + offset_y

        center_x = x + badge_w // 2
        center_y = y + badge_h // 2 + 4

        # Select float animation variant
        anim_type = ["floatA", "floatB", "floatC", "floatD"][i % 4]
        dur = round(random.uniform(3.0, 5.8), 2)
        delay = round(random.uniform(0.1, 3.2), 2)

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
    print(f"Successfully generated 80+ RANDOM SCATTER FLOATING tech_stack_wall.svg at {output_path}!")

if __name__ == "__main__":
    generate_random_scattered_svg()
