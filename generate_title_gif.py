import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_animated_gif():
    width, height = 800, 120
    bg_rgb = (13, 17, 23) # GitHub exact Dark Mode background (#0D1117)
    
    font_paths = [
        "/usr/share/fonts/adwaita-mono-fonts/AdwaitaMono-Bold.ttf",
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu-sans-mono-fonts/DejaVuSansMono-Bold.ttf",
        "/usr/share/fonts/gnu-free/FreeSansBold.ttf"
    ]
    
    font_path = None
    for p in font_paths:
        if os.path.exists(p):
            font_path = p
            break
            
    print("Using TTF font path:", font_path)
    if font_path:
        font = ImageFont.truetype(font_path, 64)
    else:
        font = ImageFont.load_default()

    blue_color = (56, 189, 248) # #38BDF8
    red_color = (239, 68, 68)   # #EF4444

    def draw_text_frame(text, color):
        # Base image with solid GitHub dark mode background
        img = Image.new("RGB", (width, height), bg_rgb)
        
        bbox = font.getbbox(text) if hasattr(font, "getbbox") else (0, 0, font.getsize(text)[0], font.getsize(text)[1])
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = (width - text_w) // 2
        y = (height - text_h) // 2 - bbox[1]

        # Draw smooth neon glow blended directly on dark background
        glow_layer = Image.new("RGB", (width, height), bg_rgb)
        glow_draw = ImageDraw.Draw(glow_layer)
        glow_draw.text((x, y), text, font=font, fill=color)
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(radius=8))

        # Blend glow and draw crisp text
        img = Image.blend(img, glow_layer, alpha=0.7)
        draw = ImageDraw.Draw(img)
        draw.text((x, y), text, font=font, fill=color)
        
        return img

    frames = []
    durations = []

    # Text 1: Jerin Rajan (Blue)
    text1 = "Jerin Rajan"
    for i in range(1, len(text1) + 1):
        frames.append(draw_text_frame(text1[:i] + "|", blue_color))
        durations.append(80)
    
    # Hold full text
    full_text1_frame = draw_text_frame(text1, blue_color)
    for _ in range(22):
        frames.append(full_text1_frame)
        durations.append(80)

    # Erase text 1
    for i in range(len(text1) - 1, -1, -1):
        txt = text1[:i] + "|" if i > 0 else ""
        frames.append(draw_text_frame(txt, blue_color))
        durations.append(50)

    # Text 2: LJ INFINITY (Red)
    text2 = "LJ INFINITY"
    for i in range(1, len(text2) + 1):
        frames.append(draw_text_frame(text2[:i] + "|", red_color))
        durations.append(80)
        
    # Hold full text
    full_text2_frame = draw_text_frame(text2, red_color)
    for _ in range(22):
        frames.append(full_text2_frame)
        durations.append(80)

    # Erase text 2
    for i in range(len(text2) - 1, -1, -1):
        txt = text2[:i] + "|" if i > 0 else ""
        frames.append(draw_text_frame(txt, red_color))
        durations.append(50)

    # Save GIF with solid background & optimal palette
    frames[0].save(
        "/home/lj/Work/Me/title_animated.gif",
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=True
    )
    print("Successfully generated title_animated.gif with solid GitHub dark background!")

if __name__ == "__main__":
    create_animated_gif()
