import numpy as np
import matplotlib.pyplot as plt

# 显示中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def separate_gershgorin_circles(original_matrix, diagonal_matrix):
    # 通过对角矩阵和其逆矩阵乘积，分离盖尔圆
    separated_row_matrix = np.dot(diagonal_matrix, np.dot(original_matrix, np.linalg.inv(diagonal_matrix)))
    separated_column_matrix = np.dot(np.linalg.inv(diagonal_matrix), np.dot(original_matrix, diagonal_matrix))

    # 创建一个画布，包含四个子图
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

    # 画出原始矩阵的行盖尔圆
    plot_gershgorin_circles(original_matrix, axes[0, 0], title="原始矩阵的行盖尔圆")

    # 画出分离后的行盖尔圆
    plot_gershgorin_circles(separated_row_matrix, axes[0, 1], title="分离后的行盖尔圆")

    # 画出原始矩阵的列盖尔圆
    plot_gershgorin_circles(original_matrix.T, axes[1, 0], title="原始矩阵的列盖尔圆")

    # 画出分离后的列盖尔圆
    plot_gershgorin_circles(separated_column_matrix.T, axes[1, 1], title="分离后的列盖尔圆")

    # 调整布局，使子图之间有一些间隔
    plt.tight_layout()

    # 显示画布
    plt.show()

def plot_gershgorin_circles(matrix, ax, title="盖尔圆"):
    row_num = matrix.shape[0]
    sample = np.linspace(-np.pi, np.pi, 100)

    ax.set_title(title)
    ax.axis('equal')

    for i in range(row_num):
        # 计算盖尔圆半径
        r = sum(np.abs(matrix[i, :])) - np.abs(matrix[i, i])

        # 获取盖尔圆圆心坐标
        point_x, point_y = matrix[i, i].real, matrix[i, i].imag

        # 绘制圆心
        ax.plot(point_x, point_y, '.b')

        # 绘制盖尔圆（填充）
        ax.fill(r * np.sin(sample) + point_x, r * np.cos(sample) + point_y, 'b', alpha=0.2)

        # 添加标签
        ax.text(point_x, point_y, "G" + str(i + 1), fontdict={'size': '12', 'color': 'k'})

# 用户输入对角矩阵的值
diagonal_values = [float(val) for val in input("输入对角矩阵的值，以空格分隔: ").split()]
diagonal_matrix = np.diag(diagonal_values)

# 用户输入原始矩阵的行数和元素值
row_num = int(input("输入原始矩阵的行数: "))
original_matrix = np.array([[complex(j) for j in input().split()] for _ in range(row_num)])

# 调用分离盖尔圆的函数并画图
separate_gershgorin_circles(original_matrix, diagonal_matrix)
