from PIL import Image

chars = "@%#*+=-:. "[::-1]

def image_to_ascii(img_path, new_width=100):
    img = Image.open(img_path).convert('L')
    width, height = img.size
    ratio = (height / 2.2) / width
    new_height = int(new_width * ratio)
    img = img.resize((new_width, new_height))
    pixels = img.getdata()
    ascii_str = ''.join(chars[pixel * (len(chars) - 1) // 255] for pixel in pixels)
    ascii_str = [ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)]
    return '\n'.join(ascii_str)
