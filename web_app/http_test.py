import requests
import json


def get_test():
    geturl = 'http://192.168.0.48:8511/devices/12399/datapoints?items=disps'
    header = {
        "key": '123456',
        # 'Content-Type': 'application/json',
        # "Host": 'api.ruhrtec.cn'
    }
    r = requests.get(geturl, headers=header, auth=('root', 'ruhrroot86038610'))
    r.raise_for_status()
    rj = r.json()
    print(rj)
    print(r.status_code)


def git_get_test():
    r = requests.get('https://api.github.com/events')
    rj = r.json()
    print(rj)


def post_test():
    url = "http://192.168.0.48:8511/devices/12399/datapoints?type=2"

    data = {
        'disps': {
            '2019-07-19 13:44:49': 8.3,
            '2019-07-19 13:44:50': 8.2
        }
    }
    header = {
        "key": '123456',
        # 'Content-Type': 'application/json',
        # "Host": 'api.ruhrtec.cn'
    }
    r = requests.post(url, data=json.dumps(data), headers=header, auth=('root', 'ruhrroot86038610'))
    # r = requests.get(url, headers=header, auth=('root', 'ruhrroot86038610'), verify=True)
    r.raise_for_status()
    rj = r.json()
    print(rj)
    print(r.status_code)
    # print(r.headers)


if __name__ == '__main__':
    # post_test()
    get_test()