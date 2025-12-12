import requests
import pandas

import math_util
import wheather_forecast
import json_placeholder

while True:
    print("What u want to do ???")
    print("1.Area Calculations")
    print("2.Putting into file Json Placeholder data")
    print("3.Wheather forecasting for a city")
    print("4.Exit")

    x = int(input("Enter Choice : "))

    match x:
        case 1:
            math_util.Compute.Area()

        case 2:
            url="https://jsonplaceholder.typicode.com/posts"
            json_placeholder.Json.getJsonData(url)

        case 3:
            api="fae1b8ea39a0e9063e0b1f9eb627e314"
            city=input("Enter city : ")
            wheather_forecast.wheather.forecast(api,city)

        case 4:
            print("Exited...!")
            break

        case _:
            print("Invalid Choice , try again ..!")
