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
    bg_rgb = (13, 17, 23) # Exact GitHub Dark Mode background (#0D1117)

    font_paths = [
        "/usr/share/fonts/adwaita-mono-fonts/AdwaitaMono-Bold.ttf",
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf",
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
    prefix_color = (148, 163, 184) # #94A3B8 (Slate Gray)

    words_info = [
        ("THINK", (56, 189, 248)),    # #38BDF8 (Vibrant Cyan)
        ("CREATE", (168, 85, 247)),   # #A855F7 (Vibrant Purple)
        ("EXPLORE", (34, 197, 94)),   # #22C55E (Vibrant Green)
        ("BUILD", (245, 158, 11)),    # #F59E0B (Vibrant Amber)
        ("INNOVATE", (244, 63, 94))   # #F43F5E (Vibrant Rose)
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

        # Word canvas
        word_canvas = Image.new("RGB", (max_word_w + 60, height), bg_rgb)
        w_draw = ImageDraw.Draw(word_canvas)

        # Draw Word 1 (moving up out of frame)
        if word1_text:
            bbox1 = font.getbbox(word1_text)
            w1_y = (center_y - (bbox1[3] - bbox1[1]) // 2 - bbox1[1]) + offset_y
            
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

        # 1. Hold steady phase: 20 frames @ 40ms (800ms hold)
        hold_img = render_frame(w1_text, w1_color, None, None, 0)
        for _ in range(20):
            frames.append(hold_img)
            durations.append(40) # 25 FPS non-throttled browser speed

        # 2. Smooth Cubic Eased Slide-Up Transition: 10 frames @ 30ms (300ms transition)
        transition_steps = 10
        for s in range(1, transition_steps + 1):
            progress = s / float(transition_steps)
            eased_progress = cubic_ease_in_out(progress)
            offset_y = int(round(-height * eased_progress))
            
            frames.append(render_frame(w1_text, w1_color, w2_text, w2_color, offset_y))
            durations.append(30) # 33 FPS non-throttled speed

    # Master Color Palette: Force inclusion of all vibrant text colors
    master = Image.new("RGB", (width, height * len(words_info)), bg_rgb)
    m_draw = ImageDraw.Draw(master)
    for idx, (w_text, w_col) in enumerate(words_info):
        m_draw.text((10, idx * height + 15), w_text, font=font, fill=w_col)
    m_draw.text((10, 0), prefix_text, font=font, fill=prefix_color)
    
    palette_img = master.quantize(colors=256, method=Image.Quantize.MEDIANCUT)

    quantized_frames = [f.quantize(palette=palette_img) for f in frames]

    output_gif = "/home/lj/Work/Me/live_to_header_v3.gif"
    quantized_frames[0].save(
        output_gif,
        save_all=True,
        append_images=quantized_frames[1:],
        duration=durations,
        loop=0
    )
    print("Successfully generated live_to_header_v3.gif with 25 FPS non-throttled smooth speed and vibrant colors!")

if __name__ == "__main__":
    create_live_to_gif()
