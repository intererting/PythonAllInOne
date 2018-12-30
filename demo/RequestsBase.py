import requests


def requestsBase():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    url = "https://www.baidu.com"
    response = requests.get(url, headers=headers)
    with open('D:\\test.txt', 'w', encoding='utf-8') as fd:
        fd.write(response.content.decode(encoding='utf-8'))


if __name__ == '__main__':
    requestsBase()
