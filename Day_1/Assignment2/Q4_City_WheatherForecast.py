import requests

api="fae1b8ea39a0e9063e0b1f9eb627e314"

city=input("Enter city : ")
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

response=requests.get(url)
print("Status code : ",response.status_code)

datatext=response.text
datajson=response.json()

# print(datatext)
# print()
# print(datajson)

print("\nTemperature : ",datajson["main"]["temp"])
print("Humidity : ",datajson["main"]["humidity"])
print("WindSpeed : ",datajson["wind"]["speed"])
