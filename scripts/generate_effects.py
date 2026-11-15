import re

# 1. GENERATE FOOTER WAVE
# We fetch capsule-render footer wave, inject our synchronized palette, and save locally
footer_svg = '''<svg
  width="854"
  height="140"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  style="z-index:1;position:relative"
  viewBox="0 0 854 140"
>
  <style>
    path {
      transform: rotate(180deg);
      transform-origin: 50% 50%;
    }
  </style>
  <defs>
    <linearGradient id="linear" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#feac5e"/>
      <stop offset="50%" stop-color="#c779d0"/>
      <stop offset="100%" stop-color="#4bc0c8"/>
    </linearGradient>
  </defs>
  
  <g transform="translate(427, 70) scale(1, 1) translate(-427, -70)">
    <path fill="url(#linear)" opacity="0.4">
      <animate
        attributeName="d"
        dur="20s"
        repeatCount="indefinite"
        keyTimes="0;0.333;0.667;1"
        calcmod="spline"
        keySplines="0.2 0 0.2 1;0.2 0 0.2 1;0.2 0 0.2 1"
        begin="0s"
        values="M0 0L 0 50Q 213.5 100 427 65T 854 90L 854 0 Z;M0 0L 0 80Q 213.5 100 427 75T 854 65L 854 0 Z;M0 0L 0 100Q 213.5 70 427 105T 854 65L 854 0 Z;M0 0L 0 50Q 213.5 100 427 65T 854 90L 854 0 Z"
      />
    </path>
    <path fill="url(#linear)" opacity="0.35">
      <animate
        attributeName="d"
        dur="20s"
        repeatCount="indefinite"
        keyTimes="0;0.333;0.667;1"
        calcmod="spline"
        keySplines="0.2 0 0.2 1;0.2 0 0.2 1;0.2 0 0.2 1"
        begin="-5s"
        values="M0 0L 0 50Q 213.5 100 427 65T 854 90L 854 0 Z;M0 0L 0 80Q 213.5 100 427 75T 854 65L 854 0 Z;M0 0L 0 100Q 213.5 70 427 105T 854 65L 854 0 Z;M0 0L 0 50Q 213.5 100 427 65T 854 90L 854 0 Z"
      />
    </path>
  </g>
</svg>'''

with open('/tmp/footer_wave.svg', 'w') as f:
    f.write(footer_svg)


# 2. GENERATE LASER DIVIDER
# An animated pulsing laser beam that shoots across the divider in a loop
laser_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 12" width="100%" height="12">
  <defs>
    <!-- Moving Laser Gradient -->
    <linearGradient id="laserBeam" x1="-40%" y1="0%" x2="140%" y2="0%">
      <stop offset="0%" stop-color="#feac5e" stop-opacity="0" />
      <stop offset="25%" stop-color="#feac5e" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#c779d0" stop-opacity="1" />
      <stop offset="75%" stop-color="#4bc0c8" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#4bc0c8" stop-opacity="0" />
      <animate attributeName="x1" values="-60%;100%;-60%" dur="5s" repeatCount="indefinite" />
      <animate attributeName="x2" values="0%;160%;0%" dur="5s" repeatCount="indefinite" />
    </linearGradient>

    <!-- Ambient Baseline Gradient -->
    <linearGradient id="baseTrack" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#feac5e" stop-opacity="0.05" />
      <stop offset="50%" stop-color="#c779d0" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#4bc0c8" stop-opacity="0.05" />
    </linearGradient>

    <filter id="laserGlow" x="-20%" y="-100%" width="140%" height="300%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Base Track -->
  <line x1="0" y1="6" x2="900" y2="6" stroke="url(#baseTrack)" stroke-width="1" />

  <!-- Animated Laser Pulse Line with Glow -->
  <line x1="0" y1="6" x2="900" y2="6" stroke="url(#laserBeam)" stroke-width="2.5" filter="url(#laserGlow)" />
</svg>'''

with open('/tmp/laser_divider.svg', 'w') as f:
    f.write(laser_svg)

print("Generated /tmp/footer_wave.svg and /tmp/laser_divider.svg")
