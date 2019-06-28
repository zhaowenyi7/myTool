import pymysql
import matplotlib.pyplot as plt
import numpy as np

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='visualloc',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "SELECT `time`, `z_corrected` FROM `axis`"
        cursor.execute(sql)
        result = cursor.fetchall()
        xAxis = []
        yAxis = []
        for singleRec in result:
            xAxis.append(singleRec['time'])
            yAxis.append(singleRec['z_corrected'])
        print(result)
        print(xAxis)
        x = [n for n in range(1, len(xAxis) + 1)]
        xMat = np.mat(x).T
        print(yAxis)
        plt.figure()
        plt.plot(xMat, yAxis)
        plt.title(u'目标点位移时程曲线', fontproperties="KaiTi", fontsize=20)
        plt.ylabel(u'竖直方向坐标/mm', fontproperties="SimHei")
        plt.xlabel(u'采样时间', fontproperties="SimHei")
        plt.savefig('E:/out/axis_z_' + xAxis[0] + '.png')
finally:
    connection.close()
