import tesserocr
from PIL import Image

for i in range(1,11):
    captcha = 'img/code_{}.png'.format(i)
    image = Image.open(captcha)

    image = image.convert('L')

    threshold = 127
    table = []
    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)

    image = image.point(table, '1')
    image.show()

    result = tesserocr.image_to_text(image).strip()
    print(result)