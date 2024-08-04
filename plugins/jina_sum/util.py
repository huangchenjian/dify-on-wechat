import json

import requests

def upload_img(image_path):
    # 本地图片文件路径

    # token值，需从实际来源获取（例如读取tokenList文件）
    token = "50ba01c6f30d1244d7d819b6c32fbe29"

    # 目标URL
    url = "https://img2.520965.xyz/api/index.php"

    # 构建请求参数
    files = {'image': open(image_path, 'rb')}
    data = {'token': token}

    # 发送POST请求
    response = requests.post(url, files=files, data=data)
    img_url = None
    # 检查响应状态码
    if response.status_code == 200:
        text = json.loads(response.text)

        img_url = text['url']
        print("Upload successful.",img_url)
    else:
        print(f"Upload failed with status code {response.status_code}.")
    return img_url

if __name__ == '__main__':

    image_path = '../../tmp/20240731223208.jpg'
    a = upload_img(image_path)
