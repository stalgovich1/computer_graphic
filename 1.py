from PIL import Image, ImageDraw
img = Image.new('L', (960, 540), 255)
draw = ImageDraw.Draw(img)
with open("D:\comp_graph\lab2\DS6.txt", "r") as file:
    for line in file:
        coords_list = line.split()
        i = int(coords_list[1])
        j = int(coords_list[0])
        draw.line((i, j, i + 1, j + 1))
img.show()
img.save('result.png')