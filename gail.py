import numpy as np
import matplotlib.pyplot as plt

row_num = int(input("input nums of row:"))

# 用0初始化矩阵
# mat = [[0] * row_num] * row_num
# 避免创建具有相同内部引用的行，使用列表推导式来创建矩阵，确保每一行都是独立的。
mat = [[0] * row_num for _ in range(row_num)]

# 字符串分割成数字并转为复数类型
# for i in range(row_num):
#     mat[i] = input().split()
#     mat[i] = [complex(j) for j in mat[i]]

# 字符串分割成数字并转为复数类型
mat = [[complex(j) for j in input().split()] for _ in range(row_num)]

mat = np.array(mat)
print(mat)

# 画圆采样
sample = np.linspace(-np.pi, np.pi, 100)

# 保持x，y轴刻度比例相同
plt.axis('equal')

for i in range(row_num):
    # 行盖尔圆半径
    r1 = sum(abs(mat[i, :])) - abs(mat[i][i])
    # 列盖尔圆半径
    r2 = sum(abs(mat[:, i])) - abs(mat[i][i])

    # 盖尔圆圆心
    point_x = mat[i][i].real  # 实部
    point_y = mat[i][i].imag  # 虚部
    print(point_x,point_y)


    # 绘制圆心
    plt.plot(point_x, point_y, '.b')

    # 绘制圆（填充）
    plt.fill(r1 * np.sin(sample) + point_x,
             r1 * np.cos(sample) + point_y,
             'b',
             alpha=0.2)

    # plt.fill(r2 * np.sin(sample) + point_x,
    #          r2 * np.cos(sample) + point_y,
    #          'g',
    #          alpha=0.2)

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
for i in e:
    plt.plot(i.real, i.imag, 'ro')
ax = plt.gca()
# 去掉默认边框刻度
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置x与y轴的位置
ax.spines['bottom'].set_position(('data', 0)) # 表示设置底部轴移动到竖轴的0坐标位置
ax.spines['left'].set_position(('data', 0))

# 指定x与y轴刻度数字位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()
