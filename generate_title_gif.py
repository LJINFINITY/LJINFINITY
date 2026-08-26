import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_animated_gif():
    width, height = 650, 95
    bg_color = (13, 17, 23, 0)
    
    font_paths = [
        "/usr/share/fonts/dejavu-sans-mono-fonts/DejaVuSansMono-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSansMono-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
        "/usr/share/fonts/liberation-mono/LiberationMono-Bold.ttf",
        "/usr/share/fonts/gnu-free/FreeMonoBold.ttf"
    ]
    
    font_path = None
    for p in font_paths:
        if os.path.exists(p):
            font_path = p
            break
            
    if font_path:
        font = ImageFont.truetype(font_path, 54)
    else:
        font = ImageFont.load_default()

    blue_color = (56, 189, 248) # #38BDF8
    red_color = (239, 68, 68)   # #EF4444

    def draw_text_frame(text, color):
        img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        
        bbox = font.getbbox(text) if hasattr(font, "getbbox") else (0, 0, font.getsize(text)[0], font.getsize(text)[1])
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = (width - text_w) // 2
        y = (height - text_h) // 2 - bbox[1]

        # Draw intense neon glow
        glow_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow_img)
        glow_draw.text((x, y), text, font=font, fill=color + (200,))
        glow_img = glow_img.filter(ImageFilter.GaussianBlur(radius=6))

        draw = ImageDraw.Draw(img)
        img.paste(glow_img, (0, 0), glow_img)
        draw.text((x, y), text, font=font, fill=color + (255,))
        
        return img

    frames = []
    durations = []

    # Text 1: Jerin Rajan (Blue)
    text1 = "Jerin Rajan"
    for i in range(1, len(text1) + 1):
        frames.append(draw_text_frame(text1[:i] + "█", blue_color))
        durations.append(80)
    
    # Hold full text
    full_text1_frame = draw_text_frame(text1, blue_color)
    for _ in range(20):
        frames.append(full_text1_frame)
        durations.append(80)

    # Erase text 1
    for i in range(len(text1) - 1, -1, -1):
        txt = text1[:i] + "█" if i > 0 else ""
        frames.append(draw_text_frame(txt, blue_color))
        durations.append(50)

    # Text 2: LJ INFINITY (Red)
    text2 = "LJ INFINITY"
    for i in range(1, len(text2) + 1):
        frames.append(draw_text_frame(text2[:i] + "█", red_color))
        durations.append(80)
        
    # Hold full text
    full_text2_frame = draw_text_frame(text2, red_color)
    for _ in range(20):
        frames.append(full_text2_frame)
        durations.append(80)

    # Erase text 2
    for i in range(len(text2) - 1, -1, -1):
        txt = text2[:i] + "█" if i > 0 else ""
        frames.append(draw_text_frame(txt, red_color))
        durations.append(50)

    # Save GIF
    frames[0].save(
        "/home/lj/Work/Me/title_animated.gif",
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        disposal=2
    )
    print("Successfully generated enlarged title_animated.gif (54px font)!")

if __name__ == "__main__":
    create_animated_gif()
