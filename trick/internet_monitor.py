# coding: utf-8
import psutil


def get_key():
    key_info = psutil.net_io_counters(pernic=True).keys()  # 获取网卡名称

    recv = {}
    sent = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)  # 各网卡接收的字节数
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)  # 各网卡发送的字节数

    return key_info, recv, sent


def get_rate(func):
    import time
    delay = 5
    key_info, old_recv, old_sent = func()  # 上一秒收集的数据

    time.sleep(delay)

    key_info, now_recv, now_sent = func()  # 当前所收集的数据

    net_in = {}
    net_out = {}
    net_in_total = {}
    net_out_total = {}

    for key in key_info:
        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024 / delay)  # 每秒接收速率
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024 / delay)  # 每秒发送速率
        net_in_total.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)
        net_out_total.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024)
    return key_info, net_in, net_out, net_in_total, net_out_total, delay


if __name__ == '__main__':
    while 1:
        try:
            key_info, net_in, net_out, net_in_total, net_out_total, delay = get_rate(get_key)

            print('%ds内：' % delay)
            for key in key_info:
                print('%s\nInput:\t %-5sKB/s\t TotalInput:\t %-5sKB\nOutput:\t %-5sKB/s\t TotalOutput:\t %-5sKB\n' % (key, net_in.get(key), net_in_total.get(key), net_out.get(key), net_out_total.get(key)))
            print('===================================================')
        except KeyboardInterrupt:
            exit()
