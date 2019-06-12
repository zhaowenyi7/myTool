import os
import re

dir_path = 'E:/data/0528/001_test/'


def sub_replace(fpath):
    file_list = os.listdir(fpath)
    n = 0
    for f in file_list:
        old_name = fpath + file_list[n]
        new_name = re.sub('-', '_', old_name)
        os.rename(old_name, new_name)
        n += 1


def zero_blank_replace(fpath):
    file_list = os.listdir(fpath)
    n = 0
    for f in file_list:
        old_name = fpath + file_list[n]
        file_array = old_name.split('-')
        new_name = file_array[0] + '-'
        index = 1
        while index < 6:
            new_name += file_array[index].zfill(2) + '-'
            index += 1

        new_name += file_array[6].zfill(7)
        n += 1
        os.rename(old_name, new_name)


if __name__ == '__main__':
    zero_blank_replace(dir_path)

