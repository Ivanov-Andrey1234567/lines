import math
import random

from PIL import Image, ImageDraw
from Perlin_noise import PerlinNoiseFactory

img = Image.new("RGBA", (300, 300), "white")
idraw = ImageDraw.Draw(img)

width = 1000
height = 1000

left_x = int(width * -0.5)
right_x = int(width * 1.5)
top_y = int(height * -0.5)
bottom_y = int(height * 1.5)
resolution = int(width * 0.01)
num_columns = int((right_x - left_x) / resolution)
num_rows = int((bottom_y - top_y) / resolution)

noise = PerlinNoiseFactory(2, tile=(0, 3))

grid = []
for e in range(num_columns):
    grid.append([])
    for j in range(num_rows):
        grid[e].append([])

default_angle = math.pi * 0.25
for column in range(num_columns):
    for row in range(num_rows):
        scaled_x = column * 0.005
        scaled_y = row * 0.005
        noise_val = noise.__call__(scaled_x, scaled_y)
        angle = noise_val * math.pi * 5
        grid[column][row] = angle

for e in range(0, 500):
    for f in range(0, 500):
        x = e
        y = f
        num_steps = 1
        step_length = 1
        x1 = x
        y1 = y
        color = random.choice(
            ['midnightblue', 'navy', 'mediumblue', 'blue',
             'royalblue', 'dodgerblue', 'cornflowerblue', 'skyblue', 'darkturquoise', 'turquoise']
        )

        for _ in range(num_steps):
            idraw.point((x1, y1), color)
            x_offset = x - left_x
            y_offset = y - top_y
            column_index = int(x_offset / resolution)
            row_index = int(y_offset / resolution)
            grid_angle = grid[column_index][row_index]
            x_step = step_length * math.cos(grid_angle)
            y_step = step_length * math.sin(grid_angle)
            x = x + x_step
            y = y + y_step
            x1 = x + random.choice([x_step, x_step]) * 1
            y1 = y + random.choice([y_step, y_step]) * 1

img.save('canvas.png')
img.show()