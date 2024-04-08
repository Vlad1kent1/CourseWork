from copy import copy
import numpy as np
from PIL import Image


def load_standards(paths):
    x = []
    for path in paths:
        standard = read_image(path)
        x.append(standard)
    return x


def read_image(file_name):
    img = Image.open(file_name)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pix = img.load()
    width, height = img.size
    t = []
    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            if (r, g, b) != (0, 0, 0):
                t.append(-1)
            else:
                t.append(1)
    return t


def action(s, T):
    if s <= 0:
        return 0
    elif 0 < s <= T:
        return s
    elif s > T:
        return T


path = ["first_image.png", "second_image.png"]
standards = load_standards(path)
test_images = ["test_image1.png", "test_image2.png", "test_image3.png"]

for img in test_images:
    y = read_image(img)
    n = len(standards[0])
    m = len(standards)
    w = [[standards[i][j] / 2 for j in range(n)] for i in range(m)]
    T = n / 2
    Emax = 1
    e = 1 / n
    Y = [[action(sum([y[i] * w[j][i] for i in range(n)]), T) for j in range(m)], [[]]]
    Y[1] = copy(Y[0])
    while 1:
        temp_y = copy(Y[1])
        for j in range(m):
            c = sum(Y[1][0:j])
            d = sum(Y[1][j + 1:])
            s = Y[1][j] - e * (c + d)
            Y[1][j] = action(s, T)
        if np.linalg.norm(np.array(Y[1]) - np.array(temp_y)) < Emax:
            break
    print(f"for image \"{img}\" result is:{Y[1]}")
