import os
import shutil
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_animated_gif():
    frames_dir = "/tmp/title_frames"
    if os.path.exists(frames_dir):
        shutil.rmtree(frames_dir)
    os.makedirs(frames_dir, exist_ok=True)

    width, height = 800, 120
    bg_rgb = (13, 17, 23) # #0D1117
    
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
        img = Image.new("RGB", (width, height), bg_rgb)
        
        bbox = font.getbbox(text) if hasattr(font, "getbbox") else (0, 0, font.getsize(text)[0], font.getsize(text)[1])
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = (width - text_w) // 2
        y = (height - text_h) // 2 - bbox[1]

        glow_layer = Image.new("RGB", (width, height), bg_rgb)
        glow_draw = ImageDraw.Draw(glow_layer)
        glow_draw.text((x, y), text, font=font, fill=color)
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(radius=6))

        img = Image.blend(img, glow_layer, alpha=0.6)
        draw = ImageDraw.Draw(img)
        draw.text((x, y), text, font=font, fill=color)
        
        return img

    frame_count = 0

    # Text 1: Jerin Rajan (Blue)
    text1 = "Jerin Rajan"
    for i in range(1, len(text1) + 1):
        frame_img = draw_text_frame(text1[:i] + "|", blue_color)
        for _ in range(4): # 60 FPS hold per char
            frame_img.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
            frame_count += 1
    
    full_text1_frame = draw_text_frame(text1, blue_color)
    for _ in range(90): # Hold 1.5s
        full_text1_frame.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
        frame_count += 1

    for i in range(len(text1) - 1, -1, -1):
        txt = text1[:i] + "|" if i > 0 else ""
        frame_img = draw_text_frame(txt, blue_color)
        for _ in range(3):
            frame_img.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
            frame_count += 1

    # Text 2: LJ INFINITY (Red)
    text2 = "LJ INFINITY"
    for i in range(1, len(text2) + 1):
        frame_img = draw_text_frame(text2[:i] + "|", red_color)
        for _ in range(4):
            frame_img.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
            frame_count += 1
        
    full_text2_frame = draw_text_frame(text2, red_color)
    for _ in range(90): # Hold 1.5s
        full_text2_frame.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
        frame_count += 1

    for i in range(len(text2) - 1, -1, -1):
        txt = text2[:i] + "|" if i > 0 else ""
        frame_img = draw_text_frame(txt, red_color)
        for _ in range(3):
            frame_img.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
            frame_count += 1

    output_gif = "/home/lj/Work/Me/title_animated.gif"
    cmd = [
        "ffmpeg", "-y", "-framerate", "60",
        "-i", f"{frames_dir}/frame_%04d.png",
        "-vf", "fps=60,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen=stats_mode=single[p];[s1][p]paletteuse=dither=sierra2_4a",
        output_gif
    ]
    subprocess.run(cmd, check=True)
    print("Successfully encoded 60 FPS broadcast-quality title_animated.gif with FFmpeg!")

if __name__ == "__main__":
    create_animated_gif()
