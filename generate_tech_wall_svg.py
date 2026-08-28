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
    ("Enoch Shell", "#3B82F6", "#FFF"), ("Arc Tracker", "#10B981", "#FFF")
]

def generate_true_random_smooth_svg():
    random.seed(8888) # Completely organic scatter distribution

    total_w = 1150
    total_h = 1850
    badge_w, badge_h = 145, 46

    # Generate non-overlapping random scatter positions
    positions = []
    attempts = 0
    max_attempts = 50000

    for skill in skills:
        placed = False
        for _ in range(max_attempts):
            rx = random.randint(40, total_w - badge_w - 40)
            ry = random.randint(40, total_h - badge_h - 40)
            
            # Check overlap with placed badges (minimum padding clearance)
            overlap = False
            for (px, py, _, _, _) in positions:
                if abs(rx - px) < (badge_w + 22) and abs(ry - py) < (badge_h + 28):
                    overlap = True
                    break
            
            if not overlap:
                rot = round(random.uniform(-10.0, 10.0), 1)
                anim_idx = random.randint(1, 6)
                positions.append((rx, ry, rot, anim_idx, skill))
                placed = True
                break
        
        if not placed:
            # Fallback random placement if dense area
            rx = random.randint(40, total_w - badge_w - 40)
            ry = random.randint(40, total_h - badge_h - 40)
            rot = round(random.uniform(-10.0, 10.0), 1)
            anim_idx = random.randint(1, 6)
            positions.append((rx, ry, rot, anim_idx, skill))

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="{total_h}">
  <defs>
    <style>
      .skill-pill {{
        font-family: ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 0.5px;
      }}

      /* Explicit keyframes with direct degree interpolation for buttery-smooth rotation */
      @keyframes float1 {{
        0%   {{ transform: translate(0px, 0px) rotate(-8deg); }}
        50%  {{ transform: translate(-14px, -26px) rotate(-3deg); }}
        100% {{ transform: translate(0px, 0px) rotate(-8deg); }}
      }}

      @keyframes float2 {{
        0%   {{ transform: translate(0px, 0px) rotate(7deg); }}
        50%  {{ transform: translate(16px, -22px) rotate(2deg); }}
        100% {{ transform: translate(0px, 0px) rotate(7deg); }}
      }}

      @keyframes float3 {{
        0%   {{ transform: translate(0px, 0px) rotate(-5deg); }}
        50%  {{ transform: translate(-12px, 25px) rotate(-9deg); }}
        100% {{ transform: translate(0px, 0px) rotate(-5deg); }}
      }}

      @keyframes float4 {{
        0%   {{ transform: translate(0px, 0px) rotate(9deg); }}
        50%  {{ transform: translate(15px, 20px) rotate(4deg); }}
        100% {{ transform: translate(0px, 0px) rotate(9deg); }}
      }}

      @keyframes float5 {{
        0%   {{ transform: translate(0px, 0px) rotate(-3deg); }}
        50%  {{ transform: translate(-18px, -15px) rotate(-7deg); }}
        100% {{ transform: translate(0px, 0px) rotate(-3deg); }}
      }}

      @keyframes float6 {{
        0%   {{ transform: translate(0px, 0px) rotate(6deg); }}
        50%  {{ transform: translate(12px, -28px) rotate(10deg); }}
        100% {{ transform: translate(0px, 0px) rotate(6deg); }}
      }}

      .badge-bg {{
        rx: 12px;
        ry: 12px;
        stroke: rgba(255, 255, 255, 0.25);
        stroke-width: 1.2px;
      }}
    </style>
  </defs>

'''

    for (x, y, rot, anim_idx, (name, bg, fg)) in positions:
        center_x = x + badge_w // 2
        center_y = y + badge_h // 2 + 5

        dur = round(random.uniform(8.0, 13.0), 2)
        delay = round(random.uniform(0.1, 5.5), 2)
        transform_origin = f"{center_x}px {center_y - 5}px"

        svg_content += f'''  <g style="animation: float{anim_idx} {dur}s cubic-bezier(0.45, 0.05, 0.55, 0.95) infinite; animation-delay: {delay}s; transform-origin: {transform_origin};">
    <rect x="{x}" y="{y}" width="{badge_w}" height="{badge_h}" fill="{bg}" class="badge-bg" />
    <text x="{center_x}" y="{center_y}" fill="{fg}" text-anchor="middle" class="skill-pill">{name}</text>
  </g>
'''

    svg_content += "</svg>\n"

    output_path = "/home/lj/Work/Me/tech_stack_wall_v7.svg"
    with open(output_path, "w") as f:
        f.write(svg_content)
    print(f"Successfully generated TRUE RANDOM SMOOTH FLOATING tech_stack_wall_v7.svg at {output_path}!")

if __name__ == "__main__":
    generate_true_random_smooth_svg()
