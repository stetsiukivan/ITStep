print("Hello Git!")

from math_functions import rectangle_area, rectangle_perimeter

side_a = 8
side_b = 5

area = rectangle_area(side_a, side_b)
perimeter = rectangle_perimeter(side_a, side_b)

print(f"Площадь прямоугольника со сторонами {side_a} и {side_b} равна: {area}")
print(f"Периметр прямоугольника со сторонами {side_a} и {side_b} равен: {perimeter}")