def power(x, n = 2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


print(power(3, 3))


def enroll(name, sex, school = "垃圾学校", city = "BJ"):
    print("name:\t ", name)
    print("sex:\t", sex)
    print("school:\t", school)
    print("city:\t", city)


print(enroll("杨帆", "女性", "清华"))

# 指定参数传入
print(enroll("杨帆", "女性", city = "HZ"))
