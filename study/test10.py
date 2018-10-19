# -*-coding:utf-8-*-

# http://docs.python-requests.org/en/latest/user/quickstart
import requests
import os

r1 = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(r1.json())

payload = {'key1': 'value1', 'key2': 'value2'}
r2 = requests.get('https://httpbin.org/get', params=payload)
print(r2.url)
print(r2.content)
print(r2.text)

r3 = requests.put('https://httpbin.org/put', data = {'key':'value'})
r4 = requests.delete('https://httpbin.org/delete')
r5 = requests.head('https://httpbin.org/get')
r6 = requests.options('https://httpbin.org/get')

headers = {'user-agent': 'my-app/0.0.1'}
r7 = requests.get('https://api.github.com/some/endpoint', headers=headers)
print(r7.headers)

files = {'file': open('d:/1.png', 'rb')}

r = requests.post('https://httpbin.org/post', files=files)
print(r.text)

try:
    f = open('d:/1.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# with 自動close
with open('d:/1.txt', 'w+') as f:
    f.write('add next')
    # 重置指針
    f.seek(os.SEEK_SET)
    print(f.read())
