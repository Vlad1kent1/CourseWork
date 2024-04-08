from PIL import Image, ImageDraw

img_size = 4  # px


def image_generate(coloring: list[list[int]], file_name):
    img = Image.new("L", (img_size, img_size))
    draw = ImageDraw.Draw(img)
    try:
        for i in range(img_size):
            for j in range(img_size):
                draw.point((i, j), fill=coloring[j][i])
    except Exception as e:
        print(e)
    else:
        img.save(f"{file_name}.png")
    finally:
        del draw


first_image_pixels = [[0, 255, 255, 255], [0, 255, 255, 255], [0, 255, 255, 255], [0, 0, 0, 0]]
second_image_pixels = [[0, 0, 0, 0], [0, 255, 255, 0], [0, 0, 0, 0], [0, 255, 255, 255]]

image_generate(first_image_pixels, "first_image")
image_generate(second_image_pixels, "second_image")

test_img_pixels1 = [[0, 0, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255]]
test_img_pixels2 = [[0, 255, 255, 255], [0, 255, 255, 255], [0, 255, 255, 255], [0, 255, 255, 255]]
test_img_pixels3 = [[255, 255, 255, 255], [0, 255, 255, 255], [0, 0, 0, 0], [0, 255, 255, 255]]
#
# image_generate(test_img_pixels1, "test_image1")
# image_generate(test_img_pixels2, "test_image2")
image_generate(test_img_pixels3, "test_image3")

