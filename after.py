# after.py
PI = 3.1415926  # 定义常量，消除魔法数字

def calculate_square_area(side):
    return side * side

def calculate_circle_area(radius):
    return PI * radius * radius

def print_area(shape, area):
    print(f"{shape}面积是: {area}")

# 调用函数，复用通用的打印逻辑
square_area = calculate_square_area(5)
print_area("正方形", square_area)

circle_area = calculate_circle_area(3)
print_area("圆形", circle_area)