import os

skills = [
    # Languages & Core
    ("Rust", "#000000", "#FFF"), ("C++", "#00599C", "#FFF"), ("C", "#A8B9CC", "#000"), ("Python", "#3776AB", "#FFF"), 
    ("TypeScript", "#3178C6", "#FFF"), ("JavaScript", "#F7DF1E", "#000"), ("Go", "#00ADD8", "#FFF"),
    ("Java", "#ED8B00", "#FFF"), ("Kotlin", "#7F52FF", "#FFF"), ("Swift", "#F05138", "#FFF"), ("Lua", "#2C2D72", "#FFF"), 
    ("Bash", "#4EAA25", "#FFF"), ("Zsh", "#F1502F", "#FFF"), ("HTML5", "#E34F26", "#FFF"),
    ("CSS3", "#1572B6", "#FFF"), ("SQL", "#4479A1", "#FFF"), ("Assembly", "#6E4C13", "#FFF"), ("Zig", "#F7A41D", "#000"), 
    ("Elixir", "#4B275F", "#FFF"), ("Haskell", "#5D4F85", "#FFF"), ("PHP", "#777BB4", "#FFF"),

    # AI & ML
    ("PyTorch", "#EE4C2C", "#FFF"), ("TensorFlow", "#FF6F00", "#FFF"), ("OpenCV", "#5C3EE8", "#FFF"), ("Hugging Face", "#FFD21E", "#000"), 
    ("Vercel AI", "#000000", "#FFF"), ("LangChain", "#1C3C3C", "#FFF"), ("LlamaIndex", "#000000", "#FFF"),
    ("Ollama", "#000000", "#FFF"), ("CUDA", "#76B900", "#000"), ("NumPy", "#013243", "#FFF"), ("Pandas", "#150458", "#FFF"), 
    ("Scikit-Learn", "#F7931E", "#FFF"), ("Keras", "#D00000", "#FFF"), ("ONNX", "#005CED", "#FFF"),
    ("OpenAI API", "#412991", "#FFF"), ("Anthropic", "#D97757", "#FFF"), ("DeepSeek", "#4D6BFE", "#FFF"), ("Whisper", "#00A67E", "#FFF"), 
    ("Midjourney", "#000000", "#FFF"), ("ComfyUI", "#222222", "#FFF"), ("Qwen", "#6366F1", "#FFF"),

    # Linux & Desktop Rig
    ("Linux", "#FCC624", "#000"), ("Fedora", "#51A2DA", "#FFF"), ("Arch Linux", "#1793D1", "#FFF"), ("Hyprland", "#00A6A6", "#FFF"), 
    ("Quickshell", "#2E3440", "#FFF"), ("QML", "#41CD52", "#FFF"), ("Wayland", "#000000", "#FFF"),
    ("Matugen", "#E5A000", "#000"), ("Pipewire", "#2A52BE", "#FFF"), ("Systemd", "#000000", "#FFF"), ("Neovim", "#57A143", "#FFF"), 
    ("VS Code", "#007ACC", "#FFF"), ("Tmux", "#1BB91F", "#FFF"), ("Kitty", "#000000", "#FFF"),
    ("Alacritty", "#F43E31", "#FFF"), ("Starship", "#DD4B39", "#FFF"), ("RTK", "#CE422B", "#FFF"), ("Rofi", "#3F51B5", "#FFF"), 
    ("Waybar", "#2C3E50", "#FFF"), ("Zsh Rig", "#F1502F", "#FFF"), ("Linux Rig", "#FCC624", "#000"),

    # Web & Microservices
    ("React", "#61DAFB", "#000"), ("Next.js", "#000000", "#FFF"), ("Vite", "#646CFF", "#FFF"), ("Vue.js", "#4FC08D", "#FFF"), 
    ("Svelte", "#FF3E00", "#FFF"), ("Tailwind", "#06B6D4", "#FFF"), ("Expo", "#000000", "#FFF"),
    ("Redux", "#764ABC", "#FFF"), ("Node.js", "#339933", "#FFF"), ("Express", "#000000", "#FFF"), ("FastAPI", "#009688", "#FFF"), 
    ("Django", "#092E20", "#FFF"), ("Flask", "#000000", "#FFF"), ("GraphQL", "#E10098", "#FFF"),
    ("REST API", "#02569B", "#FFF"), ("WebSockets", "#010101", "#FFF"), ("gRPC", "#244C5A", "#FFF"), ("Electron", "#47848F", "#FFF"), 
    ("Tauri", "#FFC131", "#000"), ("Three.js", "#000000", "#FFF"), ("WebAssembly", "#654FF0", "#FFF"),

    # DB & Infrastructure
    ("PostgreSQL", "#4169E1", "#FFF"), ("Redis", "#DC382D", "#FFF"), ("SQLite", "#003B57", "#FFF"), ("Supabase", "#3ECF8E", "#FFF"), 
    ("Firebase", "#FFCA28", "#000"), ("MongoDB", "#47A248", "#FFF"), ("Neo4j", "#008CC1", "#FFF"),
    ("Qdrant", "#DC2626", "#FFF"), ("ChromaDB", "#E11D48", "#FFF"), ("Docker", "#2496ED", "#FFF"), ("Kubernetes", "#326CE5", "#FFF"), 
    ("Git", "#F05032", "#FFF"), ("GitHub Actions", "#2088FF", "#FFF"), ("AWS", "#232F3E", "#FFF"),
    ("Vercel", "#000000", "#FFF"), ("Netlify", "#00C7B7", "#000"), ("Cloudflare", "#F38020", "#FFF"), ("NGINX", "#009639", "#FFF"), 
    ("Postman", "#FF6C37", "#FFF"), ("Figma", "#F24E1E", "#FFF"), ("Uriel AI", "#6366F1", "#FFF")
]

def generate_skills_wall_svg():
    cols = 7
    badge_w, badge_h = 115, 34
    gap_x, gap_y = 10, 10
    padding_x, padding_y = 15, 15

    total_w = cols * badge_w + (cols - 1) * gap_x + padding_x * 2 # 895px
    rows = (len(skills) + cols - 1) // cols
    total_h = rows * badge_h + (rows - 1) * gap_y + padding_y * 2 # ~580px

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="{total_h}">
  <defs>
    <style>
      .skill-pill {{
        font-family: ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.3px;
      }}
      .badge-bg {{
        rx: 6px;
        ry: 6px;
        stroke: rgba(255, 255, 255, 0.2);
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

        center_x = x + badge_w // 2
        center_y = y + badge_h // 2 + 4

        svg_content += f'''  <g>
    <rect x="{x}" y="{y}" width="{badge_w}" height="{badge_h}" fill="{bg}" class="badge-bg" />
    <text x="{center_x}" y="{center_y}" fill="{fg}" text-anchor="middle" class="skill-pill">{name}</text>
  </g>
'''

    svg_content += "</svg>\n"

    output_path = "/home/lj/Work/Me/skills_wall.svg"
    with open(output_path, "w") as f:
        f.write(svg_content)
    print(f"Successfully generated 95+ skill vector SVG at {output_path}!")

if __name__ == "__main__":
    generate_skills_wall_svg()
