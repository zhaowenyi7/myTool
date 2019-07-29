import time
import random

import pymysql


def generate_time():
    t_now = time.time()
    t_sec = int(t_now)
    t_milisec = int(round(t_now * 1000))
    on_milisec = t_milisec - t_sec * 1000
    on_milisec_str = str.replace(str(t_milisec), str(t_sec), "")
    time_array = time.localtime(t_sec)
    now02 = time.strftime('%Y-%m-%d %H:%M:%S', time_array)
    # print(t_sec)
    # print(t_milisec)
    # print(on_milisec)
    # print(now02)
    milisec_str = now02 + ':' + on_milisec_str
    return milisec_str


def generate_float():
    return round(random.uniform(0, 50), 4)


if __name__ == '__main__':
    while True:
        time_now = generate_time()
        data = generate_float()
        print(time_now, data)
        # 建立数据库连接
        db_connection = pymysql.connect(host='localhost',
                                        user='root',
                                        password='root',
                                        db='visualloc',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor)
        cursor = db_connection.cursor()
        try:
            sql = "INSERT INTO fake_data VALUES('" + time_now + "'," + str(data) + ");"
            cursor.execute(sql)
            db_connection.commit()
        except Exception:
            print('sql error, please check it')
            db_connection.rollback()
        finally:
            db_connection.close()
        time.sleep(0.2)
