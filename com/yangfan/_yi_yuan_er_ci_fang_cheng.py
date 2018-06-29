import math

print("请输入一元二次方程\"ax^2+bx+c =0\"的三个参数")
p1 = int(input())  # raw input get str
print("a: %s" % p1)

p2 = int(input())
print("b: %s" % p2)

p3 = int(input())
print("c: %s" % p3)


def quadratic(a, b, c):
    # 啊啊啊
    root = math.pow(b, 2) - 4 * a * c
    div = 2 * a
    if root < 0:
        return "error"
    else:
        x1 = (-b + math.sqrt(root)) / div
        x2 = (-b - math.sqrt(root)) / div
    return [x1, x2]


print(quadratic(p1, p2, p3))
