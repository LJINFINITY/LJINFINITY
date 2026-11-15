def generate_header_svg():
    width = 520
    height = 240

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}">
  <defs>
    <style>
      .term-bg {{
        fill: #0D1117;
        stroke: #30363D;
        stroke-width: 1.2px;
      }}
      .term-header {{
        fill: #161B22;
        stroke: #30363D;
        stroke-width: 1px;
      }}
      .term-title {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        font-size: 11px;
        fill: #8B949E;
        font-weight: 600;
        letter-spacing: 0.5px;
      }}
      .main-name {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
        font-size: 28px;
        font-weight: 800;
        fill: #F0F6FC;
        letter-spacing: 1px;
      }}
      .handle {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        font-size: 14px;
        font-weight: 700;
        fill: #38BDF8;
        letter-spacing: 1.5px;
      }}
      .sync-role {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        font-size: 14.5px;
        font-weight: 600;
        letter-spacing: 0.5px;
      }}
      .pill-text {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        font-size: 10.5px;
        font-weight: 600;
        fill: #C9D1D9;
      }}
      .cursor {{
        animation: cursorBlink 1s infinite;
      }}

      /* Synchronous Cycling Role Animation */
      @keyframes roleCycle1 {{
        0%, 22%   {{ opacity: 1; transform: translateY(0); }}
        25%, 97%  {{ opacity: 0; transform: translateY(-8px); }}
        100%      {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes roleCycle2 {{
        0%, 24%   {{ opacity: 0; transform: translateY(8px); }}
        27%, 48%  {{ opacity: 1; transform: translateY(0); }}
        51%, 100% {{ opacity: 0; transform: translateY(-8px); }}
      }}
      @keyframes roleCycle3 {{
        0%, 49%   {{ opacity: 0; transform: translateY(8px); }}
        52%, 73%  {{ opacity: 1; transform: translateY(0); }}
        76%, 100% {{ opacity: 0; transform: translateY(-8px); }}
      }}
      @keyframes roleCycle4 {{
        0%, 74%   {{ opacity: 0; transform: translateY(8px); }}
        77%, 97%  {{ opacity: 1; transform: translateY(0); }}
        100%      {{ opacity: 0; transform: translateY(8px); }}
      }}

      @keyframes cursorBlink {{
        0%, 49%   {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}

      @keyframes pulseDot {{
        0%, 100% {{ fill: #3FB950; }}
        50%      {{ fill: #2EA043; filter: drop-shadow(0 0 6px rgba(63, 185, 80, 0.8)); }}
      }}
    </style>
  </defs>

  <!-- Terminal Window Background -->
  <rect width="{width}" height="{height}" rx="10" class="term-bg"/>

  <!-- Window Header Bar -->
  <path d="M 0 10 C 0 4.477 4.477 0 10 0 L {width-10} 0 C {width-4.477} 0 {width} 4.477 {width} 10 L {width} 28 L 0 28 Z" class="term-header" />
  
  <!-- Window Control Dots -->
  <circle cx="16" cy="14" r="5" fill="#FF5F56" />
  <circle cx="32" cy="14" r="5" fill="#FFBD2E" />
  <circle cx="48" cy="14" r="5" fill="#27C93F" />

  <!-- Window Title -->
  <text x="{width/2}" y="18" text-anchor="middle" class="term-title">lj@infinity:~ (zsh)</text>

  <!-- Developer Identity -->
  <g transform="translate(24, 60)">
    <text x="0" y="0" class="main-name">JERIN RAJAN</text>
    <text x="210" y="-3" class="handle">// LJINFINITY</text>
  </g>

  <!-- Synchronous Animated Role Line -->
  <g transform="translate(24, 98)">
    <g style="animation: roleCycle1 12s infinite ease-in-out;">
      <text x="0" y="0" class="sync-role" fill="#38BDF8">> AI Full-Stack Developer</text>
    </g>
    <g style="animation: roleCycle2 12s infinite ease-in-out;">
      <text x="0" y="0" class="sync-role" fill="#A78BFA">> Software Architect &amp; Systems Crafter</text>
    </g>
    <g style="animation: roleCycle3 12s infinite ease-in-out;">
      <text x="0" y="0" class="sync-role" fill="#34D399">> Multi-Agent AI Swarm Engineer</text>
    </g>
    <g style="animation: roleCycle4 12s infinite ease-in-out;">
      <text x="0" y="0" class="sync-role" fill="#FBBF24">> Bespoke Linux Desktop Rig Designer</text>
    </g>
    <rect x="360" y="-13" width="8" height="16" fill="#38BDF8" class="cursor"/>
  </g>

  <!-- Divider line -->
  <line x1="24" y1="126" x2="{width-24}" y2="126" stroke="#21262D" stroke-width="1"/>

  <!-- Telemetry / Random Status Matrix -->
  <g transform="translate(24, 150)">
    <!-- Pill 1: Status -->
    <rect x="0" y="0" width="148" height="26" rx="6" fill="#161B22" stroke="#30363D"/>
    <circle cx="12" cy="13" r="3.5" style="animation: pulseDot 2s infinite;"/>
    <text x="24" y="17" class="pill-text">FLOW: ACTIVE</text>

    <!-- Pill 2: Audio Vibe -->
    <rect x="156" y="0" width="168" height="26" rx="6" fill="#161B22" stroke="#30363D"/>
    <text x="14" y="17" transform="translate(156,0)" class="pill-text">🎧 J-POP / JAZZ</text>

    <!-- Pill 3: OS / Shell -->
    <rect x="332" y="0" width="138" height="26" rx="6" fill="#161B22" stroke="#30363D"/>
    <text x="14" y="17" transform="translate(332,0)" class="pill-text">🐚 ENOCH SHELL</text>
  </g>

  <g transform="translate(24, 186)">
    <!-- Pill 4: Level / Architecture -->
    <rect x="0" y="0" width="148" height="26" rx="6" fill="#161B22" stroke="#30363D"/>
    <text x="14" y="17" class="pill-text">⚡ ARCH: ZERO-LAG</text>

    <!-- Pill 5: Core Loop -->
    <rect x="156" y="0" width="168" height="26" rx="6" fill="#161B22" stroke="#30363D"/>
    <text x="14" y="17" transform="translate(156,0)" class="pill-text">⚡ LATENCY: 0.1ms</text>

    <!-- Pill 6: Compositor -->
    <rect x="332" y="0" width="138" height="26" rx="6" fill="#161B22" stroke="#30363D"/>
    <text x="14" y="17" transform="translate(332,0)" class="pill-text">💎 HYPRLAND</text>
  </g>
</svg>'''

    with open("/home/lj/Projects/gitreadme/assets/header_profile.svg", "w") as f:
        f.write(svg_content)
    print("Generated /home/lj/Projects/gitreadme/assets/header_profile.svg successfully!")

if __name__ == "__main__":
    generate_header_svg()
