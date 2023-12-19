import numpy as np
import matplotlib.pyplot as plt


def separate_circles(mat, circles):
    """
    将一组圆按照对角矩阵的元素进行分离
    """
    separated_circles = []

    for i, circle in enumerate(circles):
        diagonal_element = abs(mat[i, i])
        separated_circles.append({
            'center': circle['center'],
            'radius': circle['radius'] * diagonal_element
        })

    return separated_circles


row_num = int(input("输入矩阵的行数:"))

# 用0初始化矩阵
mat = [[0] * row_num for _ in range(row_num)]

# 输入字符串并将其转为复数类型
mat = [[complex(j) for j in input().split()] for _ in range(row_num)]

mat = np.array(mat)
print("输入的矩阵:")
print(mat)

# 画圆采样
sample = np.linspace(-np.pi, np.pi, 100)

# 保持x，y轴刻度比例相同
plt.axis('equal')

circles = []

for i in range(row_num):
    # 行盖尔圆半径
    r = sum(abs(mat[i, :])) - abs(mat[i, i])

    # 盖尔圆圆心
    point_x = mat[i, i].real  # 实部
    point_y = mat[i, i].imag  # 虚部

    # 绘制圆心
    plt.plot(point_x, point_y, '.b')

    # 绘制圆（填充）
    circle, = plt.fill(r * np.sin(sample) + point_x,
                       r * np.cos(sample) + point_y,
                       'b',
                       alpha=0.2)

    circles.append({'center': (point_x, point_y), 'radius': r, 'plot': circle})

    # 标注
    plt.text(point_x,
             point_y,
             "G" + str(i + 1),
             fontdict={
                 'size': '12',
                 'color': 'k'
             })

# 绘制特征值点
[e, _] = np.linalg.eig(mat)  # 求出方阵的特征值和特征向量
for i, eigenvalue in enumerate(e):
    plt.plot(eigenvalue.real, eigenvalue.imag, 'ro')

print(circles)
print(np.diag(e))

# 分离盖尔圆
separated_circles = separate_circles(np.diag(e), circles)

for circle in separated_circles:
    plt.fill(circle['radius'] * np.sin(sample) + circle['center'][0],
             circle['radius'] * np.cos(sample) + circle['center'][1],
             'g',
             alpha=0.2)

# 配置图形属性
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plt.xlabel('实部')
# plt.ylabel('虚部')
# plt.title('盖尔圆与特征值散点图')

plt.show()
