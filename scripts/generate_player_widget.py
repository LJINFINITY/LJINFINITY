def generate_player():
    width = 900
    height = 96
    
    # 12 Equalizer bars with multi-color gradients
    eq_bars_svg = ""
    for i in range(14):
        dur = 0.7 + (i % 5) * 0.25
        h_min = 4 + (i % 3) * 3
        h_max = 24 + ((i * 3) % 12)
        eq_bars_svg += f'''
        <rect x="{i*6}" width="4" height="12" rx="1.5" class="eq-col" style="animation: eqAnim{i%5} {dur:.2f}s infinite ease-in-out;"/>'''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}">
  <defs>
    <linearGradient id="eqGradient" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="55%" stop-color="#FBBF24" />
      <stop offset="100%" stop-color="#F43F5E" />
    </linearGradient>

    <linearGradient id="vinylGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="100%" stop-color="#A855F7" />
    </linearGradient>

    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@600;700&amp;display=swap');

      .eq-col {{
        fill: url(#eqGradient);
        transform-origin: bottom;
      }}

      /* Equalizer Keyframes */
      @keyframes eqAnim0 {{ 0%, 100% {{ height: 6px; y: 22px; }} 50% {{ height: 26px; y: 2px; }} }}
      @keyframes eqAnim1 {{ 0%, 100% {{ height: 22px; y: 6px; }} 50% {{ height: 10px; y: 18px; }} }}
      @keyframes eqAnim2 {{ 0%, 100% {{ height: 14px; y: 14px; }} 50% {{ height: 28px; y: 0px; }} }}
      @keyframes eqAnim3 {{ 0%, 100% {{ height: 26px; y: 2px; }} 50% {{ height: 8px; y: 20px; }} }}
      @keyframes eqAnim4 {{ 0%, 100% {{ height: 10px; y: 18px; }} 50% {{ height: 24px; y: 4px; }} }}

      @keyframes spinVinyl {{
        0%   {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
      }}
    </style>
  </defs>

  <!-- Player Background -->
  <rect width="{width}" height="{height}" rx="12" fill="#0A0E14" stroke="#21262D" stroke-width="1.2"/>

  <!-- Left: Animated Turntable / Disc -->
  <g transform="translate(24, 22)">
    <circle cx="26" cy="26" r="24" fill="#111620" stroke="url(#vinylGlow)" stroke-width="1.5"/>
    <g style="animation: spinVinyl 6s linear infinite; transform-origin: 26px 26px;">
      <circle cx="26" cy="26" r="18" fill="none" stroke="#21262D" stroke-width="1.5" stroke-dasharray="8 4"/>
      <circle cx="26" cy="26" r="12" fill="none" stroke="#30363D" stroke-width="1" stroke-dasharray="4 3"/>
      <circle cx="26" cy="26" r="6" fill="#161B22" stroke="#00F0FF" stroke-width="1.5"/>
    </g>
    <circle cx="26" cy="26" r="2.5" fill="#FFFFFF"/>
  </g>

  <!-- Equalizer Spectrum Visualizer -->
  <g transform="translate(92, 34)">
    {eq_bars_svg}
  </g>

  <!-- Center Track Info -->
  <g transform="translate(196, 32)">
    <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="800" fill="#F0F6FC">Lamp — A Midnight Cold Session</text>
    <text x="248" y="0" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" fill="#EC4899">// J-POP &amp; MODERN JAZZ</text>

    <!-- Progress Scrubber -->
    <g transform="translate(0, 16)">
      <line x1="0" y1="8" x2="470" y2="8" stroke="#161B22" stroke-width="5" stroke-linecap="round"/>
      <line x1="0" y1="8" x2="280" y2="8" stroke="#00F0FF" stroke-width="5" stroke-linecap="round"/>
      <circle cx="280" cy="8" r="5.5" fill="#FFFFFF" stroke="#00F0FF" stroke-width="2"/>
      
      <text x="490" y="12" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#00F0FF">02:41 / 03:52</text>
    </g>
  </g>

  <!-- Right Play Controls -->
  <g transform="translate(730, 32)">
    <rect x="0" y="0" width="144" height="32" rx="6" fill="#111620" stroke="#30363D"/>
    <text x="18" y="20" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#94A3B8">⏮</text>
    <text x="44" y="20" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#00F0FF">❚❚ PLAYING</text>
    <text x="116" y="20" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#94A3B8">⏭</text>
  </g>
</svg>'''

    with open("/home/lj/Projects/gitreadme/assets/player_widget.svg", "w") as f:
        f.write(svg)
    print("Generated /home/lj/Projects/gitreadme/assets/player_widget.svg successfully!")

if __name__ == "__main__":
    generate_player()
