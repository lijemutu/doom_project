import base64
import cv2
import textwrap
from string import ascii_letters
from PIL import Image, ImageDraw, ImageFont

def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    '''
    From unutbu on [python PIL draw multiline text on image](https://stackoverflow.com/a/7698300/395857)
    '''
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height

    # Calculate the average length of a single character of our font.
    # Note: this takes into account the specific font and font size.
    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
    # Translate this average length into a character count
    max_char_count = int(image_width * .99 / avg_char_width)
    # Create a wrapped text object using scaled character count

    lines = textwrap.wrap(text, width=max_char_count)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        
        y_text += line_height


def main():
    img = cv2.imread('assets/caco.png')
    jpg_img = cv2.imencode('.png', img)
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    '''
    Testing draw_multiple_line_text
    '''
    #image_width
    image = Image.new('RGB', (1920, 1920), color = (0, 0, 0))
    fontsize = 35 # starting font size
    font = ImageFont.truetype("assets\AmazDooMLeftOutline.ttf", fontsize)
    fontsize2 = 35 # starting font size
    font2 = ImageFont.truetype("assets\AmazDooMLeftOutline.ttf", fontsize2)

    text_color = (200, 200, 200)
    text_start_height = 0
    draw_multiple_line_text(image, b64_string, font, text_color, text_start_height)
    draw_multiple_line_text(image, b64_string, font, text_color, text_start_height)
    draw_multiple_line_text(image, b64_string, font, text_color, text_start_height)
    draw_multiple_line_text(image, b64_string, font, text_color, text_start_height)
   
    text_color = (255, 165, 0)

    draw_multiple_line_text(image, b64_string, font, text_color, 2)
    draw_multiple_line_text(image, b64_string, font, text_color, 2)
    draw_multiple_line_text(image, b64_string, font, text_color, 2)
    text_color = (255, 0, 0)

    draw_multiple_line_text(image, b64_string, font, text_color, 2)
    draw_multiple_line_text(image, b64_string, font, text_color, 2)
    draw_multiple_line_text(image, b64_string, font, text_color, 2)

    image.save('caco_base64.png')
    image.show()
    

if __name__ == "__main__":
    main()
    #cProfile.run('main()') # if you want to do some profiling