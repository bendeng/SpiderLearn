import tesserocr
from PIL import Image

for i in range(1,11):
    captcha = 'img/code_{}.png'.format(i)
    image = Image.open(captcha)
    result = tesserocr.image_to_text(image).strip()
    print(result)