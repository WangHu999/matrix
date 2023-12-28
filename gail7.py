import numpy as np
import matplotlib.pyplot as plt

# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def separate_gershgorin_circles(original_matrix, row_diagonal_matrix, column_diagonal_matrix):
    # 分离行盖尔圆
    separated_row_matrix = np.dot(row_diagonal_matrix, np.dot(original_matrix, np.linalg.inv(row_diagonal_matrix)))

    # 分离列盖尔圆
    separated_column_matrix = np.dot(np.linalg.inv(column_diagonal_matrix),
                                     np.dot(original_matrix, column_diagonal_matrix))

    # 求解特征值
    eigenvalues_original, _ = np.linalg.eig(original_matrix)
    eigenvalues_separated_row, _ = np.linalg.eig(separated_row_matrix)
    eigenvalues_original_T, _ = np.linalg.eig(original_matrix.T)
    eigenvalues_separated_column, _ = np.linalg.eig(separated_column_matrix)

    # 创建一个画布，包含四个子图
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

    # 画出原始矩阵的行盖尔圆和特征值
    plot_gershgorin_circles(original_matrix, axes[0, 0], title="原始矩阵的行盖尔圆", eigenvalues=eigenvalues_original)

    # 画出分离后的行盖尔圆和特征值
    plot_gershgorin_circles(separated_row_matrix, axes[0, 1], title="分离后的行盖尔圆",
                            eigenvalues=eigenvalues_separated_row)

    # 画出原始矩阵的列盖尔圆和特征值
    plot_gershgorin_circles(original_matrix.T, axes[1, 0], title="原始矩阵的列盖尔圆",
                            eigenvalues=eigenvalues_original_T)

    # 画出分离后的列盖尔圆和特征值
    plot_gershgorin_circles(separated_column_matrix.T, axes[1, 1], title="分离后的列盖尔圆",
                            eigenvalues=eigenvalues_separated_column)

    # 调整布局，使子图之间有一些间隔
    plt.tight_layout()

    # 显示画布
    plt.show()


def plot_gershgorin_circles(matrix, ax, title="盖尔圆", eigenvalues=None):
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

    # 标注特征值
    if eigenvalues is not None:
        ax.plot(np.real(eigenvalues), np.imag(eigenvalues), 'ro', label='特征值')
        ax.legend()


# 用户输入行盖尔圆的对角矩阵的值
row_diagonal_values = [float(val) for val in input("输入行盖尔圆对角矩阵的值，以空格分隔: ").split()]
row_diagonal_matrix = np.diag(row_diagonal_values)

# 用户输入列盖尔圆的对角矩阵的值
column_diagonal_values = [float(val) for val in input("输入列盖尔圆对角矩阵的值，以空格分隔: ").split()]
column_diagonal_matrix = np.diag(column_diagonal_values)

# 用户输入原始矩阵的行数和元素值
row_num = int(input("输入原始矩阵的行数: "))
original_matrix = np.array([[complex(j) for j in input().split()] for _ in range(row_num)])

# 调用分离盖尔圆的函数并画图
separate_gershgorin_circles(original_matrix, row_diagonal_matrix, column_diagonal_matrix)
#

# 测试提交
# 测试提交
# 测试提交
