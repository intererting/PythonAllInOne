import os
from hashlib import md5
from io import BytesIO
from multiprocessing.pool import Pool
from urllib.parse import urlencode

import requests
from PIL import Image


def get_page(offset):
    headers = {
        'cookie': '__tasessionId=smu9e1orl1534840556591; csrftoken=c5959d05227f10ac569a61a259f5d72a; tt_webid=6592090000569353732; UM_distinctid=1655ba04d182b3-08fc945c63e051-514d2f1f-13c680-1655ba04d1918b; CNZZDATA1259612802=1317923562-1534839245-%7C1534839245',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print(e.args)
        return None


def getImages(json):
    if json.get('data'):
        for item in json.get('data'):
            if item:
                title = item.get('title')
                images = item.get('image_list')
                if images:
                    for image in images:
                        yield {
                            'title': title,
                            'image': image.get("url")
                        }


def formatPath(path):
    return 'D:\imagetest\\' + path


def saveImage(item):
    if not os.path.exists(formatPath(item.get('title'))):
        os.makedirs(formatPath(item.get('title')))
    try:
        response = requests.get("http:" + item.get("image"))
        if response.status_code == 200:
            file_path = '{0}\\{1}.{2}'.format(formatPath(item.get('title')), md5(response.content).hexdigest(), "jpg")
            print(file_path)
            if not os.path.exists(file_path):
                img = Image.open(BytesIO(response.content))
                img.save(file_path)
            else:
                print("image already exists")

    except requests.ConnectionError:
        print("failed save image")


def main(offset):
    json = get_page(offset)
    if json:
        for item in getImages(json):
            saveImage(item)


GROUP_START = 1
GROUP_END = 2

if __name__ == '__main__':
    pool = Pool()
    groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
    pool.map(main, groups)
    pool.close()
    pool.join()
