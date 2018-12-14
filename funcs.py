import numpy as np
import math
from PIL import Image, ImageColor


def toHSI(pixel):
    r, g, b = pixel

    # Hue
    top = r - ((1 / 2) * (g + b))
    bot = ((r * r + g * g + b * b) - (r * g + r * b + g * b)) ** 0.5
    hue = math.acos(top / bot)
    hue = hue if b <= g else (2 * math.pi) - hue

    # Saturation
    saturation = 1 - ((3 / (r + g + b)) * (min(r, g, b)))

    # Intensity
    intensity = (r + g + b) / 3

    return [hue, saturation, intensity]


def toRGB(pixel):
    h, s, i = pixel
    r = i * (1 + (
            (s * math.cos(h)) /
            math.cos((math.pi / 3) - h)
    ))
    b = 1 - (1 - s)
    g = (3 * i) - (r + b)
    return [r, g, b]


def compress(image):
    print("\n\nCompressing...")
    width, height = image.size
    print(str.format("{:d}x{:d}", width, height))
    image = np.asarray(image, "int32")
    np.clip(image, 1, 255, image)
    image = np.asarray(image / 256, "float32")
    hue, saturation, intensity = image * 0, image * 0, image * 0
    for y in range(0, width):
        for x in range(0, height):
            [hue[x, y], saturation[x, y], intensity[x, y]] = toHSI(image[x, y])
    return [hue, saturation, intensity]


def decompress(image):
    print(image)
    print("\n\nDecompressing")
    hue, saturation, intensity = image
    image = image * 0
    for x in range(0, len(image)):
        for y in range(0, len(image[0])):
            image[x, y] = toRGB([hue[x, y], saturation[x, y], intensity[x, y]])
            print(image[x, y])
    return image
