import requests
import json

data = {
    '_date': '2018-11-29 14:25:31',
    'ip': '202.204.62.62',
    'host': 'G3_4GTX1080Ti',
    'gpu_nums': 4,
    'gpu_info': {
      '0': {
        'status': '10006.0M/10240.0M',
        'percentage': 95,
      },
      '1': {
        'status': '10006.0M/10240.0M',
        'percentage': 20,
      },
      '2': {
        'status': '10006.0M/10240.0M',
        'percentage': 55,
      },
      '3': {
        'status': '10006.0M/10240.0M',
        'percentage': 65,
      },
    }
}

res = requests.post('http://localhost:5000/api/ping', json.dumps(data))
print(res.text, res.status_code)
