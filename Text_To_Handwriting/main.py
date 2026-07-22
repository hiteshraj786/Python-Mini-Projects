# import pywhatkit as pw

# txt = """Python is a high-level, interpreted, general-purpose programming language. Created b
# y Guido van Rossum and first released in 1991, its design philosophy emphasizes code readability, 
# particularly through the use of significant indentation. """

# pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
# print(" END ")

from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (800, 400), color='white')
d = ImageDraw.Draw(img)

# Update the font file name here:
font_path = "Ashley Southine Demo.ttf"
font = ImageFont.truetype(font_path, 24)

text = """Python is a high-level, interpreted, general-purpose programming language.
Created by Guido van Rossum and first released in 1991.
Its design philosophy emphasizes code readability,
particularly through the use of significant indentation."""

d.text((10, 10), text, fill=(0, 0, 138), font=font)

img.save("demo1.png")
print("✅ Handwriting image saved as demo1.png")
