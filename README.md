# Doom base64 images sprites

Python script to turn any image into a image with the base64 binary transformation into a text into a image.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install opencv-python
pip install Pillow
```

## Usage

```python
# Your image on some folder
img = cv2.imread('assets/caco.png')
jpg_img = cv2.imencode('.png', img)
b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
'''
Testing draw_multiple_line_text
'''
# image_width
image = Image.new('RGB', (1920, 1920), color = (0, 0, 0))
fontsize = 35 # starting font size
#Custom font if you want
font = ImageFont.truetype("assets\AmazDooMLeftOutline.ttf", fontsize)

text_color = (200, 200, 200)
text_start_height = 0
draw_multiple_line_text(image, b64_string, font, text_color, text_start_height)
# Save image
image.save('caco_base64.png')
image.show()
```

## Contributing
Sure
## License
[MIT](https://choosealicense.com/licenses/mit/)