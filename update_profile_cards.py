import os
import requests
import xml.sax.saxutils as saxutils
from PIL import Image
import re

def get_avatar():
    url = "https://avatars.githubusercontent.com/u/268110323?v=4"
    r = requests.get(url)
    if r.status_code == 200:
        with open("avatar.png", "wb") as f:
            f.write(r.content)
    return "avatar.png"

def image_to_ascii(img_path, width, height, invert=False):
    img = Image.open(img_path).convert('L')
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    chars = [' ', '.', ':', '-', '=', '+', '*', '%', '#', '@']
    if invert:
        chars = chars[::-1]
    
    lines = []
    for y in range(height):
        line = ''
        for x in range(width):
            p = img.getpixel((x, y))
            idx = int(p / 256 * len(chars))
            idx = min(idx, len(chars) - 1)
            line += chars[idx]
        lines.append(line)
    return lines

def update_svg_file(svg_path, width, height, invert, fill_color):
    ascii_lines = image_to_ascii('avatar.png', width, height, invert=invert)
    
    with open(svg_path, 'r', encoding='utf-8') as f:
        file_lines = f.readlines()
        
    ascii_idx = 0
    new_file_lines = []
    
    for line in file_lines:
        match = re.search(r'<text x="28" y="([^"]+)" fill="[^"]+" font-family="[^"]+" xml:space="preserve" font-size="8">(.*?)</text>', line)
        if match:
            y_val = match.group(1)
            if ascii_idx < len(ascii_lines):
                escaped_text = saxutils.escape(ascii_lines[ascii_idx])
                new_line = f'  <text x="28" y="{y_val}" fill="{fill_color}" font-family="\'Consolas\', \'Menlo\', \'DejaVu Sans Mono\', monospace" xml:space="preserve" font-size="8">{escaped_text}</text>\n'
                new_file_lines.append(new_line)
                ascii_idx += 1
            else:
                new_file_lines.append(line)
        else:
            new_file_lines.append(line)

    with open(svg_path, 'w', encoding='utf-8') as f:
        f.writelines(new_file_lines)
    print(f"Successfully replaced {ascii_idx} ASCII lines in {svg_path}")

if __name__ == '__main__':
    get_avatar()
    # Dark mode: 37 lines, width 65, fill #c9d1d9
    update_svg_file('dark_mode.svg', 65, 37, invert=False, fill_color='#c9d1d9')
    
    # Light mode: 50 lines, width 96, fill #24292f
    update_svg_file('light_mode.svg', 96, 50, invert=True, fill_color='#24292f')
