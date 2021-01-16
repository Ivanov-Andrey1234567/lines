import random
from PIL import Image, ImageDraw

img = Image.new("RGBA", (600, 600), "white")
idraw = ImageDraw.Draw(img)

# img2 = Image.new('RGBA', (50, 50))
# img2.save("line.png", "PNG")
# idraw2 = ImageDraw.Draw(img2)
# img2.show()

li = []
for y in range(0, 100, 5):
    y1 = y * 5
    y2 = (y1 - y / 100) * 3.14
    li.append([])
    for x in range(0, 100, 5):
        x1 = x * 5
        x2 = x1 + 5
        li[y // 5].append([x1, y1])
        idraw.point((x1, y1), 'black')
        idraw.line((x1, y1, x2, y2), 'black')

print(li)

# for _ in range(30):
#     idraw.line((random.randint(0, 50), random.randint(0, 300), 600, random.randint(70, 600)), 'blue')  # line (x1, y1)   (x2, Y2)

img.save('canvas.png')
img.show()
# img2.show()
