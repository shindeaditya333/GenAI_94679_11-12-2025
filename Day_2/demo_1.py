import requests
import os
from dotenv import load_dotenv

try :
    load_dotenv() # to load .env file bydefault 

    apikey=os.getenv("WEATHERMAP_API_KEY")
    city=input("Enter city : ")
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={apikey}&units=metric&q={city}"

    response=requests.get(url)
    print("Status code : ",response.status_code)

    data=response.json()

    print(data)
except Exception as e:
    print("Exception : ",e)