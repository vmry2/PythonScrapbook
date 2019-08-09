from collections import namedtuple

dict_color = {"red": 55, "green": 155, "blue": 255}

Color = namedtuple("Color", ["red", "green", "blue"])

# color = Color(55, 155, 255)
color = Color(red=55, green=155, blue=255)
white = Color(255, 255, 255)

# print(color["red"])
print(color.red)
print(white)
