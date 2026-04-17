import time
import hashlib
import requests
import json

"""
接口功能:从外网拉取文件，接口内容拉下来后，开发会转成dll
无畏sdk文件限流策略：
1、每秒最大支持单节点1000个请求（本地限流）次数不可调
2、一个ip一分钟最多请求20次 （次数可调）
3、5s内最大支持100次 请求 （次数可调）
"""

# 配置参数
key = "fageE3dDHr3!tHW8"
timestamp = int(time.time() * 1000)
ip = "192.168.35.154"
mac = "4CEDFB411CD0"
file_token = "sdk"
my_sign = hashlib.md5(f"fileToken={file_token}&timestamp={timestamp}{key}".encode('utf-8')).hexdigest()

# 3. 构建请求参数
params = {
    "key":key,
    "fileToken": file_token,
    "sign": my_sign,
    "ip": ip,
    "mac": mac,
    "timestamp": timestamp
}

# 4. 构建 URL
url = f"https://zhanba-expert-test.stnts.com/manage/server-outer/wwval/{my_sign[:10]}"

# 5. 发送请求
response = requests.post(url, data=json.dumps(params),stream=True, headers={'Content-Type': 'application/json'})


print(f"Response: {response.text[:20]}")
print(f"状态码: {response.status_code}")
print(f"响应头 Content-Length: {response.headers.get('Content-Length')}")