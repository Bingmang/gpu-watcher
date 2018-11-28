import requests
import json
import socket
import time
import pynvml

HOST = 'G1_4GTX1080Ti'
GPU_NUMS = 4
target = 'http://localhost:5000/ping'

pynvml.nvmlInit()
handle_list = [pynvml.nvmlDeviceGetHandleByIndex(i) for i in range(GPU_NUMS)]


def get_host_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        return ip


def get_gpu_info():
    gpu_info = {}
    for i in range(len(handle_list)):
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle_list[i])
        gpu_info[i] = '{:.1f}M/{:.1f}M ({}%)'.format(meminfo.used / 2**20,
                                                     meminfo.total / 2**20, round(meminfo.used / meminfo.total * 100))
    return gpu_info


if __name__ == "__main__":
    ip = get_host_ip()
    body = {'ip': ip, 'host': HOST, 'gpu_nums': GPU_NUMS,
            'gpu_info': {}, '_date': time.time()}
    error_count = 0
    while True:
        body['_date'] = int(time.time())
        body['gpu_info'] = get_gpu_info()
        res = requests.post(target, json.dumps(body))
        if res.status_code != 200:
            error_count += 1
            print(res.text, res.status_code)
            if error_count > 3:
                break
        else:
            error_count = 0
        time.sleep(10)
