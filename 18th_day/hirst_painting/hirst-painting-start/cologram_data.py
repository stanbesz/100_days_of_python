import colorgram

rgb_colors = []
colors = colorgram.extract('18th_day\hirst_painting\hirst-painting-start\image.jpg', 30)
for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)