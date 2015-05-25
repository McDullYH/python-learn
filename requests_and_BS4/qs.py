import requests

# send a request and get a response

# raw request
response=requests.request('GET','http_url')

# request method
response=requests.get('http_url')
response=requests.post('http_url')
response=requests.put('http_url')
response=requests.delete('http_url')
response=requests.head('http_url')
response=requests.patch('http_url')

# custom GET similar with POST
payload={'key1':'value1','key2':'value2'}
response=requests.get('http_url',payload)
print r.url
# output: http_url?key2=value2&key1=value1

# custom HEAD 
payload={'key':'value'}
headers={'content-type':'application/json'}
res=request.post('http_url',data=json.dumps(payload),headers=headers)

# timeouts
request.get(url,timeout=0.001)


# class
# Request
req=requests.request('GET','http_url')
req.prepare()

# Response
res=requests.get('http_url')
res.headers
res.headers['content-type']
res.headers.get('content-type')
res.text                # 输出以unicode 编码后的内容 事先用res.encoding解码res.content
res.encoding
res.content             # ***内容 未编码 (bytes)***
res.json()
res.raw         # http raw response
res.status_code

if res.status_code == requests.codes.ok:
    pass

# access cookies
res.cookies['cookies_name']
# send cookies
cookies = dict(cookies_are='working')
res=request.get(url,cookies=cookies)
res.text
# output {"cookies":{"cookies_are":"working"}}

r.history




# Sessions
s = requests.Session()
s.get('http_url')
s.head('http_url')




