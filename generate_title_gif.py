import os
import shutil
import subprocess
from PIL import Image, ImageDraw, ImageFont

def create_animated_gif():
    frames_dir = "/tmp/title_frames_v2"
    if os.path.exists(frames_dir):
        shutil.rmtree(frames_dir)
    os.makedirs(frames_dir, exist_ok=True)

    width, height = 800, 110
    bg_rgb = (13, 17, 23) # Exact GitHub Dark Mode background (#0D1117)
    
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
        font = ImageFont.truetype(font_path, 60)
    else:
        font = ImageFont.load_default()

    # Exact Vibrant Colors:
    blue_color = (56, 189, 248) # #38BDF8 (Vibrant Cyan Blue)
    red_color = (255, 40, 40)   # #FF2828 (Vibrant Intense Neon Red)

    def draw_text_frame(text, color):
        img = Image.new("RGB", (width, height), bg_rgb)
        draw = ImageDraw.Draw(img)
        
        bbox = font.getbbox(text) if hasattr(font, "getbbox") else (0, 0, font.getsize(text)[0], font.getsize(text)[1])
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = (width - text_w) // 2
        y = (height - text_h) // 2 - bbox[1]

        # Draw crisp, sharp text with 1px outline for maximum contrast & zero blurriness
        for ox, oy in [(-2,0), (2,0), (0,-2), (0,2), (-1,-1), (1,1), (-1,1), (1,-1)]:
            draw.text((x + ox, y + oy), text, font=font, fill=(5, 5, 5))
            
        draw.text((x, y), text, font=font, fill=color)
        return img

    frame_count = 0

    # Text 1: Jerin Rajan (Cyan Blue)
    text1 = "Jerin Rajan"
    for i in range(1, len(text1) + 1):
        frame_img = draw_text_frame(text1[:i] + "|", blue_color)
        for _ in range(3): # 30 FPS timing
            frame_img.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
            frame_count += 1
    
    full_text1_frame = draw_text_frame(text1, blue_color)
    for _ in range(45): # Hold 1.5 seconds @ 30 FPS
        full_text1_frame.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
        frame_count += 1

    for i in range(len(text1) - 1, -1, -1):
        txt = text1[:i] + "|" if i > 0 else ""
        frame_img = draw_text_frame(txt, blue_color)
        for _ in range(2):
            frame_img.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
            frame_count += 1

    # Text 2: LJ INFINITY (Vibrant Red)
    text2 = "LJ INFINITY"
    for i in range(1, len(text2) + 1):
        frame_img = draw_text_frame(text2[:i] + "|", red_color)
        for _ in range(3):
            frame_img.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
            frame_count += 1
        
    full_text2_frame = draw_text_frame(text2, red_color)
    for _ in range(45): # Hold 1.5 seconds @ 30 FPS
        full_text2_frame.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
        frame_count += 1

    for i in range(len(text2) - 1, -1, -1):
        txt = text2[:i] + "|" if i > 0 else ""
        frame_img = draw_text_frame(txt, red_color)
        for _ in range(2):
            frame_img.save(os.path.join(frames_dir, f"frame_{frame_count:04d}.png"))
            frame_count += 1

    output_gif = "/home/lj/Work/Me/title_animated_v2.gif"
    
    # FFmpeg palettegen with diff stats_mode ensures 100% exact Red & Blue color preservation
    cmd = [
        "ffmpeg", "-y", "-framerate", "30",
        "-i", f"{frames_dir}/frame_%04d.png",
        "-vf", "fps=30,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen=stats_mode=full[p];[s1][p]paletteuse=dither=bayer:bayer_scale=5",
        output_gif
    ]
    subprocess.run(cmd, check=True)
    print("Successfully encoded ultra-sharp title_animated_v2.gif with sharp red/blue colors!")

if __name__ == "__main__":
    create_animated_gif()
