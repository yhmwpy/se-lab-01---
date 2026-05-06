# before.py
def calculate_area_of_square(side):
    area = side * side
    print(f"正方形面积是: {area}")
    return area

def calculate_area_of_square_v2(side):
    area = side * side  # 和上面的函数几乎完全重复
    print(f"正方形面积是: {area}")
    return area

def calculate_area_of_circle(radius):
    area = 3.14 * radius * radius  # 魔法数字3.14，没有定义常量
    print(f"圆形面积是: {area}")
    return area

# 调用函数
calculate_area_of_square(5)
calculate_area_of_square_v2(5)
calculate_area_of_circle(3)