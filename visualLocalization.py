import os
import yaml
import numpy as np
import matplotlib.pyplot as plt

current_path = os.path.abspath(os.path.dirname(__file__))
print(current_path)
print(current_path + './test_dir')

with open('E:/code/visualLocalization/visualLocalization/fpsRecord_test.yml', 'r') as originf:
    origin_data = originf.read()
    subYaml = origin_data.split('\n')
    with open(current_path + './test_dir/' + 'fpsRecord_test.yml', 'w') as wf:
        i = 2
        while i < len(subYaml):
            if subYaml[i] != '---' and subYaml[i] != '...':
                wf.write(subYaml[i] + '\n')
            i += 1

with open(current_path + './test_dir/' + 'fpsRecord_test.yml', 'r') as f:
    temp = yaml.load(f.read(), Loader=yaml.FullLoader)
    keys = temp.keys()
    values = temp.values()
    axis = []
    for val in values:
        axis.append(val)

    # print(axis)
    # print(np.shape(axis))
    axis_mat = np.mat(axis)
    z = axis_mat[:, 2] * 1000  # 转化为毫米
    z_0 = np.max(z)  # 零位（最高点）
    z_max_axis = np.min(z)  # 最大挠度（最低点）
    z_max_trans = z_0 - z_max_axis  # 最大位移（极差）

    x = [n for n in range(1, z.shape[0] + 1)]
    xMat = np.mat(x).T * 0.2  # 数组转矩阵，数值操作

    plt.figure()
    plt.plot(xMat, z - z_0)
    plt.title(u'目标点位移时程曲线', fontproperties="KaiTi", fontsize=20)
    plt.ylabel(u'竖直方向坐标/mm', fontproperties="SimHei")
    plt.xlabel(u'时间/s', fontproperties="SimHei")
    plt.savefig("axis_z.png")

    h = axis_mat[:, 0] * 1000  # 转化为毫米
    h_0 = np.max(h)  # 零位（最高点）
    h_max_axis = np.min(h)  # 最大挠度（最低点）
    h_max_trans = h_0 - h_max_axis  # 最大位移（极差）
    plt.figure()
    plt.plot(xMat, h_0 - h)
    plt.title(u'目标点位移时程曲线', fontproperties="KaiTi", fontsize=20)
    plt.ylabel(u'水平方向坐标/mm', fontproperties="SimHei")
    plt.xlabel(u'时间/s', fontproperties="SimHei")
    plt.savefig("axis_x.png")

