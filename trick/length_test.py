import numpy as np
import cv2
from treelib import Node, Tree


def tree_test():
    tree = Tree()
    tree.create_node((1,1), 1)
    tree.create_node(2, 2, parent=1)
    tree.create_node(4, parent=1)
    tree.create_node(4, parent=2)
    # tree.show()
    print(tree)


def img_test():
    img = cv2.imread('../file_dir/ithin.png', cv2.IMREAD_GRAYSCALE)
    # cv2.imshow("", img)
    # cv2.waitKey()
    height = img.shape[0]
    width = img.shape[1]
    curve_list = []
    former_point = None
    for row in range(height):  # 遍历每一行
        for col in range(width):  # 遍历每一列
            if img[row][col] == 0:
                curve_list.append((row, col))  # (行号，列号）
                if former_point is None:
                    former_point = (row, col)
                else:
                    pass
    print(curve_list)


if __name__ == '__main__':
    tree_test()

