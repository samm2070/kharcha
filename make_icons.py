from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('icons', exist_ok=True)

for size in [192, 512]:
    img = Image.new('RGB', (size, size), color='#0f172a')
    draw = ImageDraw.Draw(img)
    
    # Draw a rounded rect card shape as bg
    margin = size // 8
    draw.rounded_rectangle([margin, margin, size-margin, size-margin], radius=size//8, fill='#1e293b')
    
    # Rupee symbol
    font_size = size // 3
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size)
    except:
        font = ImageFont.load_default()
    
    text = '₹'
    bbox = draw.textbbox((0,0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (size - tw) // 2
    y = (size - th) // 2
    draw.text((x, y), text, fill='#3b82f6', font=font)
    
    img.save(f'icons/icon-{size}.png')
    print(f'icon-{size}.png created')
