import os
import yaml
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import collections

yaml.warnings({'YAMLLoadWarning': False})
current_path = os.path.abspath(os.path.dirname(__file__))
print(current_path)
print(current_path + './test_dir')
origin_path = 'E:/code/visualLocalization/visualLocalization/fpsRecord_origin.yml'
kalman_path = 'E:/out/fpsRecord_kalman.yml'
with open(kalman_path, 'r') as originf:
    origin_data = originf.read()
    subYaml = origin_data.split('\n')
    with open(current_path + './test_dir/' + 'fpsRecord_test.yml', 'w') as wf:
        i = 2
        while i < len(subYaml):
            if subYaml[i] != '---' and subYaml[i] != '...':
                wf.write(subYaml[i] + '\n')
            i += 1

with open(current_path + './test_dir/' + 'fpsRecord_test.yml', 'r') as f:
    temp = yaml.load(f.read())
    # temp = yaml.load(f.read(), Loader=yaml.safe_load)
    temp = collections.OrderedDict(temp)
    keys = list(temp.keys())
    values = temp.values()
    axis = []
    for val in values:
        axis.append(val)

    # print(axis)
    # print(np.shape(axis))
    name = keys[0].split("_")[1]
    axis_mat = np.mat(axis)
    z = axis_mat[:, 2] * 1000  # 转化为毫米
    z_0 = np.max(z)  # 零位（最高点）
    z_max_axis = np.min(z)  # 最大挠度（最低点）
    z_max_trans = z_0 - z_max_axis  # 最大位移（极差）

    x = [n for n in range(1, z.shape[0] + 1)]
    xMat = np.mat(x).T  # 数组转矩阵，数值操作

    plt.figure()
    plt.plot(xMat, z - z_0)
    plt.title(u'目标点位移时程曲线', fontproperties="KaiTi", fontsize=20)
    plt.ylabel(u'竖直方向坐标/mm', fontproperties="SimHei")
    plt.xlabel(u'采样时间', fontproperties="SimHei")
    plt.savefig('E:/out/axis_z_kalman_' + name + '.png')

    # h = axis_mat[:, 0] * 1000  # 转化为毫米
    # h_0 = np.max(h)  # 零位（最高点）
    # h_max_axis = np.min(h)  # 最大挠度（最低点）
    # h_max_trans = h_0 - h_max_axis  # 最大位移（极差）
    # plt.figure()
    # plt.plot(xMat, h_0 - h)
    # plt.title(u'目标点位移时程曲线', fontproperties="KaiTi", fontsize=20)
    # plt.ylabel(u'水平方向坐标/mm', fontproperties="SimHei")
    # plt.xlabel(u'时间/s', fontproperties="SimHei")
    # plt.savefig("axis_x.png")

with open(origin_path, 'r') as originf:
    origin_data = originf.read()
    subYaml = origin_data.split('\n')
    with open(current_path + './test_dir/' + 'fpsRecord_test.yml', 'w') as wf:
        i = 2
        while i < len(subYaml):
            if subYaml[i] != '---' and subYaml[i] != '...':
                wf.write(subYaml[i] + '\n')
            i += 1

with open(current_path + './test_dir/' + 'fpsRecord_test.yml', 'r') as f:
    temp = yaml.load(f.read())
    # temp = yaml.load(f.read(), Loader=yaml.safe_load)
    temp = collections.OrderedDict(temp)
    keys = list(temp.keys())
    values = temp.values()
    axis = []
    for val in values:
        axis.append(val)

    # print(axis)
    # print(np.shape(axis))
    name = keys[0].split("_")[1]
    axis_mat = np.mat(axis)
    z = axis_mat[:, 2] * 1000  # 转化为毫米
    z_0 = np.max(z)  # 零位（最高点）
    z_max_axis = np.min(z)  # 最大挠度（最低点）
    z_max_trans = z_0 - z_max_axis  # 最大位移（极差）

    x = [n for n in range(1, z.shape[0] + 1)]
    xMat = np.mat(x).T  # 数组转矩阵，数值操作

    plt.figure()
    plt.plot(xMat, z - z_0)
    plt.title(u'目标点位移时程曲线', fontproperties="KaiTi", fontsize=20)
    plt.ylabel(u'竖直方向坐标/mm', fontproperties="SimHei")
    plt.xlabel(u'采样时间', fontproperties="SimHei")
    plt.savefig('E:/out/axis_z_origin_' + name + '.png')

os.rename(kalman_path, 'E:/out/fpsRecord_kalman_' + name + '.yml')
