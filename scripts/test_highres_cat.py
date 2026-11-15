from PIL import Image, ImageDraw, ImageFont

def draw_cyber_cat_bitmap():
    # Render a stylized high-res cat bust with geometric cyber lines
    w, h = 64, 40
    img = Image.new('L', (w, h), 0)
    draw = ImageDraw.Draw(img)

    # Ears (Polygonal ears)
    # Left Ear
    draw.polygon([(10, 2), (24, 18), (14, 22)], fill=200)
    draw.polygon([(13, 6), (22, 17), (16, 20)], fill=255) # inner ear glow
    # Right Ear
    draw.polygon([(53, 2), (39, 18), (49, 22)], fill=200)
    draw.polygon([(50, 6), (41, 17), (47, 20)], fill=255) # inner ear glow

    # Head Crown & Brow
    draw.polygon([(24, 18), (39, 18), (36, 12), (27, 12)], fill=180)

    # Cheeks & Face Shape
    draw.polygon([
        (14, 22), (24, 18), (39, 18), (49, 22),
        (54, 29), (48, 36), (32, 39), (15, 36), (9, 29)
    ], fill=150)

    # Eye cutouts (dark)
    draw.polygon([(18, 24), (27, 23), (25, 27), (19, 27)], fill=30)
    draw.polygon([(36, 23), (45, 24), (44, 27), (38, 27)], fill=30)

    # Glowing pupils (bright)
    draw.rectangle([21, 24, 24, 26], fill=255)
    draw.rectangle([39, 24, 42, 26], fill=255)

    # Nose & Muzzle
    draw.polygon([(30, 29), (33, 29), (32, 32)], fill=255)
    draw.line([(32, 32), (32, 34)], fill=220, width=1)
    draw.line([(28, 34), (32, 34), (36, 34)], fill=220, width=1)

    # Whiskers
    draw.line([(6, 28), (20, 30)], fill=230, width=1)
    draw.line([(4, 32), (20, 32)], fill=230, width=1)
    draw.line([(6, 36), (20, 34)], fill=230, width=1)

    draw.line([(57, 28), (43, 30)], fill=230, width=1)
    draw.line([(59, 32), (43, 32)], fill=230, width=1)
    draw.line([(57, 36), (43, 34)], fill=230, width=1)

    # Convert to dense ASCII
    chars = " .:-=+*#%@"
    # Or block chars: " ░▒▓█"
    block_chars = " ░▒▓█"
    
    ascii_lines = []
    for y in range(h):
        line = ""
        for x in range(w):
            v = img.getpixel((x, y))
            idx = int(v / 256 * len(block_chars))
            idx = min(idx, len(block_chars) - 1)
            line += block_chars[idx]
        if line.strip():
            ascii_lines.append(line)
            
    return "\n".join(ascii_lines)

print(draw_cyber_cat_bitmap())
