import os
import math
from PIL import Image, ImageDraw, ImageFont

def cubic_ease_in_out(t):
    if t < 0.5:
        return 4.0 * t * t * t
    else:
        return 1.0 - math.pow(-2.0 * t + 2.0, 3) / 2.0

def create_live_to_gif():
    width, height = 750, 70
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
        font = ImageFont.truetype(font_path, 34)
    else:
        font = ImageFont.load_default()

    prefix_text = "LIVE TO "
    prefix_color = (148, 163, 184) # #94A3B8

    words_info = [
        ("THINK", (56, 189, 248)),    # #38BDF8 (Cyan)
        ("CREATE", (139, 92, 246)),   # #8B5CF6 (Purple)
        ("EXPLORE", (16, 185, 129)),  # #10B981 (Emerald)
        ("BUILD", (245, 158, 11)),    # #F59E0B (Amber)
        ("INNOVATE", (236, 72, 153))  # #EC4899 (Rose)
    ]

    max_word_w = max([font.getbbox(w[0])[2] - font.getbbox(w[0])[0] for w in words_info])
    prefix_w = font.getbbox(prefix_text)[2] - font.getbbox(prefix_text)[0]
    total_w = prefix_w + max_word_w
    
    start_x = (width - total_w) // 2
    prefix_x = start_x
    word_x = prefix_x + prefix_w
    center_y = height // 2

    def render_frame(word1_text, word1_color, word2_text, word2_color, offset_y):
        img = Image.new("RGB", (width, height), bg_rgb)
        draw = ImageDraw.Draw(img)

        # Draw static prefix "LIVE TO "
        bbox_prefix = font.getbbox(prefix_text)
        py = center_y - (bbox_prefix[3] - bbox_prefix[1]) // 2 - bbox_prefix[1]
        draw.text((prefix_x, py), prefix_text, font=font, fill=prefix_color)

        # Word canvas with explicit bounding clip
        word_canvas = Image.new("RGB", (max_word_w + 60, height), bg_rgb)
        w_draw = ImageDraw.Draw(word_canvas)

        # Draw Word 1 (moving up out of frame)
        if word1_text:
            bbox1 = font.getbbox(word1_text)
            w1_y = (center_y - (bbox1[3] - bbox1[1]) // 2 - bbox1[1]) + offset_y
            # 1px outline for crisp neon contrast
            for ox, oy in [(-1,0), (1,0), (0,-1), (0,1)]:
                w_draw.text((10 + ox, w1_y + oy), word1_text, font=font, fill=(0, 0, 0))
            w_draw.text((10, w1_y), word1_text, font=font, fill=word1_color)

        # Draw Word 2 (moving up into frame from below)
        if word2_text:
            bbox2 = font.getbbox(word2_text)
            w2_y = (center_y - (bbox2[3] - bbox2[1]) // 2 - bbox2[1]) + offset_y + height
            for ox, oy in [(-1,0), (1,0), (0,-1), (0,1)]:
                w_draw.text((10 + ox, w2_y + oy), word2_text, font=font, fill=(0, 0, 0))
            w_draw.text((10, w2_y), word2_text, font=font, fill=word2_color)

        img.paste(word_canvas, (word_x - 5, 0))
        return img

    frames = []
    durations = []

    num_words = len(words_info)
    for idx in range(num_words):
        w1_text, w1_color = words_info[idx]
        w2_text, w2_color = words_info[(idx + 1) % num_words]

        # 1. Steady Hold Phase (1.2 seconds @ 80ms = 15 frames)
        hold_img = render_frame(w1_text, w1_color, None, None, 0)
        for _ in range(15):
            frames.append(hold_img)
            durations.append(80)

        # 2. Smooth Cubic Eased Slide-Up Transition (360ms @ 30ms = 12 cubic-eased frames)
        transition_steps = 12
        for s in range(1, transition_steps + 1):
            progress = s / float(transition_steps)
            eased_progress = cubic_ease_in_out(progress)
            offset_y = int(round(-height * eased_progress))
            
            frames.append(render_frame(w1_text, w1_color, w2_text, w2_color, offset_y))
            durations.append(30)

    # Save GIF with exact color palette retention
    frames[0].save(
        "/home/lj/Work/Me/live_to_header.gif",
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=False
    )
    print("Successfully generated ultra-crisp, perfectly animated live_to_header.gif!")

if __name__ == "__main__":
    create_live_to_gif()
