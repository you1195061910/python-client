#!/usr/bin/env python
# coding=utf-8

from aip import AipOcr

config = {
    'appId': '15192233',
    'apiKey': 'UfB0smfUhuz4D3m9wtTV5lK1',
    'secretKey': 'SDLkMjY9dSAtyGabKpgYbGoKuCa391fI'
}

client = AipOcr(**config)

# filePath = 'D:\gitSpace\python-client\screen'

# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# def img_to_str(image_path):
#     image = get_file_content('ocr-test2.png')
#     result = client.basicGeneral(image)
#     if 'words_result' in result:
#         return '\n'.join([w['words'] for w in result['words_result']])

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(r'D:\gitSpace\python-client\screen\ocr-test2.png')

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "false"
options["detect_language"] = "true"
options["probability"] = "false"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image, options)

words_result = result['words_result']
for x in words_result:
    print x['words']


