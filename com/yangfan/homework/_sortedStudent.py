'''
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

请用sorted()对上述列表分别按名字排序：

'''
def printStudent(r):
    for i, v in r:
        print('[', i, ',', v, ']', end = ' ')
    print()

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def sort_student_tuple_by_name(L):
    return sorted(L, key = byName)


def sort_student_tuple_by_score(L, desc):
    return sorted(L, key=byScore, reverse = desc)


def byName(t):
    return str.lower(t[0])  # 注意tuple里的元素是靠下标访问的

def byScore(t):
    return t[1]             # 注意 按照成绩排序也必须将tuple里面的成绩取出来


r = sort_student_tuple_by_name(L)
printStudent(r)
r = sort_student_tuple_by_score(L,True)
printStudent(r)
r = sort_student_tuple_by_score(L,False)
printStudent(r)



