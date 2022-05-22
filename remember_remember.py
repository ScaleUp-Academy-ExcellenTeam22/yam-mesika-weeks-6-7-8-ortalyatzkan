import PIL.ImageGrab
from PIL import Image


def get_encrypted_message(image_path: str) -> str:
    """
    A function that gets a path to an image and returns the message encrypted within it by the position of black pixels.
    :param image_path:The path of the encryption image.
    :return:The encrypted message.
    """
    image = PIL.Image.open(image_path, 'r')
    pixels = image.load()
    width, height = image.size
    black_pixels = [row for col in range(width) for row in range(height) if pixels[col, row] == 1]
    string = ''
    return string.join(chr(pixel) for pixel in black_pixels)


if __name__ == '__main__':
    path = 'C:\\Users\\user\\Desktop\\Notebooks-master\\week06\\resources\\code.png'
    print(get_encrypted_message(path))
