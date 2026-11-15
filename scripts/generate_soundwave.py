import math

def generate_sine_path(width, height, y_offset, amplitude, wavelength, phase, num_points=40):
    """Generate SVG path string for a sine wave with cubic bezier curves."""
    points = []
    dx = width / num_points
    for i in range(num_points + 1):
        x = i * dx
        window = math.sin(math.pi * i / num_points) ** 0.75
        y = y_offset + amplitude * math.sin(2 * math.pi * (x / wavelength) + phase) * window
        points.append((x, y))
    
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
HEIGHT = 75
Y_MID = 50

# 4 keyframes for 360-degree seamless phase loop
phases = [0, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi]

# Primary Wave
wave1_frames = [generate_sine_path(WIDTH, HEIGHT, Y_MID, 11, 240, p) for p in phases]

# Secondary Harmonic Wave
wave2_frames = [generate_sine_path(WIDTH, HEIGHT, Y_MID, 6.5, 150, p + math.pi/3) for p in phases]

# Sub-harmonic Ambient Wave
wave3_frames = [generate_sine_path(WIDTH, HEIGHT, Y_MID, 4, 320, -p) for p in phases]

val1 = "; ".join(wave1_frames)
val2 = "; ".join(wave2_frames)
val3 = "; ".join(wave3_frames)

# Exactly matching customColorList=1,12,24 from capsule-render header
# #feac5e (peach/sunset) -> #c779d0 (violet) -> #4bc0c8 (teal/cyan)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 75" width="100%" height="75">
  <defs>
    <!-- Perfectly Synced Gradient with Capsule-Render Header (1,12,24) -->
    <linearGradient id="headerSyncGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#feac5e" />
      <stop offset="50%" stop-color="#c779d0" />
      <stop offset="100%" stop-color="#4bc0c8" />
    </linearGradient>

    <!-- Translucent Harmonic Gradient -->
    <linearGradient id="harmonicGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#feac5e" stop-opacity="0.2" />
      <stop offset="50%" stop-color="#c779d0" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#4bc0c8" stop-opacity="0.2" />
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
    .greeting-title {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Roboto, sans-serif;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 4px;
      text-transform: uppercase;
      fill: url(#headerSyncGrad);
    }}
  </style>

  <!-- Background Chassis -->
  <rect x="0" y="0" width="900" height="75" rx="10" fill="#0D1117" />
  <rect x="0" y="0" width="900" height="75" rx="10" fill="none" stroke="url(#headerSyncGrad)" stroke-width="1" stroke-opacity="0.25" />

  <!-- Main Centered Greeting Text (Synced Gradient, No side telemetry) -->
  <text x="450" y="28" text-anchor="middle" class="greeting-title">
    GREETINGS VISITOR  •  ENJOY YOUR TIME HERE
  </text>

  <!-- Secondary Harmonic Wave (Synced Gradient, Faster Harmonic) -->
  <path fill="none" stroke="url(#harmonicGrad)" stroke-width="1.4" opacity="0.7">
    <animate attributeName="d" dur="6s" repeatCount="indefinite" values="{val2}" />
  </path>

  <!-- Sub-Harmonic Ambient Wave (Subtle Teal Base) -->
  <path fill="none" stroke="#4bc0c8" stroke-width="1" opacity="0.3">
    <animate attributeName="d" dur="9s" repeatCount="indefinite" values="{val3}" />
  </path>

  <!-- Primary Liquid Frequency Wave (Synced Header Gradient with Glow) -->
  <path fill="none" stroke="url(#headerSyncGrad)" stroke-width="2.2" filter="url(#neonGlow)">
    <animate attributeName="d" dur="4.5s" repeatCount="indefinite" values="{val1}" />
  </path>
</svg>
'''

with open('/tmp/soundwave_greeting_synced.svg', 'w') as f:
    f.write(svg)

print("Successfully generated /tmp/soundwave_greeting_synced.svg")
