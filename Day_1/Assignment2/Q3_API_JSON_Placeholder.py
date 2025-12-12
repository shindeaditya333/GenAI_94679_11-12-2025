import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response=requests.get(url)
print(f"Status code : {response.status_code}")

datatext=response.text
data=response.json()

try:
    with open("JSON_Placeholder_data.txt","w+") as file:
        json.dump(data,file)
        file.write("\n\nText Data :\n")
        file.write(datatext)
        print("Data added in file Successfully !")
except Exception as e:
    print("Exception :\n",e)
    


