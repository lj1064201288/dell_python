from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    fillcolor = "#ff0000"
    width, height = img.size
    print(width, height)
    draw.text((width-40, 0), '5', fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('Image.jpg')
    add_num(image)