import os
import math

def draw_triangle(svg, x1, y1, x2, y2, x3, y3):
    svg.write(f'<polygon points="{x1},{y1} {x2},{y2} {x3},{y3}" style="fill:black;stroke:none" />\n')

def sierpinski(svg, x1, y1, x2, y2, x3, y3, depth):
    if depth == 0:
        draw_triangle(svg, x1, y1, x2, y2, x3, y3)
    else:
        mx12 = (x1 + x2) / 2.0
        my12 = (y1 + y2) / 2.0
        mx23 = (x2 + x3) / 2.0
        my23 = (y2 + y3) / 2.0
        mx31 = (x3 + x1) / 2.0
        my31 = (y3 + y1) / 2.0
        sierpinski(svg, x1, y1, mx12, my12, mx31, my31, depth - 1)
        sierpinski(svg, x2, y2, mx23, my23, mx12, my12, depth - 1)
        sierpinski(svg, x3, y3, mx31, my31, mx23, my23, depth - 1)

def drawing(depth):
    width = 800
    height = 700
    # Получаем путь к папке, где лежит этот скрипт
    script_dir = os.path.dirname(os.path.abspath(__file__))
    svg_path = os.path.join(script_dir, "sierpinski.svg")
    with open(svg_path, "w", encoding="utf-8") as svg:
        svg.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
        svg.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">\n')
        svg.write('<rect width="100%" height="100%" fill="white" />\n')
        side = width * 0.85
        x1 = (width - side) / 2.0
        y1 = height - 50
        x2 = x1 + side
        y2 = height - 50
        x3 = x1 + side / 2.0
        y3 = height - 50 - side * math.sqrt(3) / 2.0
        sierpinski(svg, x1, y1, x2, y2, x3, y3, depth)
        svg.write('</svg>\n')
    print(f"Готово! Откройте файл {svg_path} в браузере.")

if __name__ == "__main__":
    depth = int(input("Введите глубину рекурсии: "))
    drawing(depth)
