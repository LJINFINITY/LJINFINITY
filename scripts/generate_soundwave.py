import math

def generate_sine_path(width, height, y_offset, amplitude, wavelength, phase, num_points=32):
    """Generate SVG path string for a sine wave with cubic bezier curves."""
    points = []
    dx = width / num_points
    for i in range(num_points + 1):
        x = i * dx
        # Sine wave with attenuation at edges
        window = math.sin(math.pi * i / num_points) ** 0.8 # smooth fade at ends
        y = y_offset + amplitude * math.sin(2 * math.pi * (x / wavelength) + phase) * window
        points.append((x, y))
    
    # Construct smooth path using cubic bezier segments
    d = f"M{points[0][0]:.1f},{points[0][1]:.1f}"
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i+1]
        cx1 = x0 + (x1 - x0) / 2
        cy1 = y0
        cx2 = x0 + (x1 - x0) / 2
        cy2 = y1
        d += f" C{cx1:.1f},{cy1:.1f} {cx2:.1f},{cy2:.1f} {x1:.1f},{y1:.1f}"
    return d

WIDTH = 900
HEIGHT = 80
Y_MID = 54

# Generate 4 keyframes for 360 degree phase loop
phases = [0, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi]

# Primary Wave (Cyan, larger amplitude)
wave1_frames = [generate_sine_path(WIDTH, HEIGHT, Y_MID, 12, 220, p) for p in phases]

# Secondary Harmonic Wave (Violet, higher frequency, phase offset)
wave2_frames = [generate_sine_path(WIDTH, HEIGHT, Y_MID, 7, 140, p + math.pi/4) for p in phases]

# Sub-harmonic / Baseline Glow Wave (Emerald/Teal, longer wavelength)
wave3_frames = [generate_sine_path(WIDTH, HEIGHT, Y_MID, 5, 300, -p) for p in phases]

val1 = "; ".join(wave1_frames)
val2 = "; ".join(wave2_frames)
val3 = "; ".join(wave3_frames)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 80" width="100%" height="80">
  <defs>
    <!-- Cyan to Royal Violet Gradient -->
    <linearGradient id="freqGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.1" />
      <stop offset="20%" stop-color="#00F0FF" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#A855F7" stop-opacity="1" />
      <stop offset="80%" stop-color="#00F0FF" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#00F0FF" stop-opacity="0.1" />
    </linearGradient>

    <!-- Harmonic Wave Gradient -->
    <linearGradient id="freqGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0" />
      <stop offset="30%" stop-color="#EC4899" stop-opacity="0.6" />
      <stop offset="70%" stop-color="#8B5CF6" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0" />
    </linearGradient>

    <!-- Text Glow & Gradient -->
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E0F2FE" />
      <stop offset="50%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#E0F2FE" />
    </linearGradient>

    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .mono-telemetry {{
      font-family: 'JetBrains Mono', -apple-system, 'SF Mono', monospace;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 1.5px;
      fill: #38BDF8;
      opacity: 0.75;
    }}
    .greeting-title {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Roboto, sans-serif;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 3.5px;
      text-transform: uppercase;
      fill: url(#textGrad);
    }}
  </style>

  <!-- Background Chassis -->
  <rect x="0" y="0" width="900" height="80" rx="10" fill="#0D1117" />
  <rect x="0" y="0" width="900" height="80" rx="10" fill="none" stroke="rgba(56, 189, 248, 0.18)" stroke-width="1" />

  <!-- Top Telemetry & Main Text -->
  <text x="35" y="27" class="mono-telemetry">// FREQ: 432Hz [STEREO]</text>
  <text x="450" y="27" text-anchor="middle" class="greeting-title">GREETINGS VISITOR  •  ENJOY YOUR TIME HERE</text>
  <text x="865" y="27" text-anchor="end" class="mono-telemetry">STATUS: FLOW ♫</text>

  <!-- Secondary Harmonic Wave (Pink/Purple) -->
  <path fill="none" stroke="url(#freqGrad2)" stroke-width="1.5" opacity="0.75">
    <animate attributeName="d" dur="5s" repeatCount="indefinite" values="{val2}" />
  </path>

  <!-- Sub-Harmonic Baseline Wave (Teal) -->
  <path fill="none" stroke="#2DD4BF" stroke-width="1" opacity="0.35">
    <animate attributeName="d" dur="8s" repeatCount="indefinite" values="{val3}" />
  </path>

  <!-- Primary Liquid Frequency Wave (Cyan/Violet Neon) -->
  <path fill="none" stroke="url(#freqGrad1)" stroke-width="2.2" filter="url(#neonGlow)">
    <animate attributeName="d" dur="4s" repeatCount="indefinite" values="{val1}" />
  </path>
</svg>
'''

with open('/tmp/soundwave_greeting.svg', 'w') as f:
    f.write(svg)

print("Successfully generated /tmp/soundwave_greeting.svg")
