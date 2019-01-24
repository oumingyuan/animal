from django.http import HttpResponse
from aip import AipFace
import base64

""" 你的 APPID AK SK """
APP_ID = '15459757'
API_KEY = 'TeflwgR9RxI8haND8HI1atao'
SECRET_KEY = 'GaXWynsGRBGGeCPfAAwkSTnutDK3I7ti'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

print(client)


# print(result["result"]['face_list'])

def hello(request):
    """ 读取图片 """
    # E:\Picture\image
    # f = open('image/jjw.jpeg', 'rb')
    f = open('E:/Picture/image/xy2.jpg', 'rb')

    image = base64.b64encode(f.read())

    image64 = str(image, 'utf-8')

    image_type = "BASE64"

    """ 如果有可选参数 """
    # noinspection PyDictCreation
    options = {}
    options["face_field"] = "age,beauty,expression,gender,race"
    options["max_face_num"] = 1
    options["face_type"] = "LIVE"

    # result = client.detect(image64, image_type, {"face_field": "beauty"})
    result = client.detect(image64, image_type, options)

    print(result)

    return HttpResponse("Hello world ! ")
