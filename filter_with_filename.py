from PIL import Image
import numpy as np


def refactor_pixels(pixels, i, j, step, pixel_size):
    """
        change brightness and color of image's pixels
        :param pixels: numpy image array
        :param i: start width index i
        :param j: start height index j
        :param step: color's deep step
        :param pixel_size: size of pixels block
        :return:
    """
    middle_brightness = int(int(np.sum(pixels[i:i + pixel_size, j:j + pixel_size])) // 3 // (pixel_size ** 2))
    pixels[i: i + pixel_size, j: j + pixel_size] = int(middle_brightness // step) * step


def pixelation(pixels, step, pixel_size):
    """
        Нарезка массива значений пикселей на блоки моззаики и последующее их изменение
        :param pixels: numpy image array
        :param step: color's deep step
        :param pixel_size: size of pixels block
        :return: changed numpu array of image's brightness and colors

        >>> pixelation(np.array([[100, 50, 20, 10], [30, 40, 20, 90], [60, 45, 23, 57], [23, 46, 128, 100]]), 3, 4)
        array([[15, 15, 15, 15],
               [15, 15, 15, 15],
               [15, 15, 15, 15],
               [15, 15, 15, 15]])
    """
    width = len(pixels)
    height = len(pixels[1])
    pixels = pixels[:width // pixel_size * pixel_size, :height // pixel_size * pixel_size]
    width = len(pixels)
    height = len(pixels[1])
    for i in range(0, width - pixel_size + 1, pixel_size):
        for j in range(0, height - pixel_size + 1, pixel_size):
            refactor_pixels(pixels, i, j, step, pixel_size)
    return pixels


img = Image.open('img2.jpg')
pixels = np.array(img)
res = Image.fromarray(pixelation(pixels, 50, 10))
res.save('res.jpg')
