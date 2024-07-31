from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#FFFFFF"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size


def make_certificates(name):
    """Function to save certificates as a .png file"""

    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)

    # Finding the bounding box of the text.
    # The 'textsize' method has been deprecated and replaced by the 'textbbox' method in newer versions of Pillow
    bbox = draw.textbbox((0, 0), name, font=FONT_FILE)
    name_width = bbox[2] - bbox[0]
    name_height = bbox[3] - bbox[1]

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name + ".png")
    print('Saving Certificate of:', name)


if __name__ == "__main__":

    names = ['Tushar Nankani', "Full Name", 'Some Long Ass Name Might Not Work']
    for name in names:
        make_certificates(name)

    print(len(names), "certificates done.")
