#!/usr/bin/env python3
"""
Bespoke GitHub Profile Banner Generator for Jerin Rajan (LJINFINITY)
Renders ultra-crisp, high-DPI retina banners using Cairo and system typography.
"""

import sys
import os
import math
import argparse
import cairo

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUTPUT = os.path.join(REPO_ROOT, "assets", "banner.png")


def render_horizon(output_path=DEFAULT_OUTPUT):
    """Render Horizon Minimalist (Linear & Vercel dark luxury aesthetic)."""
    W, H = 1920, 500
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    ctx = cairo.Context(surf)

    # Dark background
    ctx.set_source_rgb(0.027, 0.035, 0.051)  # #07090D
    ctx.paint()

    # Horizon beam arc at top
    grad = cairo.LinearGradient(0, 0, W, 0)
    grad.add_color_stop_rgba(0.0, 0.0, 0.94, 1.0, 0.0)
    grad.add_color_stop_rgba(0.2, 0.0, 0.94, 1.0, 0.8)       # Electric Cyan
    grad.add_color_stop_rgba(0.5, 0.51, 0.38, 0.97, 0.95)    # Royal Indigo/Violet
    grad.add_color_stop_rgba(0.8, 0.93, 0.28, 0.60, 0.7)     # Neon Rose
    grad.add_color_stop_rgba(1.0, 0.93, 0.28, 0.60, 0.0)

    # Ambient glow under the horizon line
    rad_glow = cairo.RadialGradient(W / 2, 0, 10, W / 2, 0, 500)
    rad_glow.add_color_stop_rgba(0.0, 0.45, 0.35, 0.95, 0.25)
    rad_glow.add_color_stop_rgba(0.5, 0.0, 0.7, 0.9, 0.10)
    rad_glow.add_color_stop_rgba(1.0, 0.0, 0.0, 0.0, 0.0)
    ctx.set_source(rad_glow)
    ctx.paint()

    # Horizon laser line
    ctx.set_source(grad)
    ctx.set_line_width(2.5)
    ctx.move_to(0, 2)
    ctx.line_to(W, 2)
    ctx.stroke()

    # Top Status Pill
    ctx.select_font_face('JetBrains Mono', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(15)
    pill_text = "SYSTEM STATUS: OPERATIONAL  //  LJINFINITY"
    ext = ctx.text_extents(pill_text)
    pw = ext.width + 56
    ph = 36
    px = (W - pw) / 2
    py = 45

    # Pill container
    ctx.set_source_rgba(0.1, 0.15, 0.22, 0.7)
    ctx.arc(px + pw - 18, py + 18, 18, -math.pi / 2, math.pi / 2)
    ctx.arc(px + 18, py + 18, 18, math.pi / 2, 3 * math.pi / 2)
    ctx.close_path()
    ctx.fill()
    ctx.set_source_rgba(0.0, 0.94, 1.0, 0.35)
    ctx.set_line_width(1.2)
    ctx.stroke()

    # Pulsing Green Dot
    ctx.set_source_rgba(0.06, 0.85, 0.55, 1.0)
    ctx.arc(px + 22, py + 18, 4.5, 0, 2 * math.pi)
    ctx.fill()
    ctx.set_source_rgba(0.06, 0.85, 0.55, 0.3)
    ctx.arc(px + 22, py + 18, 8.5, 0, 2 * math.pi)
    ctx.fill()

    # Text inside pill
    ctx.set_source_rgba(0.9, 0.95, 1.0, 0.9)
    ctx.move_to(px + 38, py + 24)
    ctx.show_text(pill_text)

    # Massive Minimal Title
    ctx.select_font_face('Inter Display', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(96)
    title = "JERIN RAJAN"
    ext_t = ctx.text_extents(title)

    # Title gradient fill
    tg = cairo.LinearGradient((W - ext_t.width) / 2, 0, (W + ext_t.width) / 2, 0)
    tg.add_color_stop_rgb(0.0, 1.0, 1.0, 1.0)
    tg.add_color_stop_rgb(0.7, 1.0, 1.0, 1.0)
    tg.add_color_stop_rgb(1.0, 0.75, 0.85, 1.0)
    ctx.set_source(tg)
    ctx.move_to((W - ext_t.width) / 2, 215)
    ctx.show_text(title)

    # Elegant Subtitle
    ctx.select_font_face('Inter', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(24)
    sub = "AI Full-Stack Architect  •  Systems Engineer  •  Unix Ricing Artisan"
    ext_s = ctx.text_extents(sub)
    ctx.set_source_rgba(0.55, 0.65, 0.80, 0.9)
    ctx.move_to((W - ext_s.width) / 2, 268)
    ctx.show_text(sub)

    # Subtle quote
    ctx.select_font_face('Inter', cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(18)
    q = '"Work should be an engaging, creative journey — building tools I genuinely desire to see in the world."'
    ext_q = ctx.text_extents(q)
    ctx.set_source_rgba(0.40, 0.48, 0.62, 0.85)
    ctx.move_to((W - ext_q.width) / 2, 315)
    ctx.show_text(q)

    # Three Bento Micro-Cards at Bottom
    cards = [
        ("CORE STACK", "Rust • C++ • Python • Next.js • PyTorch", 0.0, 0.94, 1.0),
        ("DESKTOP RIG", "Arch Linux • Hyprland • Quickshell QML", 0.65, 0.4, 0.98),
        ("FLOW STATE", "Zero-Lag Workflows • J-Pop & Modern Jazz", 0.06, 0.8, 0.55)
    ]
    card_w = 460
    card_h = 75
    gap = 40
    start_x = (W - (3 * card_w + 2 * gap)) / 2
    cy = 375

    for i, (k, v, r, g, b) in enumerate(cards):
        cx = start_x + i * (card_w + gap)
        # Card bg
        ctx.set_source_rgba(0.08, 0.11, 0.18, 0.6)
        ctx.rectangle(cx, cy, card_w, card_h)
        ctx.fill()
        # Card border
        ctx.set_source_rgba(r, g, b, 0.25)
        ctx.set_line_width(1.2)
        ctx.rectangle(cx, cy, card_w, card_h)
        ctx.stroke()
        # Left accent pill
        ctx.set_source_rgba(r, g, b, 0.9)
        ctx.rectangle(cx, cy, 3, card_h)
        ctx.fill()
        # Label
        ctx.select_font_face('JetBrains Mono', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(13)
        ctx.set_source_rgba(r, g, b, 0.9)
        ctx.move_to(cx + 20, cy + 28)
        ctx.show_text(f"// {k}")
        # Value
        ctx.select_font_face('Inter', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(15)
        ctx.set_source_rgba(0.85, 0.90, 0.98, 0.9)
        ctx.move_to(cx + 20, cy + 54)
        ctx.show_text(v)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    surf.write_to_png(output_path)
    print(f"✅ Generated Horizon Banner: {output_path}")


def render_cyberdeck(output_path=DEFAULT_OUTPUT):
    """Render Cyberdeck HUD / Bento Tech Console."""
    W, H = 1920, 540
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    ctx = cairo.Context(surf)

    # Background
    ctx.set_source_rgb(0.035, 0.047, 0.070)
    ctx.paint()

    # Radial glow
    rad = cairo.RadialGradient(W * 0.7, H * 0.4, 20, W * 0.7, H * 0.4, 600)
    rad.add_color_stop_rgba(0.0, 0.22, 0.74, 0.97, 0.18)
    rad.add_color_stop_rgba(0.5, 0.53, 0.33, 0.97, 0.08)
    rad.add_color_stop_rgba(1.0, 0.0, 0.0, 0.0, 0.0)
    ctx.set_source(rad)
    ctx.paint()

    # Dot grid
    ctx.set_source_rgba(1.0, 1.0, 1.0, 0.04)
    for x in range(40, W - 40, 32):
        for y in range(40, H - 40, 32):
            ctx.arc(x, y, 1.2, 0, 2 * math.pi)
            ctx.fill()

    # Outer frame
    ctx.set_source_rgba(0.22, 0.74, 0.97, 0.25)
    ctx.set_line_width(1.5)
    ctx.rectangle(30, 30, W - 60, H - 60)
    ctx.stroke()

    # Corner brackets
    bracket_len = 24
    corners = [(30, 30, 1, 1), (W - 30, 30, -1, 1), (30, H - 30, 1, -1), (W - 30, H - 30, -1, -1)]
    ctx.set_source_rgba(0.0, 0.94, 1.0, 0.9)
    ctx.set_line_width(3.0)
    for cx, cy, dx, dy in corners:
        ctx.move_to(cx + dx * bracket_len, cy)
        ctx.line_to(cx, cy)
        ctx.line_to(cx, cy + dy * bracket_len)
        ctx.stroke()

    # Top bar text
    ctx.select_font_face('JetBrains Mono', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(18)
    ctx.set_source_rgba(0.0, 0.94, 1.0, 0.85)
    ctx.move_to(65, 75)
    ctx.show_text("// SYSTEM://LJINFINITY  [NODE: 0x01_ALPHA]")

    ctx.set_source_rgba(0.65, 0.72, 0.85, 0.7)
    ctx.set_font_size(16)
    text = "KERNEL: ZEN-LINUX  •  COMPOSITOR: HYPRLAND  •  STATUS: OPERATIONAL"
    extents = ctx.text_extents(text)
    ctx.move_to(W - 65 - extents.width, 75)
    ctx.show_text(text)

    # Horizontal separator
    ctx.set_source_rgba(0.22, 0.74, 0.97, 0.15)
    ctx.set_line_width(1)
    ctx.move_to(65, 95)
    ctx.line_to(W - 65, 95)
    ctx.stroke()

    # Main Title
    ctx.select_font_face('Inter Display', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(86)
    ctx.set_source_rgba(1.0, 1.0, 1.0, 0.98)
    ctx.move_to(65, 230)
    ctx.show_text("JERIN RAJAN")

    # Subtitle
    ctx.select_font_face('JetBrains Mono', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(24)
    ctx.set_source_rgba(0.22, 0.74, 0.97, 0.95)
    ctx.move_to(68, 280)
    ctx.show_text("AI FULL-STACK ARCHITECT  //  LOW-LATENCY SYSTEMS  //  UNIX RICING")

    # Quote
    ctx.select_font_face('Inter', cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(20)
    ctx.set_source_rgba(0.7, 0.75, 0.85, 0.75)
    ctx.move_to(68, 335)
    ctx.show_text('"Work should be an engaging, creative journey — building systems that feel alive."')

    # Badges
    badges = [
        ("🤖 MULTI-AGENT SWARMS", 0.0, 0.94, 1.0),
        ("⚡ RUST & C++ RUNTIMES", 0.65, 0.36, 0.97),
        ("🐚 HYPRLAND + ENOCH RIG", 0.06, 0.73, 0.51),
        ("🎧 J-POP & MODERN JAZZ", 0.98, 0.60, 0.15)
    ]
    bx, by = 68, 415
    for label, r, g, b in badges:
        ctx.select_font_face('JetBrains Mono', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(16)
        ext = ctx.text_extents(label)
        bw = ext.width + 36
        bh = 42

        ctx.set_source_rgba(r, g, b, 0.1)
        rad_corner = 8
        ctx.new_sub_path()
        ctx.arc(bx + bw - rad_corner, by + rad_corner, rad_corner, -math.pi / 2, 0)
        ctx.arc(bx + bw - rad_corner, by + bh - rad_corner, rad_corner, 0, math.pi / 2)
        ctx.arc(bx + rad_corner, by + bh - rad_corner, rad_corner, math.pi / 2, math.pi)
        ctx.arc(bx + rad_corner, by + rad_corner, rad_corner, math.pi, 3 * math.pi / 2)
        ctx.close_path()
        ctx.fill()

        ctx.set_source_rgba(r, g, b, 0.35)
        ctx.set_line_width(1.2)
        ctx.stroke()

        ctx.set_source_rgba(r, g, b, 0.95)
        ctx.move_to(bx + 18, by + 27)
        ctx.show_text(label)
        bx += bw + 16

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    surf.write_to_png(output_path)
    print(f"✅ Generated Cyberdeck Banner: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render aesthetic GitHub profile banner")
    parser.add_argument("--style", choices=["horizon", "cyberdeck"], default="horizon", help="Banner visual style")
    parser.add_argument("--out", default=DEFAULT_OUTPUT, help="Output PNG path")
    args = parser.parse_args()

    if args.style == "horizon":
        render_horizon(args.out)
    elif args.style == "cyberdeck":
        render_cyberdeck(args.out)
