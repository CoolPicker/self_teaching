from urllib3 import encode_multipart_formdata
import requests

"""
    post接口，上传图片
"""

data = {}
header = {}
data['file'] = ('t4.png', open('C:\\Users\\nya\\Desktop\\srfPicTextRecog-online\\test\\t4.png', 'rb').read())
encode_data = encode_multipart_formdata(data)
data = encode_data[0]
header['Content-Type'] = encode_data[1]
url = 'http://172.18.28.100:58088/image/file'
r = requests.post(url, headers=header, data=data)
res = str(r.content, encoding='utf-8')
print(res)

