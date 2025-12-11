import requests
try:
    url="https://nilesh-g.github.io/learn-web/data/novels.json"
    response=requests.get(url)
    print("Status code : ",response.status_code)
    # data=response.text
    data=response.json()
    print(data)
except Exception as e:
    print("Exception : ",e)
