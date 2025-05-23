import requests

response = requests.get('https://www.baidu.com')
print(response.status_code)  # 状态码 (200, 404等)
#print(response.text)         # 响应内容文本（自动解码）
#print(response.json())       # 若响应为 JSON，直接解析为字典



