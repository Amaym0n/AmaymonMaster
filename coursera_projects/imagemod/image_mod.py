from PIL import Image
from PIL import ImageFont, ImageDraw
from IPython.display import display

# read image and convert to RGB
image=Image.open("rick-and-morty-3.jpg").convert('RGB')
width, height = image.size
all_copies  = list()
for i in [0, 1, 2]:
    for val in [0.1, 0.5, 0.9]:
        im = image.copy()
        for w in range(width):
            for h in range(height):
                r, g, b = im.getpixel((w, h))
                if i==0: im.putpixel((w, h), (int(r*val), g, b))
                elif i==1: im.putpixel((w, h), (r, int(g*val), b))
                else: im.putpixel((w, h), (r, g, int(b*val)))
        all_copies.append([im, 'channel {} intensity {}'.format(i, val)])

x, y = 0, 0
font = ImageFont.truetype("arial.ttf", 60)
contact_sheet = Image.new('RGB', (width * 3, height * 3 + 3 * 80))
draw = ImageDraw.Draw(contact_sheet)
for pict in all_copies:
    draw.text((x, y + height), pict[1], font=font, fill='white')
    contact_sheet.paste(pict[0], (x, y))
    if (x + width) == contact_sheet.width: x, y = 0, (y + height + 80)
    else: x += width
display(contact_sheet.show())