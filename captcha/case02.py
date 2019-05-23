import tesserocr

for i in range(1,11):
    captcha = 'img/code_{}.png'.format(i)
    result = tesserocr.file_to_text(captcha).strip()
    print(result)