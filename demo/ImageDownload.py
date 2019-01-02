import requests
from PIL import Image
from io import BytesIO


def downloadImg():
    rq = requests.get(
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1546084018162&di=6f17b272e4e5d12eec5b26265577b558&imgtype=0&src=http%3A%2F%2Fcdn.duitang.com%2Fuploads%2Fitem%2F201504%2F23%2F20150423H5215_HwXEv.jpeg"
    )
    img = Image.open(BytesIO(rq.content))
    img.save(r"D:\testPy.jpg")


if __name__ == '__main__':
    downloadImg()
